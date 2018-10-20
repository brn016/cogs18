
length = len(message)
index = 0
encoded = ''
key=start_key
while index < length:
    letter = ord(message[index])
    encLetter = letter + key
    newLetter = chr(encLetter)
    encoded = encoded + newLetter
    index = index + 1
    key = key + key_increment