#MadLib.py
#Name:Jadon Wiebe
#Date:8/31/2025 (Last minute I know)
#Assignment:MadLib.py

def main():
  print("Madlib")
  #Ask user for words
noun1 = input("Enter a noun: ")
emotion1 = input("Enter an emotion: ")
emotion2 = input("Enter another emotion: ")
holiday1 = input("Enter a holiday: ")
number1 = input ("Enter a number: ")
workout1 = input("Enter a workout: ")
  #Print the story with the user supplied words.
print("I know nothing about " + noun1 +".")
print("This class is going to cause me a lot of " + emotion1 + "!")
print("If I do " + number1 +  workout1 + " every time I get " + emotion2 + " I'll be jacked by " + holiday1 + "!")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
