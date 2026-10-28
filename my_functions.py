# functions
def greet():
    print("Hello, welcome to python")


def greeting(user):
    print(f"Hello {user}, welcome to python")

def area_circle(radius, precision = 3):
    a = 22/7 * radius
    result = round(a, precision)
    print(result)

def volume_cylinder(r, h):
    v = 22/7 * r**2 * h
    return v

# use == call
# greet()
# greet()
# greet()
#
# greeting("Jim")
# greeting("Amanda")
#
# # positional params
# area_circle(7.9, 2)
# area_circle(5, 0)
# area_circle(8 )
#
#
# #named params
# area_circle(precision=2, radius=11)


print(volume_cylinder(27, 10.5))