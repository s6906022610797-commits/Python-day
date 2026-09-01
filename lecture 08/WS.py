with open("example.txt", "r") as file:
    lines = file.read()
    for line in lines:
        print(line.strip())