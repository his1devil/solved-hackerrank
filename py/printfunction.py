#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):
    """
Read an integer .

Without using any string methods, try to print the following:


Note that "" represents the values in between.

Input Format
The first line contains an integer .

Output Format
Output the answer as explained in the task.

Sample Input

3
Sample Output

123
Tip
You can use the print function inside a map(). Can you write a  line code to solve the problem above?
    """
    def printf(self, n):
        n = int(raw_input())
        map(lambda x: print(x, end=""), range(1, n+1))
