import gym_2048
import gym


import board as b
import pygame
from pygame.locals import *
import sys
import constants as const
import time
import numpy as np

def render_2048(next_state):
    
    time.sleep(0.1)
    next_state = next_state.tolist()
    
    rows = 4
    cols = 4
    black = 0, 0, 0
    
    
    pygame.init()
    pygame.display.set_caption("2048")
    
    SIZE = width, height = cols * const.TILE_SIZE + (cols + 1) * const.PADDING,\
                           rows * const.TILE_SIZE + (rows + 1) * const.PADDING
    screen = pygame.display.set_mode(SIZE)
    
    
    board = b.Board(rows, cols, next_state, const.PADDING, const.TILE_SIZE,
                    const.BACKGROUND_COLOR, const.BACKGROUND_COLOR_EMPTY_TILE, const.BACKGROUND_TILE_COLORS,
                    const.TILE_COLORS, const.FONT)
    
    screen.fill(black)
    board.draw_board()
    board.draw_tiles()
    screen.blit(board.get_board(), (0, 0))
    pygame.display.update()
    pygame.display.flip()
    return

if __name__ == '__main__':
    num_games = 1
    maxTiles = np.zeros((num_games))
    game_len = np.zeros((num_games))
    fs = np.zeros((num_games))


    for n in range(num_games):
        # init enviorment
        env = gym.make('2048-v0')
        state = env.reset()
        start_time = time.time()

        done = False
        moves = 0
        while not done:
          action =  action = np.random.choice(range(4), 1) # take random action
          next_state, reward, done, info = env.step(action)
          moves += 1
          fs[n] += reward
          render_2048(next_state) 
        game_len[n] = moves
        maxTiles[n] = np.max(next_state)
        env.close()

    print("--- %s seconds ---" % (time.time() - start_time))

    for n in range(num_games):
        print(game_len[n])

    print('\n')
    for n in range(num_games):
        print(maxTiles[n])

    print('\n')
    for n in range(num_games):
        print(fs[n])




    # print('\nTotal Moves: {}'.format(moves))






