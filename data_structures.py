#stores lots data

#data structures
# list, set, tuple, dictionary


#list []
people = ["Jack", "Jane", "Ahmed", "Hussein", "Miriam"]
scores = [34, 55, 77, 53, 7, 23, 14, 52, 98]

# print(people[0])
# print(scores[0])
# print(people[-1]) #last value
#
# #append adds at the end
# people.append("Willis")
# print(people)
# scores.append(398)
# print(scores)
#
# #clear deletes everything
# # people.clear()
# # print(people)
#
#
# people.sort()
# scores.sort()
# scores.sort(reverse=True) # sorts in descending order
# print(people)
# print(scores)
#
# print(scores[0], scores[-1])
#
# print(sum(scores) // len(scores))
#
# print(scores.count(34))

scores.sort()
#slicing
print(scores)
print(scores[-3:])
print(scores[:3])

print(scores[3:5])# it is not inclusive of the last number


# set {}
numbers = {34,64,76,13,64}
print(numbers)

# Tuple () => can't add or remove
days = ("Mon", "Tue", "Fri")


#dictionary {} => key + value
person = {"name" : "Zilon", "city": "Marakwet", "age": 19}
print(person["name"])

#data structures + algorithms
print(sum(numbers))

watu = [{"name" : "Jamie", "age": 25},
        {"name" : "Maggie", "age": 29},
        {"name" : "croil", "age": 18}]

print(watu[1]["name"])