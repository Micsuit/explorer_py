import os
from explorer_commands import *

while True:
    user_input = input(os.getcwd() + "> ")

    run(user_input)