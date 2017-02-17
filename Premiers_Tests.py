#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 14:20:50 2017

@author: benjaminpujol
"""

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import math
import pandas as pd


#Load dictionary

f = open('/Users/benjaminpujol/Documents/Cours3A/DeepLearning/calldesk-intents.txt')
input = f.read()
words = input.split()
my_dictionary = list(set(words))
print len(my_dictionary)
print my_dictionary.index("esprit")

#Convert txt to matrix

input = input.splitlines()

for i in range(len(input)):
    input[i] = input[i].split()
    
#Shuffle lines
from random import shuffle
shuffle(input)
    
    
