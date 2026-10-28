#functions
import random
# a=append w= write
#from my_functions import greet()

import my_functions

with open("data.txt", "w") as file:
     # file.write("99\n")
     #  file.write("53\n")
      for temp in range(100):
          x = random.randint(-10, 65)
          file.write(str(x)+"\n")

with open("data.txt", "r") as file:

    content = file.read() # 0 parameter 0 argument
    print(content)

 my_functions.greet()