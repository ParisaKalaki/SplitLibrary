import ast
import numpy as np
import os
import sys

dirname = os.path.dirname(__file__)
sys.path.append(os.path.join(dirname, '../test'))

class Splitter:
    '''
    split the input based on sizes.
    Input will be splitted to an array of array with specified size
    
    Parameters
    ----------
    input : array
    
    '''
    def __init__(self, sizeOfRecord=10**6, sizeOfBatch=5*10**6, lengthOfBatch=500):
        '''
        Parameters
        ----------
        sizeOfRecord, sizeOfBatch, lengthOfBatch : int    
            for sake of the unit tests, the limitations
            of sizes are given as parameters.

        '''
        self.sizeOfRecord = sizeOfRecord
        self.sizeOfBatch = sizeOfBatch
        self.lengthOfBatch = lengthOfBatch
        
    def splitLib(self, input):
        
        '''
        Parameters
        ----------
        input : array
            input is an array of string with different size.
        
        Returns
        -------
        array of array
            return an array of batch which every batch is an array of a record.
    
        '''
        output =[]
        batch = []
          
        def addToBatch(self, record, batch):
            batchSize = np.array(batch).nbytes + np.array([record]).nbytes
            if batchSize  <= self.sizeOfBatch and len(batch) <self.lengthOfBatch:
                batch.append(record)
            else: 
                output.append(batch)  
                batch =[]  #empty the batch to make a new batch
                batch.append(record)
                 
            return batch     
        
        def addToOutput(self, input, batch, output):
            for record in arr:
                recSize = np.array([record]).nbytes
                if recSize  >= self.sizeOfRecord:
                    print("record discarded") #just discard from the output
                else:
                     batch = addToBatch(self, record, batch)
            output.append(batch)
            return output                                                              
       
        try:
            arr = ast.literal_eval(str(input))
            if (isinstance(arr, list) and isinstance(self.sizeOfRecord, int) and
                isinstance(self.sizeOfBatch, int) and isinstance(self.lengthOfBatch, int)):
                 outputList = addToOutput(self, arr, batch, output)            
            else:
                raise ValueError 
        except :
            print("Invalid entry")
            sys.exit()

        return outputList
