age = int(input("Enter your age: "))

if age == 100:
    print("You get century")
elif age < 0:
    print("You are not born yet")
elif age <= 10:
    print("You are a child")
elif age < 20:
    print("You are a teenager")

else:
    print("You are an adult")