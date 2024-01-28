from subprocess import run, PIPE
import shlex

# run([list-of-words-in-command])

# "ls -l"       NO
# ["ls", "-l"]  YES

cmd = "hostname"
cmd_words = shlex.split(cmd)

result = run(cmd_words)
print(result)
print(f"{result.returncode = }")
print('-' * 60)

result = run(cmd_words, stdout=PIPE)
print(result.stdout.decode())
print('-' * 60)


netstat_cmd = "netstat -an"
cmd_words = shlex.split(netstat_cmd)
result = run(cmd_words, stdout=PIPE)

output_lines = result.stdout.decode().splitlines()

# print(output_lines[:5])

for line in output_lines:
    if 'ESTABLISHED' in line:
        print(line)

