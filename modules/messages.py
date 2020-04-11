

def show_message(texts, sent_messages):
  while texts:
    current_message = texts.pop()
    print(current_message)
    sent_messages.append(current_message)

