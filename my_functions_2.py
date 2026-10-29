def add(x,y,z):
    return x+y+z

# pass #don't do anything, to utilize it later

#taking in as many args as possible
#def addition(z, *nums) => this is the order
def addition(*nums):
    total = sum(nums)
    # total = 0
    # for num in nums:
    #     total += num
    return total

# key and word arguments => **kwargs
def save(**data):
    with open("values.txt", "w") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")

save(dob='2025-01-18', gender='Female', color='Green', name='Hannah')


def some_function(name, *scores, **details):
    pass



def cylinder(r,h):
    """
    Calculates the volume and SA of a cylinder
    parameters:
    radius and height of the cylinder
    :returns: volume and Surface Area of the cylinder
    """
    v=22/7*r*r*h
    sa=22/7*r**2*2 + 22/7*r*2*h
    return sa, v




surf_area, volume = cylinder(r=21,h=5)

print(surf_area, '\n' , volume)

sum([2,3,4])

#lamda functions

# lambda x,y : x/y
divider = lambda x,y :x/y

area_circle = lambda r : 22/7 * r**2

print(divider(63, 9))
res = area_circle(9.3)
print(res)


#some_function("Hellen", 10,90,87, gender='Female', course='Chem')
# print(addition(7,99,34,73, 87, 98,87,12,42, 52,67))
# print(addition(89,78))
#
# res = add(2,7,8)
# print(res)
# data = {"name":"Ken", "gender":"Male"}
# for item in data.items():
#     print(item)