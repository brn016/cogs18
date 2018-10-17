
# YOUR CODE HERE
length = len(message)
index = 0
encoded = ''
while index < length:
    letter = ord(message[index])
    encLetter = letter + key
    newLetter = chr(encLetter)
    encoded = encoded + newLetter
    index = index + 1