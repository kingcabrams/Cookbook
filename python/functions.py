def greet_user():
    """"Generic Greeting for users"""
    print("Hello!")
    print("Welcome")


def greet_user_by_name(name="User", greeting="Hello"):
    """""Customized greeting"""
    print(greeting + ", " + name)


def cube(base_number):
    cubed_value = base_number * base_number * base_number
    return cubed_value


greet_user()
greet_user_by_name(input("What is your name? "))
greet_user_by_name()
greet_user_by_name("Cabrams", "Welcome")
greet_user_by_name(greeting="Welcome", name="Cabrams")

eleven_cubed = cube(11)
print(eleven_cubed)
