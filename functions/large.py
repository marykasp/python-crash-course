def make_shirt(size="large", message="I love python"):
  print(f"The size of shirt you requested is a {size} with the message '{message}'.")

# no arguments passed- the default values will be used
make_shirt()

make_shirt("medium")
make_shirt("small", "I love Javascript")