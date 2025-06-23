
   
size = int(input("Enter the size of the pattern: "))

if size <= 0:
        print("Please enter a positive integer.")       
row = 0

while row < size:
        # Nested for loop to print asterisks in the current row
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after printing a row
        row += 1


