# part 1
def student_discount(curr_price):
    return(curr_price - (curr_price * .1))


def additional_discount(curr_price):
    return(student_discount(10) - (curr_price * .05))


print(student_discount(10))
print(additional_discount(10))

# part 2
print((lambda x: x*(x+5)**2)(5))

# part 3
item_price = [10, 20, 30, 40, 50, 60]

discounted_items = list(map(student_discount, item_price))
print(discounted_items)

# part 4
class Computer:
    def __init__(self, height, width):
        self.height = height
        self.width = width


    def get_specs(self, height, width):
        self.height = height
        self.width = width


    def display_specs(self):
        print(self.height, self.width)
    

class Laptop(Computer):
    weight = 0

    def get_weight(self, weight):
        self.weight = weight

    def display_weight(self):
        print(self.weight)

    
class Desktop(Computer):
    depth = 0

    def get_depth(self, depth):
        self.depth = depth

    
    def display_depth(self):
        print(self.depth)

laptop = Laptop(0, 0)

laptop_height = input('What is the laptop height: ')
laptop_width = input('What is the laptop width: ')
laptop_weight = input('What is the laptop weight: ')

# Computer class methods
laptop.get_specs(laptop_height, laptop_weight)
laptop.display_specs()

# Laptop methods
laptop.get_weight(laptop_weight)
laptop.display_weight()

desktop = Desktop(0, 0)

desktop_height = input('What is the desktop height: ')
desktop_width = input('What is the desktop width: ')
desktop_depth = input('What is the desktop depth: ')

# Computer class methods 
desktop.get_specs(desktop_height, desktop_width)
desktop.display_specs()

# Desktop methods 
desktop.get_depth(desktop_depth)
desktop.display_depth()

# part 5
class A:
    def __init__(self, a):
        self.a = a

    def __mul__(self, other):
        return self.a + other.a

object1 = A(5)
object2 = A(10)

print(object1 * object2)