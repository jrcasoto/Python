# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 15:09:43 2021

@author: casoto
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    biggest = 0

    for key, value in aDict.items():
        if int(len(value)) > biggest:
            biggest = int(len(value))
    
    for key, value in aDict.items():
        if int(len(value)) == biggest:
            return key
        
biggest(animals)