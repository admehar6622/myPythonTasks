# constructor used to create a object.
#__init__ used to create a constructor


class person:
    def __init__(self, n, o):
        print("Hi- I'm a person")
        self.name = n
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("adnan", "Developer")
#a.name = "Imran"
#a.occ = "IT Support"
#a.info()

a.info()
