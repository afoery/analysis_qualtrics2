#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:40:10 2020

@author: alisha
"""
import functions_ as func

def count_corrAns(wordsperround, numWords, numRounds, immediateAns,
                          delayedAns, conditions):
    '''     
    This functions computes the amount of correct answers per condition
    per subject.
  
    Output: Counts for immediate and delayed responses
    '''
    
    def splitAndCount(data, conditions, numRounds):
        
        together = []
        recallrecogseparate = []
                
        for i in range(len(data)):
            
            #get individual data (per subject)
            data_indiv = data.loc[i].values.flatten().tolist()
            
            #split data into chunks as presented in study (different rounds)
            data_indiv = list(func.chunks(data_indiv,wordsperround*2))
            
            #initiate some lists
            closed = []
            video = []
            game = []
            
            #distribute data in respective lists
            for j in range(numRounds):
        
                if conditions.loc[i]['cond%d'%j] == 'closed':
                   
                    closed = closed+ data_indiv[j]
                
                elif conditions.loc[i]['cond%d'%j] == 'video':
                    
                    video = video + data_indiv[j]
                    
                else: 
                    game = game + data_indiv[j]
            
            #count how many correct answers per condition
            closedRecall = closed.count('recallCorrect')
            closedRecog = closed.count('recogCorrect')
            
            videoRecall = video.count('recallCorrect')
            videoRecog = video.count('recogCorrect')
            
            gameRecall = game.count('recallCorrect')
            gameRecog = game.count('recogCorrect')
            
             #get number of correct responses  per condition
            together_closed = closedRecall + closedRecog
            together_video = videoRecall+ videoRecog
            together_game = gameRecall+gameRecog
            
            
            together.append([together_closed, together_video, together_game])
            
            #recall and recog separately for each participant
            recallrecogseparate.append([closedRecall, videoRecall, gameRecall, 
                                        closedRecog, videoRecog, gameRecog])
                 
        return together, recallrecogseparate
    
    #calculate counts for immediate and delayed tests
    togetherImm, recallrecogseparateImm= splitAndCount(immediateAns, 
                                                       conditions, numRounds)
    togetherDel, recallrecogseparateDel= splitAndCount(delayedAns, 
                                                       conditions, numRounds)
    
    
    return togetherImm, togetherDel, recallrecogseparateImm, recallrecogseparateDel
    