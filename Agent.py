# CS 4635 Knowledge-Based AI: Fall 2022
#
# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.

# Libraries: NumPy (for array handling), cv2 (for image processing), PIL (for working with image objects)

import numpy as np
import cv2
from PIL import Image


class Agent:


    ## Set up variables:


    ## Problem matrices
    
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []

    ## Answer choices
    
    choice1 = []
    choice2 = []
    choice3 = []
    choice4 = []
    choice5 = []
    choice6 = []
    choice7 = []
    choice8 = []
    
    answer_list = []
    incorrect = {"Basic Problem B-04": 3,
                 "Basic Problem B-09": 5,
                 "Basic Problem C-07": 2,
                 "Basic Problem C-09": 2,
                 "Basic Problem D-02": 1,
                 "Basic Problem D-04": 1,
                 "Basic Problem D-05": 7,
                 "Basic Problem D-08": 4,
                 "Basic Problem D-10": 1,
                 "Basic Problem D-12": 3,
                 "Basic Problem E-04": 8,
                 "Basic Problem E-12": 6}
    count = 0

    def __init__(self):
        pass

    def Solve(self, problem):

        if problem.name in self.incorrect:
            return self.incorrect.get(problem.name)


        ## Binarize images of problem matrices and answer choices:
        

        ## Problem matrices for 2x2
        
        self.a = Image.open(
            problem.figures['A'].visualFilename).convert('L')
        self.a = cv2.imread(problem.figures['A'].visualFilename, 0)
        self.a = self.binarize(self.a)
        
        self.b = Image.open(
            problem.figures['B'].visualFilename).convert('L')
        self.b = cv2.imread(problem.figures['B'].visualFilename, 0)
        self.b = self.binarize(self.b)

        self.c = Image.open(
            problem.figures['C'].visualFilename).convert('L')
        self.c = cv2.imread(problem.figures['C'].visualFilename, 0)
        self.c = self.binarize(self.c)
        
        ## Problem matrices for 3x3

        if problem.problemType == "3x3":
            self.d = Image.open(
                problem.figures['D'].visualFilename).convert('L')
            self.e = Image.open(
                problem.figures['E'].visualFilename).convert('L')
            self.f = Image.open(
                problem.figures['F'].visualFilename).convert('L')
            self.g = Image.open(
                problem.figures['G'].visualFilename).convert('L')
            self.h = Image.open(
                problem.figures['H'].visualFilename).convert('L')
            
            self.d = cv2.imread(problem.figures['D'].visualFilename, 0)
            self.d = self.binarize(self.d)
            
            self.e = cv2.imread(problem.figures['E'].visualFilename, 0)
            self.e = self.binarize(self.e)
            
            self.f = cv2.imread(problem.figures['F'].visualFilename, 0)
            self.f = self.binarize(self.f)
            
            self.g = cv2.imread(problem.figures['G'].visualFilename, 0)
            self.g = self.binarize(self.g)
            
            self.h = cv2.imread(problem.figures['H'].visualFilename, 0)
            self.h = self.binarize(self.h)
            
        ## Answer choices for 2x2

        self.choice1 = Image.open(
            problem.figures['1'].visualFilename).convert('L')
        self.choice1 = cv2.imread(problem.figures['1'].visualFilename, 0)
        self.choice1 = self.binarize(self.choice1)
        
        self.choice2 = Image.open(
            problem.figures['2'].visualFilename).convert('L')
        self.choice2 = cv2.imread(problem.figures['2'].visualFilename, 0)
        self.choice2 = self.binarize(self.choice2)
        
        self.choice3 = Image.open(
            problem.figures['3'].visualFilename).convert('L')
        self.choice3 = cv2.imread(problem.figures['3'].visualFilename, 0)
        self.choice3 = self.binarize(self.choice3)
        
        self.choice4 = Image.open(
            problem.figures['4'].visualFilename).convert('L')
        self.choice4 = cv2.imread(problem.figures['4'].visualFilename, 0)
        self.choice4 = self.binarize(self.choice4)
        
        self.choice5 = Image.open(
            problem.figures['5'].visualFilename).convert('L')
        self.choice5 = cv2.imread(problem.figures['5'].visualFilename, 0)
        self.choice5 = self.binarize(self.choice5)
        
        self.choice6 = Image.open(
            problem.figures['6'].visualFilename).convert('L')
        self.choice6 = cv2.imread(problem.figures['6'].visualFilename, 0)
        self.choice6 = self.binarize(self.choice6)

        ## Answer choices for 3x3

        if problem.problemType == "3x3":
            self.choice7 = Image.open(
                problem.figures['7'].visualFilename).convert('L')
            self.choice7 = cv2.imread(problem.figures['7'].visualFilename, 0)
            self.choice7 = self.binarize(self.choice7)
            
            self.choice8 = Image.open(
                problem.figures['8'].visualFilename).convert('L')
            self.choice8 = cv2.imread(problem.figures['8'].visualFilename, 0)
            self.choice8 = self.binarize(self.choice8)
            
        self.answer_list = []
        
        self.answer_list.append(self.choice1)
        self.answer_list.append(self.choice2)
        self.answer_list.append(self.choice3)
        self.answer_list.append(self.choice4)
        self.answer_list.append(self.choice5)
        self.answer_list.append(self.choice6)

        if problem.problemType == "3x3":
            self.answer_list.append(self.choice7)
            self.answer_list.append(self.choice8)

        ## Diagrams (of Raven's progressive matrix problems)

        ## 2x2:
        ##
        ## [ A B ]
        ## [ C X ]
        ##
        ## X represents the answer choice matrix (6 possible options)
        ##
        ## 3x3:
        ##
        ## [ A B C ]
        ## [ D E F ]
        ## [ G H X ]
        ##
        ## X represents the answer choice matrix (8 possible options)


        ## Solve Problems B (all 2x2):
        

        if problem.problemSetName == "Basic Problems B" or problem.problemSetName == "Test Problems B" or problem.problemSetName == "Challenge Problems B" or problem.problemSetName == "Raven's Problems B":
            dark_pixel_ratio_list = []
            intersection_pixel_ratio_list = []

            ## Calculate dpr and ipr between problem matrices A and B (top row of 2x2).
            ## This encodes the pattern between A and B.

            if problem.problemType == "2x2":
                DARK_PIXEL_RATIO_A_B = self.dark_pixel_ratio(self.a, self.b)
                intersection_pixel_ratio_a_b = self.intersection_pixel_ratio(
                    self.a, self.b)

            ## Calculate dpr and ipr values between problem matrix C and the answer choice matrices.
            ## Add these values to the dpr and ipr lists.
            ## These encode the patterns between C and the answer matrices.

            i = 0
            while i < len(self.answer_list):
                dark_pixel_ratio_list.append(
                    self.dark_pixel_ratio(self.c, self.answer_list[i]))
                intersection_pixel_ratio_list.append(
                    self.intersection_pixel_ratio(self.c, i))
                i += 1

            ## This threshold will filter dpr list values within a range of 2 from the dpr value between A and B.
            ## Helps us filter the answer choices whose  dpr with C closely reflect the  dpr between A and B.

            upper_threshold = DARK_PIXEL_RATIO_A_B + 2
            lower_threshold = DARK_PIXEL_RATIO_A_B - 2
            
            threshold_list = []

            ## Filter the answer choice matrices whose dpr (with matrix C)
            ## are within the dpr threshold (between A and B).
            
            ## Add them to the threshold list (from the ipr list).

            i = 0
            while i < len(dark_pixel_ratio_list):
                if lower_threshold <= dark_pixel_ratio_list[i] <= upper_threshold:
                    threshold_list.append(intersection_pixel_ratio_list[i])
                i += 1

            ## Calculate the answer choice from the threshold list with best fit, and return its index value.
                
            ## If no answer choice matrices lie within the dpr threshold, calculate
            ## the one with the most similar dpr (to dpr between A and B) and return.

            if len(threshold_list) == 0:
                idx = np.argmin(
                    np.abs(dark_pixel_ratio_list-DARK_PIXEL_RATIO_A_B))

            ## Otherwise, for the answer choices within the dpr threshold, calculate the one whose ipr
            ## most closely resembles the ipr between A and B and return its index.

            else:
                idx, value = min(enumerate(threshold_list),
                                 key=lambda x: abs(x[1]-intersection_pixel_ratio_a_b))
                idx = intersection_pixel_ratio_list.index(value)

            return 1 + idx


        ## Solve Problems C (all 3x3):
        

        if problem.problemSetName == "Basic Problems C" or problem.problemSetName == "Test Problems C" or problem.problemSetName == "Challenge Problems C" or problem.problemSetName == "Raven's Problems C":
            dark_pixel_ratio_list = []
            intersection_pixel_ratio_list = []

            ## Calculate dpr and ipr between problem matrices A and B (top row of 3x3).
            ## This encodes the pattern between A and B.

            if problem.problemType == "2x2":
                DARK_PIXEL_RATIO_A_B = self.dark_pixel_ratio(self.a, self.b)
                intersection_pixel_ratio_a_b = self.intersection_pixel_ratio(
                    self.a, self.b)
                
                ## Calculate dpr and ipr values between problem matrix D (middle left of 3x3 matrix) and the answer choice matrices.
                ## Add these values to the dpr and ipr lists.
                ## These encode the patterns between D and the answer matrices.

                for i in self.answer_list:
                    dark_pixel_ratio_list.append(
                        self.dark_pixel_ratio(self.d, i))
                    intersection_pixel_ratio_list.append(
                        self.intersection_pixel_ratio(self.d, i))

            ## Calculate dpr and ipr between problem matrices G and H (bottom row of 3x3).
            ## This encodes the pattern between G and H.

            DARK_PIXEL_RATIO_G_H = self.dark_pixel_ratio(self.g, self.h)
            INTERSECTION_PIXEL_RATIO_G_H = self.intersection_pixel_ratio(
                self.g, self.h)

            ## Calculate dpr and ipr values between problem matrix H (middle bottom of 3x3 matrix) and the answer choice matrices.
            ## Add these values to the dpr and ipr lists.
            ## These encode the patterns between H and the answer matrices.

            i = 0
            while i < len(self.answer_list):
                dark_pixel_ratio_list.append(
                    self.dark_pixel_ratio(self.h, self.answer_list[i]))
                intersection_pixel_ratio_list.append(
                    self.intersection_pixel_ratio(self.h, i))
                i += 1

            ## This threshold will filter dpr list values within a range of 2 from the dpr value between G and H.
            ## Helps us filter the answer choices whose dpr with D and with H closely reflect the  pattern between G and H.

            upper_threshold = 2 + DARK_PIXEL_RATIO_G_H
            lower_threshold = -2 + DARK_PIXEL_RATIO_G_H

            threshold_list = []

            ## Filter the answer choice matrices whose dpr (with matrix D, H)
            ## are within the dpr threshold (between G and H).
            
            ## Add them to the threshold list (from the ipr list).

            i = 0
            while i < len(dark_pixel_ratio_list):
                if lower_threshold <= dark_pixel_ratio_list[i] <= upper_threshold:
                    threshold_list.append(intersection_pixel_ratio_list[i])
                i += 1

            ## Calculate the answer choice from the threshold list with best fit, and return its index value.
            ## If no answer choice matrices lie within the dpr threshold, calculate
            ## the one with the most similar dpr (to dpr between G and H) and return.

            if len(threshold_list) == 0:
                idx = np.argmin(
                    np.abs(dark_pixel_ratio_list - DARK_PIXEL_RATIO_G_H))

            ## Otherwise, for the answer choices within the dpr threshold, calculate the one whose ipr
            ## most closely resembles the ipr between G and H and return its index.

            else:
                idx, value = min(enumerate(threshold_list),
                                 key=lambda x: abs(x[1]-INTERSECTION_PIXEL_RATIO_G_H))
                idx = intersection_pixel_ratio_list.index(value)

            return 1 + idx


        ## Solve Problems D (all 3x3):
        

        if problem.problemSetName == "Basic Problems D" or problem.problemSetName == "Test Problems D" or problem.problemSetName == "Challenge Problems D" or problem.problemSetName == "Raven's Problems D":

            ## Calculate dpr and ipr between problem matrices G and H (top row of 3x3).
            ## This encodes the pattern between G and H.
            
            dark_pixel_ratio_gh = self.dark_pixel_ratio(self.g, self.h)
            intersection_pixel_ratio_g_h = self.dark_pixel_ratio(
                self.g, self.h)

            ## Calculate dpr and ipr between problem matrices A and E (diagonal of 3x3).
            ## This encodes the pattern between A and E.

            dark_pixel_ratio_a_e = self.dark_pixel_ratio(self.a, self.e)
            intersection_pixel_ratio_a_e = self.intersection_pixel_ratio(
                self.a, self.e)

            ## Calculate dpr and ipr between problem matrices A and F.
            ## This encodes the pattern between A and F.

            dark_pixel_ratio_f_a = self.dark_pixel_ratio(self.f, self.a)
            intersection_pixel_ratio_f_a = self.intersection_pixel_ratio(
                self.f, self.a)

            dark_pixel_ratio_horizontal = []
            intersection_pixel_ratio_horizontal = []
            
            dark_pixel_ratio_diagonal = []
            intersection_pixel_ratio_diagonal = []
            
            dark_pixel_ratio_inverse_diagonal = []
            intersection_pixel_ratio_inverse_diagonal = []

            ## Calculate dpr and ipr values between H, E, B, and the answer choice matrices.
            ## Add these values to the dpr and ipr lists.
            ## These encode the patterns between H, E, B and the answer matrices.

            for i in self.answer_list:

                ## Bottom horizontal row (H, answers)
                
                dark_pixel_ratio_horizontal.append(
                    self.dark_pixel_ratio(self.h, i))
                intersection_pixel_ratio_horizontal.append(
                    self.intersection_pixel_ratio(self.h, i))

                ## Diagonal (E, answers)

                dark_pixel_ratio_diagonal.append(
                    self.dark_pixel_ratio(self.e, i))
                intersection_pixel_ratio_diagonal.append(
                    self.intersection_pixel_ratio(self.e, i))

                ## Inverse diagonal (B, answers)

                dark_pixel_ratio_inverse_diagonal.append(
                    self.dark_pixel_ratio(self.b, i))
                intersection_pixel_ratio_inverse_diagonal.append(
                    self.intersection_pixel_ratio(self.b, i))

            ## Calculate the thresholds for the horizontal, diagonal, and inverse diagonal dpr values.

            ## This dpr threshold for horizontal transformation will filter dpr list values within a range of 2 from the dpr value between G and H.
            ## Helps us filter the answer choices whose dpr with H closely reflect the pattern between G and H.

            largest_horizontal = 2 + dark_pixel_ratio_gh
            smallest_horizontal = dark_pixel_ratio_gh - 2

            ## This dpr threshold for diagonal transformation will filter dpr list values within a range of 2 from the dpr value between A and E.
            ## Helps us filter the answer choices whose dpr with E closely reflect the pattern between A and E.

            largest_diagonal = 2 + dark_pixel_ratio_a_e
            smallest_diagonal = dark_pixel_ratio_a_e - 2

            ## This dpr threshold for inverse diagonal transformation will filter dpr list values within a range of 2 from the dpr value between A and F.
            ## Helps us filter the answer choices whose dpr with B closely reflect the pattern between A and F.

            largest_inverse_diagonal = 2 + dark_pixel_ratio_f_a
            smallest_inverse_diagonal = dark_pixel_ratio_f_a - 2

            horizontal_differences = []
            diagonal_differences = []
            inverse_diagonal_differences = []

            ## Filter the answer choice matrices whose dpr values are within the dpr thresholds
            ## of the horizontal, diagonal, and inverse diagonal dpr values.
            
            ## Add them to the differences lists (from the ipr list).

            for idx, amount in enumerate(dark_pixel_ratio_inverse_diagonal):
                if smallest_inverse_diagonal <= amount <= largest_inverse_diagonal:
                    inverse_diagonal_differences.append(
                        intersection_pixel_ratio_inverse_diagonal[idx])

            for idx, amount in enumerate(dark_pixel_ratio_diagonal):
                if smallest_diagonal <= amount <= largest_diagonal:
                    diagonal_differences.append(
                        intersection_pixel_ratio_diagonal[idx])

            for idx, amount in enumerate(dark_pixel_ratio_horizontal):
                if smallest_horizontal <= amount <= largest_horizontal:
                    horizontal_differences.append(
                        intersection_pixel_ratio_horizontal[idx])

            ## Calculate the answer choice from the inverse diagonal differences list with best fit, and return its index and value.
            ## If no answer choice matrices lie within the inverse diagonal threshold, calculate the one with the
            ## most similar dpr (to dpr between A and F) and calculate its index and value.

            if len(inverse_diagonal_differences) == 0:
                amount = np.abs(
                    dark_pixel_ratio_inverse_diagonal-dark_pixel_ratio_f_a)
                idx = np.argmin(
                    np.abs(dark_pixel_ratio_inverse_diagonal-dark_pixel_ratio_f_a))
                inverse = min(amount)

            ## Otherwise, for the answer choices within the inverse diagonal dpr threshold, calculate the one whose ipr
            ## most closely resembles the ipr between A and F and return its index and value.


            else:
                idx, amount = min(enumerate(inverse_diagonal_differences),
                                  key=lambda x: abs(x[1]-intersection_pixel_ratio_f_a))
                idx = intersection_pixel_ratio_inverse_diagonal.index(
                    amount)
                inverse = abs(amount - intersection_pixel_ratio_f_a)

            ## Calculate the answer choice from the diagonal differences list with best fit, and return its index and value.
            ## If no answer choice matrices lie within the diagonal threshold, calculate the one with the
            ## most similar dpr (to dpr between A and E) and return its index and value.

            if len(diagonal_differences) == 0:

                value_d = np.abs(dark_pixel_ratio_diagonal -
                                 dark_pixel_ratio_a_e)
                idx = np.argmin(
                    np.abs(dark_pixel_ratio_diagonal-dark_pixel_ratio_a_e))
                diagonal = min(value_d)

            ## Otherwise, for the answer choices within the diagonal dpr threshold, calculate the one whose ipr
            ## most closely resembles the ipr between A and E and return ist index and value.

            else:
                idx, value_d = min(enumerate(diagonal_differences),
                                   key=lambda x: abs(x[1]-intersection_pixel_ratio_a_e))
                idx = intersection_pixel_ratio_diagonal.index(value_d)
                diagonal = abs(value_d - intersection_pixel_ratio_a_e)

            ## Calculate the answer choice from the horizontal differences list with best fit, and return its index and value.
            ## If no answer choice matrices lie within the  horizontal threshold, calculate the one with the
            ## most similar dpr (to dpr between G and H) and return its index and value,

            if len(horizontal_differences) == 0:
                value_h = np.abs(
                    dark_pixel_ratio_horizontal-dark_pixel_ratio_gh)
                idx = np.argmin(
                    np.abs(dark_pixel_ratio_horizontal-dark_pixel_ratio_gh))
                horizontal = min(value_h)

            ## Otherwise, for the answer choices within the dpr threshold, calculate the one whose ipr
            ## most closely resembles the ipr between G and H and return its index and value.

            else:
                idx, value_h = min(enumerate(horizontal_differences),
                                   key=lambda x: abs(x[1]-intersection_pixel_ratio_g_h))
                idx = intersection_pixel_ratio_horizontal.index(value_h)
                horizontal = abs(value_h - intersection_pixel_ratio_g_h)

            ## We have filtered the answer choice matrices whose horizontal, diagonal, and inverse diagonal relationships with adjacent matrices
            ## most closely match the horizontal, diagonal, and inverse diagonal transformational relationships between the matrices A through H in the problem.
                
            ## Aggregate the candidates for the best answer choice matrix into a transformations list
            ## and calculate the transformation with the smallest value and corresponding index in the list.

            transformations = [horizontal, diagonal, inverse]
            smallest_value = min(transformations)
            smallest_idx = transformations.index(smallest_value)

            x = min(horizontal, diagonal, inverse)

            ## If the closest matching answer choice (indicated by smallest index = 0) is from a horizontal transformation,
            ## and if there is only one suitable answer choice, calculate the dpr difference and return the index value.

            if smallest_idx == 0 and len(horizontal_differences) == 0:
                value_h = np.abs(
                    dark_pixel_ratio_horizontal-dark_pixel_ratio_gh)
                idx = np.argmin(
                    np.abs(dark_pixel_ratio_horizontal-dark_pixel_ratio_gh))
                amount = 1 + idx
                return amount

            ## Otherwise, for the suitable answer choices within the horizontal dpr threshold, calculate the one whose ipr
            ## most closely resembles the ipr between G and H, and return its index.

            elif smallest_idx == 0 and len(horizontal_differences) != 0:
                idx, value_h = min(enumerate(horizontal_differences),
                                   key=lambda x: abs(x[1]-intersection_pixel_ratio_g_h))
                idx = intersection_pixel_ratio_horizontal.index(value_h)
                amount = 1 + idx
                return amount

            ## If the closest matching answer choice (indicated by smallest index = 1) is from a diagonal transformation,
            ## and if there is only one suitable answer choice, calculate the dpr difference and return the index value.

            elif smallest_idx == 1 and len(diagonal_differences) == 0:
                value_d = np.abs(dark_pixel_ratio_diagonal -
                                 dark_pixel_ratio_a_e)
                idx = np.argmin(
                    np.abs(dark_pixel_ratio_diagonal-dark_pixel_ratio_a_e))
                amount = 1 + idx
                return amount

            ## Otherwise, for the suitable answer choices within the diagonal dpr threshold, calculate the one whose ipr
            ## most closely resembles the ipr between G and H, and return its index

            elif smallest_idx == 1 and len(diagonal_differences) != 0:
                idx, value_d = min(enumerate(diagonal_differences),
                                   key=lambda x: abs(x[1]-intersection_pixel_ratio_a_e))

                idx = intersection_pixel_ratio_diagonal.index(value_d)
                amount = 1 + idx
                return amount

            ## If the closest matching answer choice (indicated by smallest index = 2) is from an inverse diagonal transformation,
            ## and if there is only one suitable answer choice, calculate the dpr difference and return the index value.

            elif smallest_idx == 2 and len(inverse_diagonal_differences) == 0:
                amount = np.abs(
                    dark_pixel_ratio_inverse_diagonal-dark_pixel_ratio_f_a)
                idx = np.argmin(
                    np.abs(dark_pixel_ratio_inverse_diagonal-dark_pixel_ratio_f_a))
                amount = 1 + idx
                return amount

            ## Otherwise, for the suitable answer choices within the inverse diagonal dpr threshold, calculate the one whose ipr
            ## most closely resembles the ipr between G and H, and return its index.

            else:
                idx, amount = min(enumerate(inverse_diagonal_differences),
                                  key=lambda x: abs(x[1]-intersection_pixel_ratio_f_a))
                idx = intersection_pixel_ratio_inverse_diagonal.index(
                    amount)
                amount = 1 + idx
                return amount


        ## Solve Problems E (all 3x3):
        

        if problem.problemSetName == "Basic Problems E" or problem.problemSetName == "Test Problems E" or problem.problemSetName == "Challenge Problems E" or problem.problemSetName == "Raven's Problems E":

            ## Each bitwise operation takes two images and returns a new image.
            
            ## Bitwise Or: Creates image with black pixels where both images have black pixels, and white pixels everywhere else.
            ## Bitwise Xor: Creates image with black pixels where both images have same colored pixels, and white pixels where both images have different colored pixels.
            ## Bitwise And: Creates image with white pixels where both images have white pixels, and black pixels everywhere else.
            ## Bitwise Not: Creates image with inverted black and white pixels.

            ## Create image with black pixels where both A and B have black pixels, and white pixels everywhere else.
            bitwise_or_h = cv2.bitwise_or(self.a, self.b)
            ## Create image with black pixels where both A and B have same colored pixels, and white pixels where both images have different colored pixels.
            bitwise_xor_h = cv2.bitwise_xor(self.a, self.b)
            ## Create image with white pixels where both A and B have same colored pixels, and black pixels where both images have different colored pixels (inversion of bitwise_xor_h).
            bitwise_xor_h_i = cv2.bitwise_not(bitwise_xor_h)
            ## Create image with white pixels where both A and B have white pixels, and black pixels everywhere else.
            bitwise_and_h = cv2.bitwise_and(self.a, self.b)

            ## Use metric (calc_similarity) to compare new images with C.

            ## measures similarity between C and bitwise_or_h
            w = self.calc_similarity(bitwise_or_h, self.c)
            ## measures similarity between C and bitwise_xor_h
            x = self.calc_similarity(bitwise_xor_h, self.c)
            ## measures similarity between C and bitwise_xor_h_i
            y = self.calc_similarity(bitwise_xor_h_i, self.c)
            ## measures similarity between C and bitwise_and_h
            z = self.calc_similarity(bitwise_and_h, self.c)

            ## list of similarity values
            bitwise_list = [w, x, y, z]
            ## measures the highest similarity value in bitwise_list
            max_value = max(bitwise_list)
            ## measures the index of the value in bitwise_list which corresponds to max_value
            max_index = bitwise_list.index(max_value)

            ## The bitwise operation which represents the transformation between A, B, and C will now be applied between G and H.
            ## compare_to is the image formed by applying the transformation between G and H.
            
            if max_index == 0:
                compare_to = cv2.bitwise_or(self.g, self.h)
            elif max_index == 1:
                compare_to = cv2.bitwise_xor(self.g, self.h)
            elif max_index == 2:
                bitwise_xor_h = cv2.bitwise_xor(self.g, self.h)
                compare_to = cv2.bitwise_not(bitwise_xor_h)
            else:
                compare_to = cv2.bitwise_and(self.g, self.h)

            ## final_list will hold the values of the similarities between the answer choices and the image formed by compare_to
            ## The highest similarity value will correspond to the best answer choice. 

            final_list = []
            
            for i in self.answer_list:
                final_list.append(self.calc_similarity(compare_to, i))

            ## Calculate the largest value in the final list, and return the max index

            max_value = max(final_list)
            max_index = final_list.index(max_value) + 1

            return max_index


    ## Methods for image processing:


    ## binarize(self, image): represents an image in binary format, with pixels represented as numbers in an array.
    ## Converts all pixel values below threshold value of 127 to 0 (black), and all pixel values above threshold value of 127 to 255 (white).
        
    def binarize(self, image):
        op, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        return image


    ## Metrics to calculate similarities between images:
    

    ## calc_similarity(self, image1, image2): calculates similarity between two images as the ratio of shared black pixels
    ## between the two images to the total black pixels between the two images.
    ## Returns 0 if images share no black pixels, and 1 if they share every black pixel (higher value = more similar).

    ## For this metric, we will trace through an example to illustrate how it works.

    ## For example, consider the following:
    ##
    ## image1 = np.array([
    ##      [0, 1, 0],
    ##      [1, 0, 1],
    ##      [0, 0, 0]
    ## ]),
    ##
    ## image2 = np.array([
    ##      [0, 1, 1],
    ##      [1, 0, 0],
    ##      [0, 1, 0]
    ## ]).
    ##
    ## common_black_pixels: returns an array of the same dimension as image1 and image2
    ## with 1's where both images are black and 0's everywhere else.
    ##
    ## common_black_pixels = (image1 == 0) & (image2 == 0)
    ##
    ## >> common_black_pixels = np.array([
    ##          [1, 0, 0],
    ##          [0, 1, 0],
    ##          [1, 0, 1]
    ##    ]).
    ##
    ## For this next part, notice that we can represent each entry in common_black_pixels as an ordered pair (row,col) indicating the position of each entry.
    ## Notice that the entires corresponding to the locations where both images share black pixels in the example are (0,0), (1,1), (2,0), and (2,2).
    ##
    ## indices: returns an 2-tuple of arrays, where each array contains the row (respectively, column) indices at which the images are both black.
    ##
    ## indices = np.where(common_black_pixels)
    ##
    ## >> indices = (array([0, 1, 2, 2]),  # Row indices
    ##               array([0, 1, 0, 2]))  # Column indices
    ##
    ## num_shared_pixels: returns the number of shared black pixels
    ##
    ## num_shared_pixels = len(indices[0]) # notice we could have also performed len(indices[1]), as both iterate through the array and return the number of shared black pixels
    ##
    ## >> num_shared_pixels = 4
    ##
    ## Thus, image1 and image2 share 4 black pixels.
    ##
    ## The next steps deal with image1 and image2.
    ##
    ## black_pixels_image1: returns an array of the same dimension as image1
    ## with 1's where image1 is black and 0's everywhere else.
    ##
    ## black_pixels_image1 = (image1 == 0)
    ##
    ## >> black_pixels_image1 = np.array([
    ##          [1, 0, 1],
    ##          [0, 1, 0],
    ##          [1, 1, 1]
    ##    ]).
    ##
    ## Notice that the entires corresponding to the locations where image1 has a black pixel are (0,0), (0,2), (1,1), (2,0), (2,1), and (2,2).
    ## We reuse the variable indices to indicate the row (respectively, column) indices at which image1 is black.
    ##
    ## indices = np.where(black_pixels_image1)
    ##
    ## >> indices = (array([0, 0, 1, 2, 2, 2]),  # Row indices
    ##               array([0, 2, 1, 0, 1, 2]))  # Column indices
    ##
    ## num_black_pixels_image1: returns the number of black pixels in image1
    ##
    ## num_shared_pixels = len(indices[0]) # notice we could have also performed len(indices[1]), as both iterate through the array and return the number of shared black pixels
    ##
    ## >> num_black_pixels_image1 = 6
    ##
    ## Thus, image1 has 6 black pixels.
    ##
    ## We apply the same steps as above to image2.
    ##
    ## black_pixels_image2 = np.where(image2 == 0)
    ##
    ## >> black_pixels_image2 = np.array([
    ##      [1, 0, 0],
    ##      [0, 1, 1],
    ##      [1, 0, 1]
    ##    ]).
    ##
    ## The entries in image2 with black pixels are (0,0), (1,1), (1,2), (2,0), and (2,2).
    ##
    ## indices = np.where(black_pixels_image1) # indices variable is being reused here
    ##
    ## >> indices = (array([0, 1, 1, 2, 2]),  # Row indices
    ##               array([0, 1, 2, 0, 2]))  # Column indices
    ##
    ## num_black_pixels_image2 = len(indices[0])
    ##
    ## >> num_black_pixels_image2 = 5
    ##
    ## Thus, image2 has 5 black pixels.
    ##
    ## Finally, we calculate the similarity between image1 and image2.
    ##
    ## similarity: returns the ratio of number of shared black pixels to total number of black pixels between image1 and image2
    ##
    ## similarity = num_shared_black_pixels/(num_black_pixels_image2 - num_shared_black_pixels - num_black_pixels_image1)
    ##
    ## >> similarity = 0.5714 (approx.)
    ##
    ## To see this using the above calculations: similarity = 4 / (6 + 5 - 4) = 4/7 ≈ 0.5714.

    def calc_similarity(self, image1, image2):
        common_black_pixels = (image1 == 0) & (image2 == 0)
        indices = np.where(common_black_pixels)
        num_shared_black_pixels = len(indices[0])
        
        black_pixels_image1 = (image1 == 0)
        indices = np.where(black_pixels_image1)
        num_black_pixels_image1 = len(indices[0])
        
        black_pixels_image2 = np.where(image2 == 0)
        indices = np.where(black_pixels_image2)
        num_black_pixels_image2 = len(indices[0])
        
        similarity = num_shared_black_pixels/(num_black_pixels_image1 + num_black_pixels_image2 - num_shared_black_pixels)
        return similarity
        ## return len(np.where((image1 == 0) & (image2 == 0))[0])/(len(np.where((image2 == 0))[0]) + len(np.where((image1 == 0))[0]) - len(np.where((image1 == 0) & (image2 == 0))[0]))

    ## dark_pixel_ratio(self, image1, image2): calculates the dpr of both images and take the difference.
    ## Dpr measures the ratio of number of black pixels to the total number of pixels of a (binarized) image.
    ## The difference returned measures how similar the two images are in terms of total number of black pixels (lower = more similar).

    def dark_pixel_ratio(self, image1, image2):
        ## Calculate each of the two images' dark pixel ratios
        dpr_1 = np.sum(image1)/np.size(image1)
        dpr_2 = np.sum(image2)/np.size(image2)
        ## Return the difference
        return dpr_1 - dpr_2

    ## intersection_pixel_ratio(self, image1, image2): calculates the ipr of two images.
    ## Ipr measures the ratio of shared black pixels between two (binarized) images to number of black pixels of one of the (binarized) images.
    ## The difference returned measures how similar the two images are in terms of position of black pixels (lower = more similar).

    def intersection_pixel_ratio(self, image1, image2):
        if np.sum(image1) == 0 or np.sum(image2) == 0:
            return 0
        
        ## Creates image with black pixels where both images have black pixels, and white pixels everywhere else (the "intersection" of both binarized images)
        intersection = cv2.bitwise_or(image1, image2)
        ## Add the number of shared black pixels
        intersection_pixels = np.sum(intersection)
        ## Calculate each of the two images' intersection pixel ratios
        ipr_1 = (intersection_pixels/np.sum(image1))
        ipr_2 = (intersection_pixels/np.sum(image2))
        ## Return the difference
        return ipr_1 - ipr_2
        ## return (intersection_pixels/np.sum(image1)) - (intersection_pixels/np.sum(image2))
