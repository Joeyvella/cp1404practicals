"""
CP1404/CP5632 Practical
Word occurrences in a string
Estimate of time: 10 minutes
Actual time: 10 minutes
"""

def main():
    """Ask user to enter text of which the code will count the number of times words occour"""
    text = input("Text: ").lower()
    words = text.split()


    word_to_count = {}
    for word in words:
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1


    sorted_words = sorted(word_to_count.items())


    longest_word = max(len(word) for word, _ in sorted_words)


    for word, count in sorted_words:
        print(f"{word:{longest_word}} : {count}")


main()