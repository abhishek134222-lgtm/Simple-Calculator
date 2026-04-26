from data import data
from Addition import Addition
from Substraction import Substraction   
from Multiplication import Multiplication
from Division import Division


def main():
    print("==== Welcome to Abhishek's Simple Calculator ====")
    print(" ")
    while True:
        print("Enter 1 to perform Addition")
        print("Enter 2 to perform Subtraction")
        print("Enter 3 to perform Multiplication")
        print("Enter 4 to perform Division")
        print("Enter 5 to Exit")
        choice = int(input("Enter your Choice : "))
        
        if choice == 1:
            data() 
            Addition()
        elif choice == 2:
            data()
            Substraction()
        elif choice == 3:
            data()
            Multiplication()
        elif choice == 4:
            data()
            Division()
        elif choice == 5:
            print("Thanks For Using My caclulator")
            break
        else: print("Invalid Input  !!!")

main()