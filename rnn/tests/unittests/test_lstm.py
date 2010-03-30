"""

>>> from rnn.lstm import lstm
>>> inpt = scipy.array([ 0.6,  0.8,  0.2,  0.4,  0.4,  0.6,  0.8,  1. ])
>>> initialstate = scipy.zeros(2)

>>> state, outpt = lstm(inpt, initialstate)
>>> state
array([ 0.35500377,  0.4130792 ], dtype=float32)
>>> outpt 
array([ 0.405588  ,  0.43997008], dtype=float32)
>>> state, outpt = lstm(inpt * 1.5, state)
>>> state
array([ 0.63761002,  0.78988129], dtype=float32)
>>> outpt
array([ 0.50277889,  0.56233251], dtype=float32)

"""

__author__ = 'Justin Bayer, bayer.justin@googlemail.com'

import scipy


        
if __name__ == "__main__":
    runModuleTestSuite(__import__('__main__'))

