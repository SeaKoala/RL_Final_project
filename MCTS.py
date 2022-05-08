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

# configure agent
config = MCTSAgentConfig()
config.num_simulations = 200
agent = MCTSAgent(config)

# init game
game = DiscreteGymGame(env = gym.make('2048-v0'))
state = game.reset()
done = False
reward = 0
moves = 0

# run a trajectory
while not done:
    action = agent.step(game, state, reward, done)
    state, reward, done = game.step(action)
    moves += 1
    
    game.render()     # uncomment for environment rendering
    print('Next Action: "{}"\n\nReward: {}'.format(
        gym_2048.Base2048Env.ACTION_STRING[action], reward))
    render_2048(state) 


print('\nTotal Moves: {}'.format(moves))
game.close()