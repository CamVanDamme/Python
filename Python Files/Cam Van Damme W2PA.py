# Cam Van Damme

# Use variables for repeated pieces and not for single use lines
connector = '- + -'
body = '| | |'
legs = '|   |'
indent = '     '

# Create a function for printing the body
def print_body():
    print(indent + body)
    print(indent + body)
    print(indent + body)
    print(indent + body)
    
# Create a function for printing the legs
def print_legs():
    print(indent + legs)
    print(indent + legs)

# Create a function to print our parrot
def print_parrot():
    print('-----* ||')
    print(indent + '  +')
    print(indent + connector)
    print_body()
    print(indent + connector)
    print_legs()
    print('    --   --')

# Run the function to print our parrot
print_parrot()