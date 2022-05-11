# Monte Carlo Tree Search for 2048 Gym Enviorment

## Dependencies
Python 3.7 is used. Simply run:

```shell script
pip install -r requirements.txt
````

## How to run MCTS
Navigate to MCTS directory
Run:
````
python MCTS.py
````

This is likely to win or get very close and will return the runtime in seconds, the max tile reached, and the total score
Increasing the number of simulations will increase preformance at the cost of time

A random policy can be played with:
````
python 2048_random.py
````

# Model free TD(0) Learning for the game of 2048
	
* To train the RL agent (the tuple network will be saved to the directory tupleNet/)		
>	`python3 2048.py --play=n --train=on -e=5000 -a=0.0025 -r=0        

 # e is number of episodes to train which is 5000, 
 # -a is step size parameter alpha, 
 # r = 0 means sum based reward and r = 1 means empty cell based reward	
	
* To test the RL agent after training	
>	`python3 visualize_agent.py -r=0		
# r = 0 means sum based reward and r = 1 means empty cell based reward		
	
	

References:

This use of MCTS Algorithm is based on the one from [PatrickKorus](https://github.com/PatrickKorus/mcts-general) which is 
forked from [here](https://github.com/werner-duvaud/muzero-general).

This RL agent code for TD(0) is taken from below user and modified to achieve results of our experiment

SizzleHSU, https://github.com/sizzle0121/2048-Game-and-AI/

The code for rendering the game is taken from below user and modified to work with our code

Juan Gallostra Acín, https://github.com/juangallostra/2048