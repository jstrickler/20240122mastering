
with open('myinputfile.txt') as file_in:
    with open('myoutputfile.txt', 'w') as file_out:
        # open 3rd file here..
        for line in file_in:
            # do stuff
            file_out.write(line)