# slicing

name = input("Enter your name: ")

first_name = name[:4]
last_name = name[4:]
modern_name = name[::2]
reverse_name = name[::-1]

print(reverse_name)

website = input("Enter your website address: ")
slice = slice(7,-4)
print(website[slice])