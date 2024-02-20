test_path = 'tests/A1_out.txt'

my_file = open(test_path, 'r', encoding="utf-8")
my_test = my_file.readlines()
my_file.close()
questions = {}
num = 1.

questions[num] = []

for i in my_test:
    if i == '\n':
        num += 1
        questions[num] = []
    else:
        questions[num].append(i)
