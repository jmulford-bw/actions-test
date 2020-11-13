import os

name = os.environ["MY_NAME"]
print(name)
name_2 = name + "lol"
print(name_2)
print(os.environ["MY_NAME"] + "asdf")
print("name comparison")
print(name == "JacobMulford")
