
# Knowing the start key, and the length of the message, we can reconstruct the current key
key = start_key + (len(encoded) * key_increment)

decoded = ''

# Note that this decodes the message backwards, stepping back along key values
for char in encoded[::-1]:
    
    # Step the key back one step, and apply to current character
    key = key - key_increment
    decoded = decoded + chr(ord(char) - key)
    
# Having decoded backwords, flip the message back around
decoded = decoded[::-1]