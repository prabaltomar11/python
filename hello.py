class student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def introduction(self):

        print(f"Hi, I am : {self.name}, and I am studying: {self.course}")
s1 = student("Prabal", "BCA")

s1.introduction()
