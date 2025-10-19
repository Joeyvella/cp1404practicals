"""
CP1404/CP5632 Practical
Word occurrences in a string
Estimate of time: 10 minutes
"""

def main():
    text = input("Text: ").lower()  # make it case-insensitive
    words = text.split()  # split into list of words

    # Count word occurrences using a dictionary
    word_to_count = {}
    for word in words:
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1