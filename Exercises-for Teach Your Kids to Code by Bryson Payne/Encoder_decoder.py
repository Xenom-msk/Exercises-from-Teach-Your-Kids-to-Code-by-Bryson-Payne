# Encoder decoder
massage=input("Enter a massage to encoder or decoder: ")
massage=massage.upper()
output=""                           # Empty string to hold output
for letter in massage:              # Loop each letter in the massage
    if letter.isupper():            # If the letter is in the alphabet (A-Z)
        value=ord(letter)+13        # Shift the letter value up by 13
        letter=chr(value)           # Turn the value back into a letter
        if not letter.isupper():    # Check to see if we shifted so far
            value-=26               # If we did, warp it aroun Z->A
            letter=chr(value)       # by subtracing 26 from the letter value
    output+=letter                  # Add the letter to our output string
print("Output massage: ", output)
