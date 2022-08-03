# fucc 12
import sys

name = input("What's your name? \n")

print("Hello, " + name + "!\nHow are you?")

# raw_input returns the empty string for "enter"
yes = {'yes','y', 'ye'}
no = {'no','n'}

choice = input().lower()
if choice in yes:
   print('YES')
elif choice in no:
   print('NO')
else:
   sys.stdout.write("Please respond with 'yes' or 'no'")
   choice