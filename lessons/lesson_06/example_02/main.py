# if __init__.py is empty, then you can import:
import utility

utility.useful.functions.nice_function()
utility.dummy.functions.not_bad("Test string")

# if __init__.py is not empty, then you can import:
from utility import nice_function, not_bad

nice_function()
not_bad("Test string")

# OR
from utility import *

nice_function()
not_bad("Test string")

