# Surround top-level functions and classes with two blank lines
class MyFirstClass:
    pass


class MySecondClass:
    pass


def top_level_function():
    return None


# Surround method definitions inside classes with a single blank line
class MyClass:
    def first_method(self):
        return None

    def second_method(self):
        return None


# Use blank lines sparingly inside functions to show clear steps
# 79 characters Maximum Line Length
# Python will assume line continuation if code is contained
def function(arg_one, arg_two,
             arg_three, arg_four):
    return arg_one
# break lines before binary operators
# Recommended
first_variable, second_variable, third_variable = 0
total = (first_variable
         + second_variable
         - third_variable)

# Indentation
    # Use 4 consecutive spaces to indicate indentation.
		# Prefer spaces over tabs.

# Indentation Following Line Breaks
    #  align the indented block with the opening delimiter
def functionx(arg_one, arg_two,
             arg_three, arg_four):
    return arg_one

# When only 4 spaces are needed to align with the opening delimiter
# add some additional 4 spaces extra indentation.
x = 5
if (x > 3 and
        x < 10):
    print(x)

# Hanging indents must avoid arguments on the first line
arg_one = arg_two = arg_three = arg_four = 0
var = function(
    arg_one, arg_two,
    arg_three, arg_four)
    # keep the closing parenthesis
    #... whith the last element

# When using a hanging indent double indent to distinguish
 # from following block code
def function(
        arg_one, arg_two,
        arg_three, arg_four):
    return arg_one

# Line up the closing brace to the previous line
list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
    ]


# Limit the line length of comments and docstrings to 72 characters!!
#_______________________________________________________________________
#______________________________________________________________________________

# Indent block comments to the same level as the code they describe.
# Separate paragraphs by a line containing a single #.
def quadratic(a, b, c, x):
    # Calculate the solution to a quadratic equation using the quadratic
    # formula.
    #
    # There are always two solutions to a quadratic equation, x_1 and x_2.
    x_1 = (- b+(b**2-4*a*c)**(1/2)) / (2*a)
    x_2 = (- b-(b**2-4*a*c)**(1/2)) / (2*a)
    return x_1, x_2


# Separate inline comments by two or more spaces from the statement.
# Avoid them whenever possible.
x = 5  # This is an inline comment

# Multiline docstrings ends on a single line just for the """ token.
def quadratic2(a, b, c, x):
    """Solve quadratic equation via the quadratic formula.

    A quadratic equation has the following form:
    ax**2 + bx + c = 0

    There always two solutions to a quadratic equation: x_1 & x_2.
    """
    x_1 = (- b+(b**2-4*a*c)**(1/2)) / (2*a)
    x_2 = (- b-(b**2-4*a*c)**(1/2)) / (2*a)

    return x_1, x_2


# white spaces surround the following binary operators on each side:
# =, +=, -=, ==, !=, >, <. >=, <=, is, is not, in, not in, and, not, or
# + - * / // % **
# : (as binary operator in slices)

# Exceptions: default parameters assignments or higher priority ops.
def functiony(x=5):
    y = x ** 2 + 5
    z = (x+y) * (x-y)
    if x>5 and x%2 == 0:
        my_list = [0, 1, 2, 3, 4, 5, 6, 7]
        x = my_list[3:4:5]
        y = my_list[x+1 : x+2 : x+3]


# Avoid invisible trailing whitespace at the end of the line
# also avoid spacing between a trailing comma and a closing parenthesis:
tuple = (1,)  # OK

# Do not align assignment operators:
# Recommended
var1 = 5
var2 = 6
some_long_var = 7

# Not recommended
var1_          = 5
var2_          = 6
some_long_var_ = 7

# Take advantage of falsy values except for None values
my_list = []
if not my_list:
    print('List is empty!')
if x is not None:  # Avoid 'if not x is None:'
    pass # Do something with arg...
# Recommended
if 'whatever'.startswith('cat'):  # Avoid "if word[:3] == 'cat':"
    print('The word starts with "cat"')


