# -*- coding: utf-8 -*-
s = 'mqdvjlaffo'
s = s + str(1)

subStringLength = 0
longestSubString = ""

for start in range(0, len(s)-1):
    counter = 1
    for end in range(start+1, len(s)):
        if s[end] >= s[end-1]:
            counter += 1
        else:
            if counter > subStringLength:
                longestSubString = s[start:end]
                subStringLength = counter
            break
            
print "Longest substring in alphabetical order is: " + longestSubString