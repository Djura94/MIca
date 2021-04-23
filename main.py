import pygame
from alfabetarezanje import *
from heuristika import *

alfa = float('-inf')
beta = float('inf')
depth = 3

board = ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X",
         "X", "X"]
boardCirclesProp = [[(370, 60), (0, 0, 0), 1], [(670, 60), (0, 0, 0), 1], [(970, 60), (0, 0, 0), 1],
                    [(370, 360), (0, 0, 0), 1], [(970, 360), (0, 0, 0), 1], [(370, 660), (0, 0, 0), 1],
                    [(670, 660), (0, 0, 0), 1], [(970, 660), (0, 0, 0), 1], [(470, 160), (0, 0, 0), 1],
                    [(670, 160), (0, 0, 0), 1], [(870, 160), (0, 0, 0), 1], [(470, 360), (0, 0, 0), 1],
                    [(870, 360), (0, 0, 0), 1], [(470, 560), (0, 0, 0), 1], [(670, 560), (0, 0, 0), 1],
                    [(870, 560), (0, 0, 0), 1], [(570, 260), (0, 0, 0), 1], [(670, 260), (0, 0, 0), 1],
                    [(770, 260), (0, 0, 0), 1], [(570, 360), (0, 0, 0), 1], [(770, 360), (0, 0, 0), 1],
                    [(570, 460), (0, 0, 0), 1], [(670, 460), (0, 0, 0), 1], [(770, 460), (0, 0, 0), 1]]
circles = []


def drawboard(message):
    circles.clear()
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0, 0, 0), (390, 60), (650, 60), 1)
    pygame.draw.line(screen, (0, 0, 0), (690, 60), (950, 60), 1)
    pygame.draw.line(screen, (0, 0, 0), (370, 80), (370, 340), 1)
    pygame.draw.line(screen, (0, 0, 0), (370, 380), (370, 640), 1)
    pygame.draw.line(screen, (0, 0, 0), (970, 80), (970, 340), 1)
    pygame.draw.line(screen, (0, 0, 0), (970, 380), (970, 640), 1)
    pygame.draw.line(screen, (0, 0, 0), (390, 660), (650, 660), 1)
    pygame.draw.line(screen, (0, 0, 0), (690, 660), (950, 660), 1)
    pygame.draw.line(screen, (0, 0, 0), (490, 160), (650, 160), 1)
    pygame.draw.line(screen, (0, 0, 0), (690, 160), (850, 160), 1)
    pygame.draw.line(screen, (0, 0, 0), (590, 260), (650, 260), 1)
    pygame.draw.line(screen, (0, 0, 0), (690, 260), (750, 260), 1)
    pygame.draw.line(screen, (0, 0, 0), (390, 360), (450, 360), 1)
    pygame.draw.line(screen, (0, 0, 0), (490, 360), (550, 360), 1)
    pygame.draw.line(screen, (0, 0, 0), (790, 360), (850, 360), 1)
    pygame.draw.line(screen, (0, 0, 0), (890, 360), (950, 360), 1)
    pygame.draw.line(screen, (0, 0, 0), (590, 460), (650, 460), 1)
    pygame.draw.line(screen, (0, 0, 0), (690, 460), (750, 460), 1)
    pygame.draw.line(screen, (0, 0, 0), (490, 560), (650, 560), 1)
    pygame.draw.line(screen, (0, 0, 0), (690, 560), (850, 560), 1)
    pygame.draw.line(screen, (0, 0, 0), (470, 180), (470, 340), 1)
    pygame.draw.line(screen, (0, 0, 0), (470, 380), (470, 540), 1)
    pygame.draw.line(screen, (0, 0, 0), (570, 280), (570, 340), 1)
    pygame.draw.line(screen, (0, 0, 0), (570, 380), (570, 440), 1)
    pygame.draw.line(screen, (0, 0, 0), (870, 180), (870, 340), 1)
    pygame.draw.line(screen, (0, 0, 0), (870, 380), (870, 540), 1)
    pygame.draw.line(screen, (0, 0, 0), (770, 280), (770, 340), 1)
    pygame.draw.line(screen, (0, 0, 0), (770, 380), (770, 440), 1)
    pygame.draw.line(screen, (0, 0, 0), (670, 80), (670, 140), 1)
    pygame.draw.line(screen, (0, 0, 0), (670, 180), (670, 240), 1)
    pygame.draw.line(screen, (0, 0, 0), (670, 480), (670, 540), 1)
    pygame.draw.line(screen, (0, 0, 0), (670, 580), (670, 640), 1)
    pygame.font.init()
    myfont = pygame.font.SysFont('Arial', 20)
    textsurface = myfont.render(message, False, (0, 0, 0))
    screen.blit(textsurface, (20, 340))
    for boardCircle in boardCirclesProp:
        circles.append(pygame.draw.circle(screen, boardCircle[1], boardCircle[0], 20, boardCircle[2]))

    pygame.display.flip()


def boardChanged(message):
    for i in range(24):
        if board[i] == "X":
            boardCirclesProp[i][1] = (0, 0, 0)
            boardCirclesProp[i][2] = 1
        elif board[i] == "1":
            boardCirclesProp[i][2] = 0
        elif board[i] == "2":
            boardCirclesProp[i][2] = 0
            boardCirclesProp[i][1] = (255, 0, 0)
    drawboard(message)


