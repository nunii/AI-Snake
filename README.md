# AI-Snake


## proposal
According to Wikipedia, the seeds of modern AI were planted by classical philosophers who attempted to describe the process of human thinking as the mechanical manipulation of symbols.
This work culminated in the invention of the programmable digital computer in the 1940s, a machine based on the abstract essence of mathematical reasoning. This device and the ideas behind it inspired a handful of scientists to begin seriously discussing the possibility of building an electronic brain.
As we find it both exciting and challenging, we decided to take a small step into the world of the AI. We will create an AI agent which will study by itself how to play the famous snake game, hopefully a lot better than the average human being.
We will implement multiple techniques which we will study on our course, starting with the logistic regression algorithm of the supervised learning technique, to predict at each step what a human brain would choose, based on a given data set.  

## Data description
First, we might change the structure of our data sets, but for now that’s how we use it:
The data is being represented as a CSV file for each game we have played. It's a matrix of 66 columns and an unfixed number of rows. 

The first 64 columns (x) consist of the following numbers: \n
0 - represents an empty pixel.
1 - represents a snake body pixel.
2 - represents the pixel of the head.
3 - represents the pixel of the food.

Then there is an empty column, only for making it more comfortable while observing the data.

The last column (y) consists of the following numbers:
2 - pressed down
4 - pressed left
6 - pressed right
8 - pressed up
0 - if we haven't clicked anything.

The rows aren’t a fixed number, because it represents the "moves" you had until you either won or lost, and for each game record it will probably be different. This way each row is an image of the current board state being normalized to a vector.
