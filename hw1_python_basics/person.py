class person:
    name = "blank"
    age = 0
    height = 0
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
    def __repr__(self):
        string = "{:} is {:} years old and {:} cm tall.".format(self.name, self.age, self.height)
        return string

