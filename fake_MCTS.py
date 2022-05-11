import gym_2048
import gym


import board as b
import pygame
from pygame.locals import *
import sys
import constants as const
import time
import numpy as np


def MCTS_move(searches_per_move, search_length, actions):

    scores = np.zeros(4)
    for first_index in range(4):
        env = gym.make('2048-v0')
        env.seed(42)
        env.reset()
        action = env.np_random.choice(range(4), 1).item()
        next_state, reward, done, info = env.step(action)
        for i in range(len(actions)):
            action = actions[i]
            next_state, reward, done, info = env.step(action)

        first_state, reward, done, info = env.step(first_index)
        scores[first_index] += reward
        move_number =1
        while not done and move_number < search_length:
            action = np.random.choice(range(4), 1)
            search_board, reward, done, info = env.step(action)
            scores[first_index] += reward
            move_number +=1
            if (done):
                scores[first_index] = -1000
        env.close()
                

    best_move_index = np.argmax(scores)
    return best_move_index

def fake_move(actions):

    scores = np.zeros(4)
    for first_index in range(4):
        env = gym.make('2048-v0')
        env.seed(42)
        env.reset()
        for i in range(len(actions)):
            action = actions[i]
            next_state, reward, done, info = env.step(action)

        first_state, reward, done, info = env.step(first_index)
        scores[first_index] += reward   

    best_move_index = np.argmax(scores)
    return best_move_index

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
    num_games = 2
    maxTiles = np.zeros((num_games))
    game_len = np.zeros((num_games))
    fs = np.zeros((num_games))


    for n in range(num_games):
        actions = []
        env = gym.make('2048-v0')
        # env.seed(42)

        state = env.reset()
        start_time = time.time()
        # env.render()

        done = False
        moves = 0
        while not done:
          action =  action = np.random.choice(range(4), 1)
          # actions.append(action)
          next_state, reward, done, info = env.step(action)
          moves += 1
          fs[n] += reward

          # print('Next Action: "{}"\n\nReward: {}'.format(
          #   gym_2048.Base2048Env.ACTION_STRING[action], reward))
          # env.render()
          render_2048(next_state) 
        game_len[n] = moves
        maxTiles[n] = np.max(next_state)

              # print('game: {}'.format(n))
        env.close()
    print("--- %s seconds ---" % (time.time() - start_time))
              # print("--- %s seconds ---" % (time.time() - start_time))
    # print('Roll outs: {}'.format(RO[d]))
    for n in range(num_games):
        print(game_len[n])

    print('\n')
    for n in range(num_games):
        print(maxTiles[n])

    print('\n')
    for n in range(num_games):
        print(fs[n])




    # print('\nTotal Moves: {}'.format(moves))






