import pygame, sys
import numpy as np
pygame.init()

#constantes para a tela | Screen Constants
Width = 600
Height = 600
line_width = 10
board_rows = 3
board_cols = 3
circle_radius = 60
circle_width = 10
cross_width = 25
space = 55


#RGB
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0,96,255)
BLACK = (0,0,0)
WHITE = (251,255,255)

#criação da tela | Screen creation
screen = pygame.display.set_mode((Width, Height))

#printa as posições do tabuleiro | prints the board's positions
board = np.zeros((board_rows, board_cols))
print(board)

player = 1
game_over = False

#customizando a tela | customizing the screen
def screenPers():
    #colocando titulo | Setting title 
    pygame.display.set_caption("Jogo da Velha")

    #Muda a cor do fundo | change the background color
    screen.fill( LIGHT_BLUE )

screenPers()

#local de controle das jogadas no tabuleiro | local that it will be controled the plays of the game
def mark_Square(row, col, player):
    board[row][col] = player

#verificador se o local esta disponivel |checker if the location in the board is available
def available(row, col):
    return board[row][col] == 0

#verifica se o tabuleiro esta cheio | check if the board is full
def is_board_full():
    for row in range (board_rows):
        for col in range (board_cols):
            if board[row][col] == 0:
                return False
    return True

#desenha o X ou O | draw the X or O
def drawFigures():
    #loop para rodar todo o tabuleiro | loop for run all the board
    for row in range (board_rows):
        for col in range (board_cols):
            if board[row][col] == 1: 
                #desenhando o circulo | drawing the circle
                pygame.draw.circle(screen, WHITE, (int(col*200 + 100), int(row*200 + 100)), circle_radius, circle_width)
            elif board[row][col] == 2:
                #desenhando o X | drawing the X
                pygame.draw.line(screen, BLACK, (col * 200 + space, row * 200 + 200 - space), (col * 200 + 200 - space, row * 200 + space), cross_width)
                pygame.draw.line(screen, BLACK, (col * 200 + space, row * 200 + space), (col * 200 + 200 - space, row * 200 + 200 - space), cross_width)


def drawLine():
    #Desenha uma linha | Draw a line
    #linhas Horizontal | horizontal line
    pygame.draw.line(screen, BLUE, (0, 200), (600,200), line_width )
    pygame.draw.line(screen, BLUE, (0, 400), (600,400), line_width )
    #linha vertical | vertical line
    pygame.draw.line(screen, BLUE, (200, 0), (200,600), line_width )
    pygame.draw.line(screen, BLUE, (400, 0), (400,600), line_width )

#confere se o jogador ganhou | checks if the player won
def check_win(player):
    #vitoria na vertical | vertical win check
    for col in range(board_cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    #vitoria na horizontal | horizontal win check
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    #vitoria na diagonal | asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_ascending_diagonal(player)
        return True

    #vitoria na diagonal | asc diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    
    return False

#desenha a linha de vitoria na vertical | draw the vertical winning line
def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100

    if player == 1: 
        color = WHITE
    elif player == 2:
        color = BLACK

    pygame.draw.line(screen, color, (posX, 15), (posX, Height - 15), 15)

#desenha a linha de vitoria na horizontal | draw the horizontal winning line
def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 100

    if player == 1: 
        color = WHITE
    elif player == 2:
        color = BLACK

    pygame.draw.line(screen, color, (15, posY), (Width - 15, posY), 15)

#desenha a linha de vitoria na diagonal | draw the diagonal winning line
def draw_ascending_diagonal(player):
    if player == 1: 
        color = WHITE
    elif player == 2:
        color = BLACK
    
    pygame.draw.line(screen, color, (15, Height - 15), (Width - 15, 15), 15)

#desenha a linha de vitoria na diagonal | draw the diagonal winning line
def draw_desc_diagonal(player):
    if player == 1: 
        color = WHITE
    elif player == 2:
        color = BLACK

    pygame.draw.line(screen, color, (15, 15), (Width - 15, Height - 15), 15)

def restart(player):
    screen.fill( LIGHT_BLUE )
    drawLine()
    player = 1
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0
    

drawLine()

#def screenLoop(player, game_over):
    #loop para a tela de pygame | loop for pygame's screen
while True:
    for event in pygame.event.get():
        #se clicarmos no botao para sair da tela, a janela irá fechar | if we click in the button to close the sceen, it will close it 
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] #x
            mouseY = event.pos[1] #y
            #limita o click do mouse para um quadrado | limits the mouse click to a square
            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)
            #começa com o jogador 1 e quando ele jogar, ira trocar para o jogador 2 | start with p1, and after he plays, it will be p2
            if available(clicked_row, clicked_col):
                mark_Square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1

                drawFigures()

        #se clicar a tecla R, ira reiniciar o jogo | if the user clicks the R key, it will restart
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart(player)
                player = 1
                game_over = False
    #atualiza a tela | refresh the screen
    pygame.display.update()

screenLoop(player, game_over)