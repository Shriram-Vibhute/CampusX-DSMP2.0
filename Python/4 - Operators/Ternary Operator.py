# Using a ternary operator to assign a value to 'name'
name = 'Dexter' if type('Dexter') is str else 'Sam'

# Print the value of 'name'
print(name)

# Explanation of the ternary operator:
# The ternary operator is a shorthand for an 'if-else' statement. 
# Syntax: <value_if_true> if <condition> else <value_if_false>
# In this example:
# - The condition is 'type('Dexter') is str'
# - If the condition is True (which it is, because 'Dexter' is a string), 'name' is assigned 'Dexter'
# - If the condition were False, 'name' would be assigned 'Sam'