background_color = (255, 255, 255)
(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mica (9 Man Morris)')
screen.fill(background_color)
pygame.display.flip()
running = True
message = "Postavi Figuru:"
drawboard(message)

prom = "X"

while running:
    pos = pygame.mouse.get_pos()
    ev = pygame.event.get()

    heuristic_phase1 = position_number_heuristic
    heuristic_phase23 = human_vs_ai_heuristic
    evaluation = evaluator()
    for i in range(9):
        finished = False
        while not finished:
            try:
                position = -1
                while position == -1:
                    ev = pygame.event.get()
                    pos = pygame.mouse.get_pos()
                    for event in ev:
                        if event.type == pygame.MOUSEBUTTONUP:
                            for i in range(len(circles)):
                                if circles[i].collidepoint(pos):
                                    position = i
                        if event.type == pygame.QUIT:
                            quit()
                if board[position] == "X":
                    board[position] = "1"
                    boardChanged("Postavili ste figuru. Protivnik igra.")
                    if player_have_mill(position, board):
                        piecePlaced = False
                        while not piecePlaced:
                            try:
                                position = -1
                                boardChanged("Postavili ste figuru. Ukloni protivnicku figuru.")
                                while position == -1:
                                    ev = pygame.event.get()
                                    pos = pygame.mouse.get_pos()
                                    for event in ev:
                                        if event.type == pygame.MOUSEBUTTONUP:
                                            for i in range(len(circles)):
                                                if circles[i].collidepoint(pos):
                                                    position = i
                                                    boardCirclesProp[i][2] = 0
                                                    drawboard("Pojeli ste protivnika. Protivnik igra")
                                        if event.type == pygame.QUIT:
                                            quit()
                                if board[position] == "2" and not player_have_mill(position, board) or (
                                        player_have_mill(position, board) and concrete_move_number(board, "1") == 3):
                                    board[position] = "X"
                                    boardChanged("Pojeli ste protivnika. Protivnik igra")
                                    piecePlaced = True
                                else:
                                    boardChanged("Ne postoji protivnicka figura na tom mjestu.")
                            except Exception:
                                boardChanged("Doslo je do greske, pokusajte ponovo.")
                    finished = True
                else:
                    boardChanged("Mjesto je zauzeto.")
            except Exception:
                boardChanged("Doslo je do greske, pokusajte ponovo.")
        opponentResponse = minimax(board, depth, False, alfa, beta, True, heuristic_phase1)
        if opponentResponse.evaluator == float('-inf'):
            boardChanged("Izgubili ste!.")
        else:
            board = opponentResponse.board
            boardChanged("Protivnik odigrao. Postavi figuru.")
    finishingPhasesCompleted = False
    while not finishingPhasesCompleted:
        playerHasMoved = False
        while not playerHasMoved:
            try:
                position = -1
                boardChanged("Odaberi figuru koju zelis da pomjeris.")
                while position == -1:
                    ev = pygame.event.get()
                    pos = pygame.mouse.get_pos()
                    for event in ev:
                        if event.type == pygame.MOUSEBUTTONUP:
                            for i in range(len(circles)):
                                if circles[i].collidepoint(pos):
                                    position = i
                        if event.type == pygame.QUIT:
                            quit()
                while board[position] != '1':
                    position = -1
                    boardChanged("Odaberi figuru koju zelis da pomjeris.")
                    while position == -1:
                        ev = pygame.event.get()
                        pos = pygame.mouse.get_pos()
                        for event in ev:
                            if event.type == pygame.MOUSEBUTTONUP:
                                for i in range(len(circles)):
                                    if circles[i].collidepoint(pos):
                                        position = i
                            if event.type == pygame.QUIT:
                                quit()
                playerHasNewPosition = False
                while not playerHasNewPosition:
                    new_positon = -1
                    boardChanged("Odaberi gdje zelis da pomjeris tu figuru.")
                    while new_positon == -1:
                        ev = pygame.event.get()
                        pos = pygame.mouse.get_pos()
                        for event in ev:
                            if event.type == pygame.MOUSEBUTTONUP:
                                for i in range(len(circles)):
                                    if circles[i].collidepoint(pos):
                                        new_positon = i
                            if event.type == pygame.QUIT:
                                quit()
                    if board[new_positon] == "X" and possibleMove(position, new_positon, board):
                        board[position] = 'X'
                        board[new_positon] = '1'
                        boardChanged("Pomjerili ste figuru. Protivnik igra")
                        if player_have_mill(new_positon, board):
                            opponentRemoved = False
                            while not opponentRemoved:
                                try:
                                    position = -1
                                    boardChanged("Pojedi protivnika.")
                                    while position == -1 :
                                        ev = pygame.event.get()
                                        pos = pygame.mouse.get_pos()
                                        for event in ev:
                                            if event.type == pygame.MOUSEBUTTONUP:
                                                for i in range(len(circles)):
                                                    if circles[i].collidepoint(pos):
                                                        position = i
                                            if event.type == pygame.QUIT:
                                                quit()
                                    if board[position] == "2" and not player_have_mill(position, board) or (
                                            player_have_mill(position, board) and concrete_move_number(board, "1") == 3):
                                        board[position] = "X"
                                        boardChanged("Pojeli ste protivnika. Protivnik igra")
                                        opponentRemoved = True
                                    else:
                                        boardChanged("Pozicija ne postoji.")
                                except Exception:
                                    boardChanged("GRESKA!")
                        playerHasNewPosition = True
                        playerHasMoved = True
                    else:
                        boardChanged("Ne možete se pomjeriti na datu poziciju.")
            except Exception:
                boardChanged("Ne možete se pomjeriti na datu poziciju.")
        if heuristicEvaluationPhase23(board) == float('inf'):
            boardChanged("Pobijedili ste!")
        evaluation = minimax(board, depth, False, alfa, beta, False, heuristic_phase23)
        if evaluation.evaluator == float('-inf'):
            boardChanged("Izgubili ste!")
        else:
            board = evaluation.board
            boardChanged("Protivnik odigrao. Vi ste na potezu")
