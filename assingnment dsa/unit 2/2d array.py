# input matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix values:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Matrix is:")
for r in matrix:
    print(r)


# row sum
print("\nRow sums:")
for i in range(rows):
    s = 0
    for j in range(cols):
        s += matrix[i][j]
    print(f"Row {i} sum = {s}")


# column sum
print("\nColumn sums:")
for j in range(cols):
    s = 0
    for i in range(rows):
        s += matrix[i][j]
    print(f"Column {j} sum = {s}")


# search element
key = int(input("\nEnter element to search: "))
found = False

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == key:
            print("Element found at position:", i, j)
            found = True

if not found:
    print("Element not found")


# transpose
print("\nTranspose:")
for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()
