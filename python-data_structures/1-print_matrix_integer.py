#Function that prints a matrix of integers.  
#Function that prints a matrix of integers.
def print_matrix_integer(matrix=[[]]):
    Row = int(input("Enter the number of rows:"))
    Column = int(input("Enter the number of columns:"))
    matrix = [[]]
    for row in range(Row):
        a = []
        for column in range(Column):
            a.append(int(input()))
        matrix.append(a)    

    for row in range(Row):
        for column in range(Column):
            print(matrix[row][column], end=" ")
        print()    



Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries row wise:")

# For user input
# A for loop for row entries
for row in range(Row): 
	a = []
	# A for loop for column entries
	for column in range(Column): 
		a.append(int(input()))
	matrix.append(a)

# For printing the matrix
for row in range(Row):
	for column in range(Column):
		print(matrix[row][column], end=" ")
	print()
	
