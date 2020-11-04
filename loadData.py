#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:24:26 2020

@author: alisha
"""

import pandas as pd
import functions_ as func

def load_data(numWords):
    """ 
    This function extract the important data from a Qualtrics output .csv file 
    """
            
    #load data of session 2  ---------------------------
    df = pd.read_csv('data.csv', index_col = None, header = 0)
    
    #drop certain subjects
    df = df[df.RandomID != '87965'] #16 minute break
    df = df[df.RandomID != '77236'] # internet connection dropped
    df = df[df.RandomID != '31997'] #sahana
    df = df[df.RandomID != '34054'] #2am in the morning morocco
    
    #participant ID 
    identifiers = df['RandomID']
    identifiers = func.deleteFirstTwoColumns(identifiers)
    
    #extract immediate answers of qualitrcs output
    immediateAns = df[['i%d'%i for i in range(numWords*2)]]
    immediateAns = func.deleteFirstTwoColumns(immediateAns)
    
    #extract delayed answers of qualtrics output
    delayedAns = df[[str(i) for i in range(numWords*2)]]
    delayedAns = func.deleteFirstTwoColumns(delayedAns)
    
    #extract solutions (correct answers)
    solutions = df[['english' + str(i) for i in range(numWords)]]
    solutions = func.deleteFirstTwoColumns(solutions)
    
    #remove all whitespaes from solutions
    solutions = solutions.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    conditions = df[['cond' + str(i) for i in range(6)]]
    conditions = func.deleteFirstTwoColumns(conditions)
    
    #replace some words, because we only need to know which condition the
    #subject was presented with and not which exact game or video
    replace = {'swingTriangle' : 'game', 
               'yeti': 'game',
               'videoYeti': 'video',
               'videoTriangle': 'video'}
    
    conditions.replace(replace, inplace = True)
    
    #rename column names with integers 
    immediateAns.columns = [x for x in range(numWords*2)]
    delayedAns.columns = [x for x in range(numWords*2)]
    
    
    return immediateAns, delayedAns, solutions, conditions, identifiers




