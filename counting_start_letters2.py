import sys

target_letter = sys.argv[1]   # get letter on command line
output_file_name = f"{target_letter}_words.txt"

word_count = 0
with open('DATA/words.txt') as words_in:
    with open(output_file_name, "w") as words_out:
        for word in words_in:
            if word[0] == target_letter:
                word_count += 1
                words_out.write(word)

print(f"There were {word_count} words starting with '{target_letter}'")



