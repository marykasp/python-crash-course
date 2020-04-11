glossary = {
  'list': "A collection of ordered items",
  'dictionary': "A collection of key:value pairs",
  'conditional_test': "boolean expression, evaluates operands and returns true or false",
  'string': "represents text, a sequence of characters wrapped in quotations",
  'if-elif-else': "controls logic in program, represents different paths data can take. If a condition is true then the code block will be executed",
  'boolean': "true or false",
  'float': 'decimal point number',
  'logical_operators': "and, or, and not. Compare two boolean expressions",
  'tuple': "immutable list. List of items wrapped in () separated by commas",
  'for_loop': "iterates through items in a list and performs a task on each item. Can also loop through dictionaries"
}

# print(glossary)
# print(glossary['list'])

# print(f"""
# List: {glossary['list']}\n 
# Dictionary: {glossary['dictionary']}\n
# Condtional Tests: {glossary['conditional_test']}\n 
# String: {glossary['string']}\n 
# If Statements: {glossary['if-elif-else']}
# """)

# loop through the dictionary
for key, value in glossary.items():
  print(f"\n{key}: {value}")