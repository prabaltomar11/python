with open("Diary.txt", "w") as file:
    file.write("Today I started Phase 4 of Python.\n")



with open("Diary.txt", "r") as file:
    content = file.read()
    print(content)