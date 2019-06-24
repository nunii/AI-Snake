# AI-Snake

Authors:  Amit Nuni (nunii) Bar Janach (BarJan) Merav Boim (meravboim)

As a part of DeepLearning & Natural language processing course we chose to create a snake game using pygame, and implement different methods of DL & ML to create an AI which can learn how to play by itself. We weren't allowed to use external libraries like sklearn and keras, we could've used TensorFlow only.
The models: Simple SoftMax logistic regression MLP with hidden layers Reinforcement learning (RL)

## Data description
First, we might change the structure of our data sets, but for now that’s how we use it:
The data is being represented as a CSV file for each game we have played. It's a matrix of 66 columns and an unfixed number of rows. 

The first 64 columns (x) consist of the following numbers: 
- 0 - represents an empty pixel.
- 1 - represents a snake body pixel.
- 2 - represents the pixel of the head.
- 3 - represents the pixel of the food.

Then there is an empty column, only for making it more comfortable while observing the data.

The last column (y) consists of the following numbers:
- 2 - pressed down
- 4 - pressed left
- 6 - pressed right
- 8 - pressed up
- 0 - if we haven't clicked anything.

The rows aren’t a fixed number, because it represents the "moves" you had until you either won or lost, and for each game record it will probably be different. This way each row is an image of the current board state being normalized to a vector.
