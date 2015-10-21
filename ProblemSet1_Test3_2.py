# -*- coding: utf-8 -*-
s = 'zyxwvutsrqponmlkjihgfedcba'

def correctOrder(firstInput, secondInput):
    return firstInput <= secondInput
    
longestSubString = 0
subString = s[0]

for runner1 in range(0, len(s)-1):
    subStringLen = 1
    
    for runner2 in range(runner1+1, len(s)):
        char1 = s[runner2-1]
        char2 = s[runner2]
        
        if correctOrder(char1, char2):
            subStringLen += 1
            if subStringLen > longestSubString:
                subString = s[runner1:runner2+1]
                longestSubString = subStringLen
        else:
            break
            
print "Longest substring in alphabetical order is: " + subString

