#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

def segment(input_string):
    c = '. '
    output_string = input_string
    if c in input_string:
        output_string = input_string.replace(c, '.\n')
    return output_string

while True:
    line = sys.stdin.readline()
    if line == '':
        break
    output = segment(line)
    sys.stdout.write(output)








