text_messages = ['brb', 'hey there', 'how is life?']
sent_messages = []

def show_message(texts):
  while texts:
    current_message = texts.pop()
    print(current_message)
    sent_messages.append(current_message)

# pass a copy of the list to the function
show_message(text_messages[:])
# original list is unchanged
print(text_messages)
print(sent_messages)