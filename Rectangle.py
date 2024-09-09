#Custom Classes in Python: Rectangle


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}


rect = Rectangle(5, 10)
for dimension in rect:
    print(dimension)

#Output:
#{'length': 5}
#{'width': 10}
#This class allows us to iterate over an instance of Rectangle, first yielding the length and then the width in the desired format.
