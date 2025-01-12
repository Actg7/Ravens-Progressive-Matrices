An AI agent that solves Raven's Progressive Matrices (RPM) IQ problems.

Background:

Raven’s Progressive Matrices, or RPM, is a nonverbal IQ test that relies on abstract reasoning and pattern recognition to predict fluid intelligence.
The test consists of a series of 2x2 and 3x3 grids of cells containing images of black-and-white arrangements of shapes.
All except one cell in the grid contain an image.
The images in the grid are related to each other, which can be observed by noticing patterns and transformations in the position, size, and shape of adjacent images.
The test involves selecting the image in a list of answer choices that best fits the missing cell, based on considering the surrounding patterns and transformations between nearby images.

How the agent solves RPM problems:

The problems are represented as black-and-white image files containing the 2x2 and 3x3 grids of images, along with possible answer choices.
The program first binarizes these image files, converting them into two-dimensional arrays of 0's (for black pixels) and 1's (for white pixels).
This allows the agent to apply NumPy array methods for image operations and pixel-ratio calculations between images to understand the patterns and transformational relationships between the images.
The agent (Agent.py) approaches solving the RPM problems by performing several steps.
First, the agent applies transformations between two adjacent images in a row, column, or diagonal.
These transformations are represented by applying bitwise image operations (e.g. and, or, xor, not) and pixel-ratio methods such as dark pixel ratio (DPR) and intersection pixel ratio (IPR) between nearby images.
Applying these transformations between nearby images results in a new image, which (depending on the applied transformation) carries information about the relationships and patterns in shape, size, and position between the two original images.
Next, the agent uses 
The problems that the agent has been tested on are divided into categories: basic, test, challenge, and Raven's. 
The agent correctly solves (35/48) of the. More detailed breakdowns of the problems and efficiency can be found in the RPM final journal pdf file.
