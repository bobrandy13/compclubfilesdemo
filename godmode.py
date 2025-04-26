# By adding a plus sign, we can do both reading and writing
file = open("demo.txt", "w+")

# We can write
file.write("Hello, CompClub!")

# Think of this like you writing a diary
file.seek(0)

# We can read
print(file.read())

file.close()