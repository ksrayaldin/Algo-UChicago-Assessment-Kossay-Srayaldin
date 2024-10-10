# Algo-UChicago-Assessment-Kossay-Srayaldin
Name: Kossay Srayaldin
Algo Group Uchicago Assessment. 

Option 2: Implement Stack
Create an integer stack without containers (list, vector, array, etc.) with methods:
    "push" adds an integer to the top and does not return anything
    "pop" returns and removes the integer at the top. If the stack is empty, an error is thrown
    "peek" returns the integer at the top. If the stack is empty, an error is thrown.
    "size" return an integer - the number of values on the stack

Method: I implement this stack using linked lists (standard method). To do this, I create a
"Node" Class to represent the integers in the stack as objects. Each object has a value
and a pointer to the next integer in the stack. The idea is to be able to organize the objects in the stack
using pointers. Next, I create a "Stack" class that is used to modify how the objects point to each other.
This is where I implement all the methods noted above.

***TESTING***

I did not create any extra testing files to save myself some time. I included a few basic commands in this file that should
hopefully be enough to demonstrate that the stack works as it should. All you have to do is run the current file 
through a python interpreter (python3). It should log some info on your terminal. The answers inside parentheses are 
expected answers while the answers outside the parantheses are the actual answers... For the last part, if you want
to test out whether pop() or peek() give out an error message, just comment out the line you don't want to run as explained below. 

Thanks a lot!!!
