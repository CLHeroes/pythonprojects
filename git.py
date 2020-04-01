#### Asomiddin Rustamov  ###  asomiddin@live.com ###
##### ZiyoTek ### 04/02/2020 ##########
import time

print("Welcome to GIT game")
name = input("Please enter your name : ")
print("Hello " + name + "!")
time.sleep(1)

## git init
print(name + ", please help me to create git repo")
print('We are in "/projects" directory, what do we type to make it as "git working directory/tree?" ')
com1 = ''
while com1 != str("git init"):
    com1 = input("please type the command:\n ")
    if com1 == str("git init"):
        print(" Initialized empty Git repository in /projects/.git/")
        print("Thank you for your help!")
    else:
        print("Didn't work, try again.")

time.sleep(1)

## git add
print('\nNow, I just created "/projects/file1" file')
print("And I don't know how to add it to Staging Area \nPlease help me with the command")
com2 = ''
while com2 != str("git add file1"):
    com2 = input("please type the command:\n ")
    if com2 == str("git add file1"):
        print("")
    elif com2 == str("git add ."):
        print("That works too but please add the <file_name> instead . in the end.")
    elif com2 == str("git add"):
        print("Nothing specified, nothing added.\nMaybe you wanted to say 'git add .'?")
    else:
        print("Didn't work, try again.")

time.sleep(1)

## git status
print("\nIt seems we added but I'm not sure since it was no output.\nHow can we check the status?")
com3 = ''
while com3 != str("git status"):
    com3 = input("please type the command:\n ")
    if com3 == str("git status"):
        print(" On branch master\n\nNo commits yet\n\nChanges to be committed:")
        print('  (use "git rm --cached <file>..." to unstage\n')
        print("      new file:   file1")
    else:
        print("Didn't work, try again.")

time.sleep(1)

## git commit
print("Let's commit it now with your name as commit message.")
print("what was the command?")
com4 = ''
while com4 != str('git commit -m "' + name + '"'):
    com4 = input("please type the command:\n ")
    if com4 == str('git commit -m "' + name + '"'):
        print("\n 1 file changed, 0 insertions(+), 0 deletions(-)\ncreate mode 100644 file1\n")
    elif com4 == str('git commit -a'):
        print('use -m "message" option for short message')
    else:
        print("Didn't work, try again.")

time.sleep(2)

## git push
print("You are welcome to modify next section.\n\n")

