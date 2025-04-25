def uncommon_from_sentences(sentences):
    word_list = []
    for sentence in sentences:
        word_list.extend(sentence.split())

    word_dict = {}
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1

    return [word for word in word_dict if word_dict[word] == 1]
