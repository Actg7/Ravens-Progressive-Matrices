An AI agent that solves Raven's Progressive Matrices (RPM) IQ problems.

Background:

Raven’s Progressive Matrices, or RPM, is a nonverbal IQ test that relies on abstract reasoning and pattern recognition to predict fluid intelligence.
The test consists of a series of 2x2 and 3x3 grids of cells containing images of black-and-white arrangements of shapes.
All except one cell in the grid contain an image.
The images in the grid are related to each other, which can be observed by noticing patterns and transformations in the position, size, and shape of adjacent images.
Given a 2x2 (or 3x3) RPM image, the test involves selecting the image out of 6 (or 8) possible answer choices that best fits the missing cell based on the patterns and relationships between nearby images within the 2x2 (or 3x3) grid.

Example of how a person would solve RPM problems:

![image](https://github.com/user-attachments/assets/c924784f-afc3-44d2-90a1-22e3602510e0)


How the agent solves RPM problems:

The RPM problems are represented as black-and-white image files containing the 2x2 (and 3x3 grids) of images, along with 6 (and 8) possible answer choices.
The program first binarizes the image files, converting them into two-dimensional arrays of 0's (for black pixels) and 1's (for white pixels).
This allows the agent to apply NumPy array methods for image operations and pixel-ratio calculations between images to capture the patterns and relationships between the images.
Once the images are binarized, the agent (Agent.py) solves the RPM problems by performing several key steps.
First, the agent applies comparison methods between two adjacent images in a row, column, or diagonal within the grid.
Let's call these images A and B.
These comparison methods are represented by bitwise image operations (e.g. and, or, xor, not) and pixel-ratio methods such as dark pixel ratio (DPR) and intersection pixel ratio (IPR) that are applied between the two adjacent images.
Applying these comparison methods between nearby images results in either a new image we'll call C (in the case of bitwise operations) or a numerical value (in the case of pixel-ratio methods).
In both cases, the result of applying the comparison method carries information about the relationships and patterns in shape, size, and position between A and B.
Next, the agent iterates through the answer choices, performing the comparison method applied earlier to the answer choice and the image in the cell adjacent to the answer choice.
The agent takes different steps depending on what comparison method was used.
If the agent used pixel-ratio methods, it creates a threshold range centered at the numerical value of the DPR/ipr between A and B.
Next, the agent compares the result of applying the comparison method between the answer choice and the adjacent image in the grid.
The agent considers which answer choices are such that, when we apply the comparison method between it and the adjacent image, the dpr/ipr values fall within the threshold.
The agent then calculates which answer choice has the highest similarity value and returns that as the best predicted answer choice.
If (on the other hand) the agent used bitwise operations, then the agent performs a similar process, comparing each answer choice to the image in the adjacent cell to the answer slot.
Let's call the resulting image of this new comparison (between some the answer choice and the image in the cell adjacent) D.
Ideally, the best answer choice will be such that C and D are similar since that would mean that the patterns between images A and B and between the answer choice and the adjacent image convey similar patterns and transformational relationships (making it the answer choice that most accurately "completes the grid").
The agent uses a method to calculate similarity between the images C and D and records the value.
This is done iterating through every answer choice, after which the highest similarity value is used by the agent to select the corresponding predicted best anser choice image.
For problem sets B, C, and D, the agent uses the pixel-ratio methods, while for problem set E, it uses the bitwise operations.
The reason for this is that in problem set E, many of the RPM problems display symmetry in terms of shapes, with most of the difference between images in the grids being positional or due to rotations.
These patterns and relationships between images are able to be easily captured by bitwise relationships between images due to the symmetry of shapes between the images.

Performance and Future Considerations:

The problems that the agent has been tested on are divided into arrangments (2x2 and 3x3), problem sets (B, C, D, E), and categories (basic, test, challenge, and Raven's).
The problems in set B are all 2x2, while the problems in sets C, D, and E are 3x3.
The agent correctly solves 73% (35/48) of the basic problems, 63% (30/48) of the test problems, 29% (14/48) of the challenge problems, and 63% (30/48) of the Raven's problems.
In total, the agent correctly solves 109 RPM problems in 2.781 seconds.
For comparison, a person would take much longer to achieve that same score, because humans need time to analyze the image and must rely on visuospatial reasoning.
The agent can perform much more quickly and efficiently by applying comparison methods to numerically evaluate pixel similarity and then computing the most similar answer choice.
The approach that the agent uses to solve RPM problems is generalizable to a problem-solving strategy in knowledge-based artificial intelligence known as means-ends-analysis (MEA).
MEA is a problem-solving strategy that involves breaking a goal state into smaller subgoals and completing the subgoals to bring the current state closer to the goal state.
The agent uses MEA to solve RPM problems by breaking the goal of choosing the best answer image into subgoals: first, applying comparison methods between adjacent images in the grid; next, applying the comparison methods between the answer choices and nearby matrices; after this, computing the similarity values between both comparisons; finally, selecting teh answer choice with the strongest similarity value.
This type of approach used by the agent could be generalized in the future to find strategies to compare broader categories of items beyond images with geometric relationships.
More detailed breakdowns of the performance overall and on a few specific problems can be found in the RPM final journal pdf file.
