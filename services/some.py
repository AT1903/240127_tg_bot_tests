book_path = "tests/A1.txt"
b2 = 'tests/A1_out.txt'
# my_dict = {}


my_file = open(book_path, 'r', encoding="utf-8")
my_test = my_file.readlines()
my_file.close()
questions = {}
num = 1.

questions[num] = []
output = []

for i in my_test:
    if len(i) > 1:
        if i[-2] != '+':
            output.append(i[:-1] + ' \n')
        else:
            output.append(i)
    else:
        output.append(i)

my_file1 = open(b2, 'w', encoding="utf-8")
my_file1.writelines(output)
my_file1.close()