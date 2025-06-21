try:
    file = open("numbers.txt", "r")
    numbers = file.readlines()
    for num in numbers:
        print(int(num.strip()))
except FileNotFoundError:
    print("The file 'numbers.txt' does not exist.") 
except ValueError:
    print("The file contains non-numeric data.")   
finally:
    print("Done trying to read the file.")
    if 'file' in locals():
        file.close()