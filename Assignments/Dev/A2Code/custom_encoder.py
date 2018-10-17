
# YOUR CODE HERE
custom_encoded = ''
for char in custom_message:
    if char in custom_encodings:
        custom_encoded = custom_encoded + (custom_encodings[char])
    else:
        custom_encoded = custom_encoded +char