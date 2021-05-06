# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

aTuple = ('I', 'am', 'a', 'test', 'tuple')

def oddTuples(aTuple):
    """
    Parameters
    ----------
    aTuple : Tuple with strings

    Returns only odd components from tuple
    -------
    """
    return print(aTuple[::2])

oddTuples(aTuple)