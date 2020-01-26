import numpy as np
from datetime import datetime

#An class to sort data
class sortData(object):

    def __init__(self):
        self.arr = np.random.random((100))
        # make space for sorted array
        self.sortArr=np.empty(self.arr.shape)

        #copy array so we can modify without overwriting
        self.copArr=np.copy(self.arr)

    # an method to find the minimum value in the dataset
    def findMin(self,arr):
        '''A minimum fuinding function'''
        minN=10000  # a big number
        for i in range(0,arr.shape[0]):
            if(arr[i]<minN):
              minN=arr[i]
              minInd=i
        return(minN,minInd)

    #an method to sort the data 
    def sortarray(self):
      # sort the array
        for i in range(0,self.copArr.shape[0]):
            minN,minInd= self.findMin(self.copArr)
            self.sortArr[i]=minN
            self.copArr[minInd]=1000000
      # write to a file
          # write to a file
        filename="x.txt"
        f=open(filename,"w")
        for i in self.sortArr:
          line=str(i)+"\n"
          f.write(line)

        f.close()
        print("Written to",filename)
