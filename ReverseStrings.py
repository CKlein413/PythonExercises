# This exercise is going to take in a string and then reverse the text.
# Example entering ABC will be reversed to CBA
# Slice [start:stop:step]
# For reverse the start will be the higher position since reverse (-step) is going right to left.

reversetext = input("Text to reverse: ")

def reverse(string): 
    string = string[::-1] 
    return string 
print ("Reversed Text: " + (reverse(reversetext))) 

