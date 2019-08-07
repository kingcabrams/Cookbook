import os

# Get OS name and environment vars
#print(os.name)
#print(os.environ) 

# Get and change directories
print(os.getcwd())
os.chdir("./")
print(os.getcwd())

# Get file sizes and folder contents
print(os.path.getsize("os_funcs.py"))
print(os.listdir("./"))

# Check path validity
print(os.path.exists("os_functions.py"))
print(os.path.exists("os_funcs.py"))
os.chdir("../")
print(os.path.exists("os"))

# Execute commands
os.system("ls")

