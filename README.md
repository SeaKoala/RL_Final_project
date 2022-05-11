# Monte Carlo Tree Search for 2048 Gym Enviorment
This use of MCTS Algorithm is based on the one from [PatrickKorus](https://github.com/PatrickKorus/mcts-general) which is 
forked from [here](https://github.com/werner-duvaud/muzero-general).

## Dependencies
Python 3.7 is used. Simply run:

```shell script
pip install -r requirements.txt
````

## How to Use
Simply run:
````
python MCTS.py
````

This is likely to win or get very close and will return the runtime in seconds, the max tile reached, and the total score
Increasing the number of simulations will increase preformance at the cost of time

A random policy can be played with:
````
python 2048_random.py
````