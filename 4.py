with open('anna_words.txt', encoding="utf-8") as file:
    text = file.read().lower()
    words = text.split()
    unique_words = set(words)
    word_freq={}
    for word in unique_words:
        word_freq[word] = words.count(word)
        for word, freq in word_freq.items():
            print(freq, word)