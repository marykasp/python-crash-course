def make_shirt(size, message):
  print(f"The size of the shirt you requested is a {size} and the message says '{message}''")

# positional arguments - have to enter arguments in the same order as the parameters
make_shirt('small', 'Bad ass bitch')

# keyword arguments- give the arguments a name-value pair, can be in any order
make_shirt(size="large", message="WFH")