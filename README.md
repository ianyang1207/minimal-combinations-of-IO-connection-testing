# unique-combination-of-2^n-number

Say, there is a list of 8 I/O [0,1,2,3,4,5,6,7]  

We want to test 0->1, 1->0, 0->2, 2->0... to ensure that every I/O can be connected to another, considering the direction.

To be efficient, we'd like to minimize the times to try.

The expectation result is,  
[[0, 1, 2, 3, 4, 5, 6, 7],  
 [1, 3, 0, 5, 2, 7, 4, 6],  
 [2, 0, 4, 1, 6, 3, 7, 5],  
 [3, 5, 1, 7, 0, 6, 2, 4],  
 [4, 2, 6, 0, 7, 1, 5, 3],  
 [5, 7, 3, 6, 1, 4, 0, 2],  
 [6, 4, 7, 2, 5, 0, 3, 1],  
 [7, 6, 5, 4, 3, 2, 1, 0]]
 
