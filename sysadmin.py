import os
#os.mkdir('newdir')
#os.rmdir('newdir')
# os.system('ls -lah')
# print(os.name)
# print(os.getcwd())
# a = 0
# file = ['me', 'you', 'all']
# for i in file:
#     if a <= 3:
#         os.system('touch ' + i)
#     a = a + 1




# def get_filename_datetime(): 
#     # Use current date to get a text file name. 
#     return (str(date.today()) + "_testfile.txt") 

# print(get_filename_datetime())

import datetime
dynamic_file = (str(datetime.date.today()) + "_testfile.txt")
print(dynamic_file)
    