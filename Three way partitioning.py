#Given an array of size n and a range [a, b]. The task is to partition the array around the range such that array is divided into three parts.
#1) All elements smaller than a come first.
#2) All elements in range a to b come next.
#3) All elements greater than b appear in the end.
#The individual elements of three sets can appear in any order. You are required to return the modified array.
class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
def swap(self,array,left,right):
        temp=array[left]
        array[left]=array[right]
        array[right]=temp
        
def threeWayPartition(self, array, a, b):
	# code here 
            n=len(array)
            left = 0
            right = n-1
            i=0
            
            while i<=right:
                    if array[i]<a:
                        self.swap(array,left,i)
                        left=left+1
                    if array[i]>b:
                        self.swap(array,right,i)
                        right=right-1
                    else:     
                        i=i+1