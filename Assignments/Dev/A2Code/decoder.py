
# YOUR CODE HERE
decoded = ''
length = len(encoded)
index = 0
while index < length:
    letter = ord(encoded[index])
    decLetter = letter - key
    newLetter = chr(decLetter)
    decoded = decoded + newLetter
    index = index + 1