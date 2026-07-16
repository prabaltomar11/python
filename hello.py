try:
    with open("goste.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File does not exist! But the code is safe.")