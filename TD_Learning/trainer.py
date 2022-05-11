from agent import Agent
from board import Board
from analyze import Analyzer

class Trainer():
	def __init__(self, _train=True, _episode=1000, _milestone=500, _alpha = 0.0025, _reward_type = 0):
		self.TRAIN = _train
		self.EPISODE = _episode
		self.MILESTONE = _milestone
		self.alpha = _alpha
		self.R_type = _reward_type       


		self.Game = Board(self.R_type)
		self.AI = Agent(self.alpha,self.R_type)
		self.analysis = Analyzer()
		if self.TRAIN == True:
			totalR = 0
			for e in range(self.EPISODE):
				self.Game.initialize()
				self.AI.Episode_begin()
				while True:
					act, r = self.AI.step(self.Game)
					if r != -1:
						totalR += r
					if self.Game.end_game():
						break
					self.Game.GenRandTile(r)
					if self.Game.end_game():
						break
				self.AI.Episode_end()
				self.analysis.eval(self.Game)
				if e % self.MILESTONE == 0:
					print("\n#Episode: {episode}, score: {score}".format(episode = e, score = totalR))	
					totalR = 0
					self.analysis.printAnalysis(self.MILESTONE)
					self.analysis.reset()
					self.AI.save_tupleNet()
			self.AI.save_tupleNet()

		else:
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
			self.Game.printBoard()
			print("Score: {}".format(totalR))


if __name__ == "__main__":
	trainer = Trainer()
