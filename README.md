# Security_HW3_Part1

This is my solution to Question 2 of the homework assignment. Question 1 was already submitted in Canvas.

## Purpose
For this assignment, we had to analyze the CrackMe code using Ollydbg in order to figure out the Serial number for any Name.

## Method
To do this, I searched within the code for where the Name and Serial were stored in order to see how they were compared. By going into the call at line at 0040137E (the location called when a Name is entered) we can see that the function captializes the Name entered by the user. The function then goes on to sum the ascii characters of the username and XORs the total with 0x5678.

![Name](https://github.com/jkwourms/Security_HW3_Part1/blob/master/name.JPG)

The function called by the Serial input at line 004013D8 then calls a function that XORs the given Serial value with 0x1234. 

![Serial](https://github.com/jkwourms/Security_HW3_Part1/blob/master/serial.JPG)

The program then compares these two values. If they match, then the user has entered the correct serial number.

## My Solution
In python, the serial is equal to the sum of the characters in the username ^ 0x5678 ^ 0x1234. This can be simplified to the serial is equal to the sum of the characters ^ 0x444C. 

So I simply wrote a python script that takes the *capitalized* version of the Name, performs this calculation, and returns the Serial that will pass the CrackMe test.

## Example
Running my python script

![Python_script_run_example](https://github.com/jkwourms/Security_HW3_Part1/blob/master/run_python_example.jpg)

We can see that the Serial corrosponding to my name is 17553. Entering this number into the CrackMe program results in a successful response.
