#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:29:53 2020

@author: alisha

this programm calculates the amount of correct answers per subject 
for recog and recall separate and together

"""

import loadData, checkData, count
import pickle

numWords = 42
wordsperround = 7
numRounds = 6

#import data
immediateAns, delayedAns, solutions, conditions, IDs= loadData.load_data(numWords)

#check answers
immediateAns, delayedAns = checkData.check_data(numWords,immediateAns, 
                                                delayedAns, solutions)

#calculate how many correct answers per condition
togImm, togDel, sepImm, sepDel = count.count_corrAns(wordsperround, numWords, 
                                                     numRounds, immediateAns,
                                                     delayedAns, conditions)

#export results
with open(F"saveThings/results_S1_separateImmediate.txt", "wb") as fp:
    pickle.dump(sepImm,fp)
with open(F"saveThings/results_S1_separateDelayed.txt", "wb") as fp:
    pickle.dump(sepDel,fp)
with open(F"saveThings/identifiersS1.txt", "wb") as fp:
    pickle.dump(IDs,fp)
with open(F"saveThings/solutionsS1.txt", "wb") as fp:
    pickle.dump(solutions,fp)
with open(F"saveThings/conditionsS1.txt", "wb") as fp:
    pickle.dump(conditions,fp)