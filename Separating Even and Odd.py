#write a python program that reads a text file named numbers.txt that contains 20integers. 
#The program will create two other text file; the first text file will be named even.txt that will contains all even numbers from the numbers.txt. 
#The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

def Categorize():
#open the three text files
    with open("numbers.txt", "r") as integers_numbers, open("even.txt", "a") as even_integers, open("odd.txt", "a") as odd_integers:
#read the numbers.txt that contains 20integers in each line    
        for line in integers_numbers:
            input_number = int(line)
#if the numbers are even
            if input_number % 2 == 0:
                even_integers.write(str(input_number) + "\n")
#if the numbers are odd
            else: 
                odd_integers.write(str(input_number) + "\n")

Categorize()