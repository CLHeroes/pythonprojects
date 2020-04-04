import os
#os.mkdir('newdir')
#os.rmdir('newdir')
# os.system('ls -lah')
# print(os.name)
# print(os.getcwd())
a = 0
file = ['me', 'you', 'all']
for i in file:
    if a <= 3:
        os.system('touch ' + i)
    a = a + 1


