# A function called make_snippet that takes a string as an argument and returns the first five words and then a '...' if there are more than that.

# You may immediately think "I know how to code that!". Resist that temptation and stick to the test-driving process.

# Write a small example as a test.
# Run the test (RED).
# Write enough code to make that test pass.
# Run the test (GREEN).
# Refactor if necessary.
# Return to step 1 and keep going until your program is complete. 

def make_snippet(string):
    words = string.split(" ")
    if len(words) <= 5:
        return " ".join(words)
    else:
        return " ".join(words[0:5]) + "..."