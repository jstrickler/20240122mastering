import sys

target_letter = sys.argv[1]   # get letter on command line

word_count = 0
with open('DATA/words.txt') as words_in:
    for word in words_in:
        if word[0] == target_letter:
            word_count += 1

print(f"There were {word_count} words starting with '{target_letter}'")



