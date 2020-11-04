#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:32:59 2020

@author: alisha
"""

from copy import deepcopy

def check_data(numWords,immediateAns, delayedAns, solutions ):
    """
    This function checks the answers of the participants and returns
    2 dataframes (immediate and delay responses) which include the strings
    "recallCorrect" and "recogCorrect" for answers that are correct
    """
    #save originals
    immediateOriginal = deepcopy(immediateAns)
    delayedOriginal = deepcopy(delayedAns)
    
    #check which recognition answers are correct
    for i in range(numWords):
        immediateAns = immediateAns.replace({'${e://Field/answer%d0}'%i : 'recogCorrect'})
        delayedAns = delayedAns.replace({'${e://Field/answer%d0}'%i : 'recogCorrect'})
     
    #repace 'nan' because we can't have float object for replace function later
    immediateAns.fillna('',inplace = True)
    delayedAns.fillna('',inplace = True)
    
    #remove all whitespaces
    immediateAns = immediateAns.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    delayedAns = delayedAns.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    #replace misspelled answers from participants
    replaceDic = {'cow?':'cow', 'banan':'banana', 'grasshoper':'grasshopper',
                  'carr':'car', 'elephent': 'elephant', 'turtule': 'turtle',
                  'benana': 'banana', 'eyes' : 'eye', 'gra': 'grasshopper',
                  'Watermelon\\': 'watermelon', 'co': 'cow' , 
                  'catterpillar' : 'caterpillar',
                  'cterpillar': 'caterpillar', 'Grashopper': 'Grasshopper', 
                  'Bow,': 'Bowl',
                  'Ake' : 'Axe', 'bread ': 'bread', 'doll ': 'doll', 
                  'toothrush' : 'toothbrush', 'plane': 'airplane',
                  'caterpillar ' : 'caterpillar', 'ar': 'ear', 'ax': 'axe',
                  'Griffafe': 'giraffe', 'reindeer' : 'deer', 
                  'envelope ': 'envelope', 'bottel ': 'bottle', 
                  'ancher ': 'anchor',
                  'elephant ': 'elephant' ,'giraffe ': 'giraffe', 
                  'onion ': 'onion',
                  'chicken ': 'chicken', 'turtle ': 'turtle', 'dol': 'doll',
                  'catepillar': 'caterpillar', 'barre;': 'barrel',
                  'catiplillar': 'caterpillar', 'catipiller': 'caterpillar',
                  'airplane ' : 'airplane', 'choe':'shoe', 'Plane':'Airplane'}
    
    immediateAns.replace(replaceDic, inplace = True)
    delayedAns.replace(replaceDic, inplace = True)
    
    def checkRecall(data,solutions,numWords, original):
        for i in range(len(data)):
            for j in range(0,numWords):
                
                #make capital letters to compare answers to solution words
                data.loc[i,((j*2))] = data.loc[i,((j*2))].title()
                
                #check whether correct
                if data.loc[i,((j*2))] == solutions.loc[i]['english%d'%j]:
                    data.loc[i,((j*2))] = 'recallCorrect'
                
                if (data.loc[i,((2*j))] != 'recallCorrect'):
                    print(i,(j*2), original.loc[i,((2*j))], solutions.loc[i]['english%d'%(j)] )
        return data
    
    immediateAns = checkRecall(immediateAns, solutions, numWords, immediateOriginal)
    delayedAns = checkRecall(delayedAns, solutions, numWords, delayedOriginal)
    
    return immediateAns, delayedAns