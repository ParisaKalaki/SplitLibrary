# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 08:16:03 2022

@author: paris
"""
import ast
import numpy as np
import os
import pytest
import sys

dirname = os.path.dirname(__file__)
sys.path.append(os.path.join(dirname, '../split_library'))
import splitlib


input = ['Helsinki', 'Paris', 'this is a long string' 'Rome', 'Barcelona',
         'Tehran', 'Lisbon', 'this is another long string', 'Stokholm', 'Amesterdam']

sizeOfRecord = 70
sizeOfBatch = 80
lengthOfBatch = 3
splitter = splitlib.Splitter(sizeOfRecord,sizeOfBatch,lengthOfBatch)
output = splitter.splitLib(input)

def test_recSize():
    for each in output:
        for i in each:
            assert np.array(i).nbytes  <= sizeOfRecord

def test_batchSize():
    for each in output:
        assert np.array(each).nbytes <= sizeOfBatch

def test_batchlength():
    for each in output:
        assert len(each)  < lengthOfBatch

def test_input():
   arr = ast.literal_eval(str(input))
   assert isinstance(arr, list)

def test_inputVar():
   assert (isinstance(sizeOfRecord, int) and isinstance(sizeOfBatch, int)
           and isinstance(lengthOfBatch, int))
