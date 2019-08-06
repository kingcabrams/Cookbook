"""Local Variables Cannot Be Used in the Global Scope"""
def spam():
    eggs = 31337


spam()
print(eggs)  # Yields an error eggs only exists in local scope

"""Local Scopes Cannot Use Variables in Other Local Scopes"""
def spam():
    eggs = 99
    bacon()
    print(eggs)  # bacon() does not change local variable

def bacon():
    ham = 101
    eggs = 0


spam()

"""Global Variables Can Be Read from a Local Scope"""
def spam():
    print(eggs)

eggs = 42


spam()

"""Local and Global Variables can Have the Same Name"""
def spam():
    eggs = 'spam local'
    print(eggs)  # prints 'spam local'

def bacon():
    global eggs
    spam()
    print(eggs)  # prints 'global'

eggs = 'global'
bacon()
print(eggs)  # prints 'global'
