# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 14:35:11 2021

@author: casoto
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for key, value in aDict.items():
        for element in value:
            count += 1
    return count

print(how_many(animals))