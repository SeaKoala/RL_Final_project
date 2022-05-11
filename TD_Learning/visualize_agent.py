#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 11:56:43 2022

@author: srinivas
"""

from agent import Agent
from board import Board
from analyze import Analyzer
from argparse import ArgumentParser 


import board_display as b
import pygame
from pygame.locals import *
import sys
import constants_vis as const
import time
import numpy as np

parser = ArgumentParser()
parser.add_argument("-r", help = "Reward type, use 0 for sum and use 1 for empty tile based reward", dest="reward_type", type=int, default=0)
args = parser.parse_args()

def render_2048(next_state):
    
 
    next_state = 2**next_state
    next_state[next_state==1] = 0    
    
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
    
    
    board = b.board_display(rows, cols, next_state, const.PADDING, const.TILE_SIZE,
                    const.BACKGROUND_COLOR, const.BACKGROUND_COLOR_EMPTY_TILE, const.BACKGROUND_TILE_COLORS,
                    const.TILE_COLORS, const.FONT)
    
    screen.fill(black)
    
    '''
    # Main loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    twenty_forty_eight.move(const.LEFT)
                    board.update_board(twenty_forty_eight.get_game_state())
                elif event.key == pygame.K_RIGHT:
                    twenty_forty_eight.move(const.RIGHT)
                    board.update_board(twenty_forty_eight.get_game_state())
                elif event.key == pygame.K_UP:
                    twenty_forty_eight.move(const.UP)
                    board.update_board(twenty_forty_eight.get_game_state())
                elif event.key == pygame.K_DOWN:
                    twenty_forty_eight.move(const.DOWN)
                    board.update_board(twenty_forty_eight.get_game_state())
    '''
    
    board.draw_board()
    board.draw_tiles()
    screen.blit(board.get_board(), (0, 0))
    pygame.display.update()
    pygame.display.flip()
    
    return



class visualize_agent():
	def __init__(self, _train=True, _episode=1000, _milestone=500, _reward_type = 0 ):
		self.TRAIN = _train
		self.EPISODE = _episode
		self.MILESTONE = _milestone
		self.r_type =  _reward_type       

		self.Game = Board(self.r_type)
		self.AI = Agent(0.0025,self.r_type)

		state = self.Game.getBoard()   
		render_2048(state) 
        
		print("Testing mode...")
		totalR = 0
		while True:
			act, r = self.AI.step(self.Game)
			if r != -1:
				totalR += r
			if self.Game.end_game():
				break
			self.Game.GenRandTile(r)
			if self.Game.end_game():
				break
            
			state = self.Game.getBoard()  
            
			render_2048(state) 
            
            
		print("Score: {}".format(totalR))


if __name__ == "__main__":
	trainer = visualize_agent()
