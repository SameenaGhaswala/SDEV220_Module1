test1 = "This is a test of the emergency text system"

with open("test.txt", "w") as f:
    f.write(test1)

with open("test.txt", "r") as f:
    test2 = f.read()
    if test2 == test1:
        print("Yes, they both are same")
    else:
        print("No, they both are different")