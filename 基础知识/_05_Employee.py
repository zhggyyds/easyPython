class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self,add=None):
        if add:
            self.salary += add
        else:
            self.salary += 5000
