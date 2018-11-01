from board import board
from snake import Snake
# import time
import pygame


def drawsnake(snake):
    for i in range(len(snake)):
        pygame.draw.rect(game_board.game_display, board.teal, (snake[i].x, snake[i].y, Snake.factor, Snake.factor))
    pygame.draw.rect(game_board.game_display, board.gold, (snake[i].x, snake[i].y, Snake.factor, Snake.factor - 3))
    pygame.display.update()


# def update_snake(score):
#    i = len(snake) - 1
#
#    while i > 0:
#        snake[i].x = snake[i - 1].x
#        snake[i].y = snake[i - 1].y
#        i -= 1    


########### M A I N ##############
if __name__ == "__main__":
    game_board = board(500, 500)
    snake = [Snake(230, 220), Snake(240, 220), Snake(250, 220)]
    x_change = 0
    y_change = 0
    drawsnake(snake)
    exitGame = False
    while not exitGame:
        for event in pygame.event.get():  # {}
            if event.type == pygame.QUIT:  # if clicked on exit
                exitGame = True

            if event.type == pygame.KEYDOWN:
                first_time = False
                if event.key == pygame.K_LEFT:
                    if x_change is not 10:
                        x_change = -10
                        y_change = 0
                elif event.key == pygame.K_RIGHT:
                    if x_change != -10:
                        x_change = 10
                        y_change = 0
        #               elif event.key == pygame.K_UP:
        #                   if y_change is not 10:
        #                       x_change = 0
        #                       y_change = -10
        #               elif event.key == pygame.K_DOWN:
        #                   if y_change != -10:
        #                       x_change = 0
        #                       y_change = 10
        #               elif event.key == pygame.K_c:
        #                   x_change = 0
        #                   y_change = 0

        #       if not first_time:
        #            update_snake(score)
        #       if score % 10 == 0 and eat:
        #           snake.append(snake_body(snake[len(snake)-1].x, snake[len(snake)-1].y))
        #            print(len(snake))
        #            eat = False

        snake[0].x += x_change
        snake[0].y += y_change
        #            if event.type == pygame.KEYDOWN:
        #                if event.key == pygame.K_LEFT:
        #                    lead_x -= 10
        #                if event.key == pygame.K_RIGHT:
        #                    lead_x += 10
        pygame.display.update()

    # {}
    game_board.close()
