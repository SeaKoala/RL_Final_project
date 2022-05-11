import gym
import gym_2048
from mcts_general.agent import MCTSAgent
from mcts_general.config import MCTSAgentConfig
from mcts_general.game import DiscreteGymGame

import board as b
import pygame
from pygame.locals import *
import sys
import constants as const
import time
import numpy as np
import time

def render_2048(next_state): # Friendly UI
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



# Run MCTS with various parameters
# RO = [1,2,4,8,16,32,64,128,256,512,1024,2048]
RO = [1] # Fixed parameters
for d in range(len(RO)):
    # configure agent
    config = MCTSAgentConfig()
    config.num_simulations = 128
    config.number_of_roll_outs = 5  # default =5
    config.do_roll_outs = False
    config.max_roll_out_depth = 20 # default = 20
    agent = MCTSAgent(config)

    num_games = 1 
    maxTiles = np.zeros((num_games))
    game_len = np.zeros((num_games))
    fs = np.zeros((num_games)) # final game score

    for n in range(num_games):
    # init game
        game = DiscreteGymGame(env = gym.make('2048-v0'))
        state = game.reset()
        done = False
        reward = 0
        moves = 0
        render_2048(state) # renders friendly UI
        # run a trajectory
        start_time = time.time()
        while not done:
            action = agent.step(game, state, reward, done)  # Use MCTS to get best action
            state, reward, done = game.step(action)
            fs[n] += reward
            # reward = 16- np.count_nonzero(state) # empty tile reward
            moves += 1
            render_2048(state) 

        game_len[n] = moves
        maxTiles[n] = np.max(state)

        # print('game: {}'.format(n))
        game.close()
        print(time.time() - start_time)
    # print('Roll Outs: {}'.format(RO[d]))
    for n in range(num_games):
        print(maxTiles[n])
    print('\n')
    for n in range(num_games):
        print(fs[n])   
    print('\n') 