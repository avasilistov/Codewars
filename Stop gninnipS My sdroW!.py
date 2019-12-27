def spin_words(sentence):
    return ' '.join([wor[::-1] if len(wor) >= 5 else wor for wor in sentence.split()])
