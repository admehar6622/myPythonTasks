class Person:
    name = "Adnan"
    occupation = "IT Engineer"
    worth = 20
    def info(self):
        print(f"{self.name} is a {self.occupation} and his accupation is {self.worth}")

a = Person()
b = Person()
a.name = "imran"
a.occupation = "software developer"
b.name = "majid"
b.worth = 40
#print(a.name,a.occupation)
a.info()
b.info()