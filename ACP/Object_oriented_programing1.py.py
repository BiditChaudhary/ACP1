class Tom:
    def __init__(self, name1):
        self.name1 = name1

    def intro(self):  # Removed the unused parameter
        print(f"Hi! My name is {self.name1}.")

class Jerry:
    def __init__(self, name1):
        self.name1 = name1

    def intro(self):  # Removed the unused parameter
        print(f"Hi! My name is {self.name1}.")

T = Tom("Tom")
J = Jerry("Jerry")

T.intro()
J.intro()