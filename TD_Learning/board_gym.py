import numpy as np
import random
import copy
import gym_2048
import gym

class Board():

	def __init__(self):
        	self.env = gym.make('2048-v0') 
        	self.env.seed(42) # = gym.make('2048-v0') 
        	self.initialize()

	def initialize(self):
		self.env.reset() 
		self.state, r, self.done = self.env.reset(), 0., False 
#		self.env.render() 
#		print(self.state)           
		self.tile = self.state_tile(self.state)  
#		self.env.render() 
        
	def state_tile(self,state):
        
        	state_board = state.copy()
        	state_board[state_board == 0] = 1
        	tile = np.uint32(np.log2(state_board))
        	return tile 
    

	def copyBoard(self, tmp):
		self.tile = tmp.getBoard().copy()	
        
	def GenRandTile(self, prev_reward):
		if prev_reward == -1:
			return

		self.tile = self.tile

	def move(self, action):
		if self.done == 1:
			return -1
		#re-map action
		if action == 0:
			action = 1
		elif action == 1:
			action = 2
		elif action == 2:
			action = 3
		else:
			action = 0

  
        
#		print(action)
#		self.env.render()          
		next_state, reward, self.done, info = self.env.step(action) 
#		self.env.render()      
#		print(self.done)
		self.state =  next_state
#		print(next_state)     
		self.tile =  self.state_tile(self.state)       
		return reward

	def transpose(self):
		self.tile = self.tile.transpose()

	def reflect_horizontal(self):
		self.tile = np.fliplr(self.tile)
	
	def reflect_vertical(self):
		self.tile = np.flipud(self.tile)

	def rotate_right(self):
		self.tile = np.rot90(self.tile, 1, (1, 0))
	
	def rotate_left(self):
		self.tile = np.rot90(self.tile)

	def reverse(self):
		self.reflect_horizontal()
		self.reflect_vertical()

	def morphBoard(self, i):
		#if i == 0: keep the same board
		if i == 1:
			self.reflect_horizontal()
		elif i == 2:
			self.reflect_vertical()
		elif i == 3:
			self.reflect_horizontal()
			self.reflect_vertical()
		elif i == 4:
			self.rotate_right()
		elif i == 5:
			self.rotate_right()
			self.reflect_horizontal()
		elif i == 6:
			self.rotate_right()
			self.reflect_vertical()
		elif i == 7:
			self.rotate_right()
			self.reflect_horizontal()
			self.reflect_vertical()		


	def end_game(self):
		tmp = Board()
		tmp.copyBoard(self)
		if tmp.move(0) == -1 and tmp.move(0) == tmp.move(1) and tmp.move(1) == tmp.move(2) and tmp.move(2) == tmp.move(3):
			return True
		else:
			return False

	def getBoard(self):
		return self.tile
	
	def getTile(self, pos):
		return self.tile[pos // 4][pos % 4]

	def printBoard(self):
		print(self.tile)



if __name__ == "__main__":
	b = Board()
	b.initialize()
#	b.env.render()
    
	r = 0
    
	while True:
		op = input()
		if op == 'w':
			op = 0
		elif op == 'd':
			op = 1
		elif op == 's':
			op = 2
		elif op == 'a':
			op = 3
		r += b.move(op)
		if b.end_game():
			break
		b.GenRandTile(r)
		b.printBoard()
		print("Score: {}\n".format(r))
		if b.end_game():
			break

