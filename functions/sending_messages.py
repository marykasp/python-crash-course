text_messages = ['brb', 'hey there', 'how is life?']
sent_messages = []

def show_message(texts):
  while texts:
    current_message = texts.pop()
    print(f"Current message: {current_message}")
    sent_messages.append(current_message)

show_message(text_messages)
print(text_messages)
print(sent_messages)