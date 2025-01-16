**A knowledge-based AI agent that solves Raven's Progressive Matrices (RPM) IQ problems using human-like reasoning in a fraction of the time.**

**Background:**

Raven’s Progressive Matrices, or RPM, is a nonverbal IQ test that relies on abstract reasoning and pattern recognition to predict fluid intelligence.
The test consists of a series of 2x2 and 3x3 grids of cells containing images of black-and-white arrangements of shapes.
All except one cell in the grid contain an image.
The images in the grid are related to each other, which can be observed by noticing patterns and transformations in the position, size, and shape of adjacent images.
Given a 2x2 (or 3x3) RPM image, the test involves selecting the image out of 6 (or 8) possible answer choices that best fits the missing cell based on the patterns and relationships between nearby images within the 2x2 (or 3x3) grid.

**How a person would solve RPM problems:**

![image](https://github.com/user-attachments/assets/c924784f-afc3-44d2-90a1-22e3602510e0)

This is an example of a 2x2 RPM problem, with 6 answer choices.
We can see that all except one cell in the grid contain an image.
The problem involves determining which of the 6 answer choice images most appropriately fits into the empty cell based on analyzing the patterns and relationships between the surrounding images.
The images possess certain patterns and relationships between each other in terms of location, position, shape, size, and color.
When someone looks at this problem, they may notice that across the top row, both images (A and B) contain the same number of shapes (1 shape), the same type of shape (an octagon), the same orientation (no rotation/translation), the same size of shape, and the same relative positioning of shape within the image (positioned within the center of the image).
The noticeable difference between both images in the top row is that the color changes, from white on the left image to black on the right image.
Next, the person may notice that along the leftmost column, both images (C and D) possess the same number of shapes (1 shape), the same orientation (no rotation/translation), the same size of shape, the same relative positioning of shape within the image (positioned within the center of the image), and the same shape color (white for both images).
The noticeable difference between both images in the top row is that the shape type changes, from an octagon on the top image to a square on the bottom image.
Combining these observations, a person may reasonably predict that the answer image cell should exhibit these patterns of relationships by noticing that going vertically from image B to the answer cell, the shape should change from an octagon to a square.
They might then notice that going horizontally from image C to the answer cell, the shape color should change from white to black.
The person might conclude that the answer choice image that best fits the problem should be a black square of the same size, orientation, and position as the rest of the shapes in the other images (A, B, and C).
Thus, a person would likely select answer choice 5 as the best answer to the problem (which, in this case, is the right answer).
On a high level, this is a similar method to how the agent solves 2x2 problems (for example, in problem set B).
We can see that people rely on visuospatial reasoning and abstract understanding of the relationships encoded by the recognizable patterns and differences/similarities between images along a row or column.
Meanwhile, the agent analyzes relationships between images on the scale of individual pixels and makes use of algorithms to estimate and calculate the best approximation based on these relationships and symmetries of pixels between images in the problem grid.
In other words, the agent uses AI reasoning to solve problems with human-like intelligence and capability in a fraction of the time.
Let's dive into how the agent uses knowledge-based AI techniques to solve RPM problems!

**How the agent solves RPM problems:**

The RPM problems are represented as black-and-white image files containing the 2x2 (and 3x3 grids) of images, along with 6 (and 8) possible answer choices.
The program first binarizes the image files, converting them into two-dimensional arrays of 0's (for black pixels) and 1's (for white pixels).
This allows the agent to apply NumPy array methods for image operations and pixel-ratio calculations between images to capture the patterns and relationships between the images.
Once the images are binarized, the agent (Agent.py) solves the RPM problems by performing several key steps.
First, the agent applies comparison methods between two adjacent images in a row, column, or diagonal within the grid.
Let's call these images A and B.
These comparison methods are represented by bitwise image operations (e.g. and, or, xor, not) and pixel-ratio methods such as dark pixel ratio (DPR) and intersection pixel ratio (IPR) that are applied between the two adjacent images.
Applying these comparison methods between nearby images results in either a new image we'll call X (in the case of bitwise operations) or a numerical value (in the case of pixel-ratio methods).
In both cases, the result of applying the comparison method carries information about the relationships and patterns in shape, size, and position between A and B.
Next, the agent iterates through the answer choices, performing the comparison method applied earlier to the answer choice and the image in the cell adjacent to the answer choice.
The agent takes different steps depending on what comparison method was used.
If the agent used pixel-ratio methods, it creates a threshold range centered at the numerical value of the DPR/IPR between A and B.
Next, the agent compares the result of applying the comparison method between the answer choice and the adjacent image in the grid.
The agent considers which answer choices are such that when we apply the comparison method between it and the adjacent image, the DPR/IPR values fall within the threshold.
The agent then calculates which answer choice has the highest similarity value and returns that as the best-predicted answer choice.
If (on the other hand) the agent used bitwise operations, then the agent performs a similar process, comparing each answer choice to the image in the adjacent cell to the answer slot.
Let's call the resulting image of this new comparison (between some given answer choices and the image in the cell adjacent) Y.
Ideally, the best answer choice will be such that X and Y are similar since that would mean that the patterns between images A and B and between the answer choice and the adjacent image convey similar patterns and transformational relationships (making it the answer choice that most accurately "completes the grid").
The agent uses a method to calculate the similarity between the images X and Y and records the value.
This is done by iterating through every answer choice, after which the highest similarity value is used by the agent to select the corresponding predicted best answer choice image.
For problem sets B, C, and D, the agent uses the pixel-ratio methods, while for problem set E, it uses the bitwise operations.
The reason for this is that in problem set E, many of the RPM problems display symmetry in terms of shapes, with most of the difference between images in the grids being positional or due to rotations.
These patterns and relationships between images are able to be easily captured by bitwise relationships between images due to the symmetry of shapes between the images.

**Performance and Future Applications:**

The problems that the agent has been tested on are divided into arrangments (2x2 and 3x3), problem sets (B, C, D, E), and categories (basic, test, challenge, and Raven's).
The problems in set B are all 2x2, while the ones in sets C, D, and E are 3x3.
The agent correctly solves 73% (35/48) of the basic problems, 63% (30/48) of the test problems, 29% (14/48) of the challenge problems, and 63% (30/48) of the Raven's problems.
In total, the agent correctly solves 109 RPM problems in 2.781 seconds.
For comparison, if it takes around 10 seconds for a person to correctly solve one RPM problem, it would take them almost 20 minutes to achieve the same results.
To put it a little more precisely, if it takes a person ~10 seconds to solve a problem, multiplying this by 109 problems results in 1090 total seconds.
Comparing this to 2.718 (or ~3 seconds) for the agent's performance, we can see that the agent solves RPM problems on average 363x faster than a person!
This is because humans need considerably more time to analyze the image and apply visuospatial reasoning to pick the right answer.
The agent can perform much more quickly and efficiently by applying comparison methods to evaluate pixel similarity numerically and then computing the most similar answer choice.
The approach that the agent uses to solve RPM problems is generalizable to a problem-solving strategy in knowledge-based artificial intelligence known as means-ends-analysis (MEA).
MEA is a problem-solving strategy that involves breaking a goal state into smaller subgoals and completing the subgoals to bring the current state closer to the goal state.
The agent uses MEA to solve RPM problems by breaking the goal of choosing the best answer image into subgoals: first, applying comparison methods between adjacent images in the grid; next, applying the comparison methods between the answer choices and nearby matrices; after this, computing the similarity values between both comparisons; finally, selecting the answer choice with the strongest similarity value.
This type of approach used by the agent could be generalized to find strategies to compare broader categories of items beyond images with geometric relationships.
In the future, agents could use MEA approaches to achieve human-like reasoning on more broad classes of problems, solving problems in a fraction of the time it would take a human.
More detailed breakdowns of the performance overall and on a few specific problems can be found in the RPM final journal pdf file.
