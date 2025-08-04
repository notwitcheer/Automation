# Starting with text files.

import os.path

filename = os.path.join('rep', 'my_file.txt')
print('filename:' + filename)
if os.path.exists(filename):
    print('File exists.')
else:
    print('File does not exist.')


f = open('my_file.txt', 'w')

f.write('Henlo\n')

l = ['first sentence\n', 'second sentence\n', 'last sentence\n']

f.writelines(l)

for i in range(10):
    f.write(str(i+1) + '\n')

f.close()