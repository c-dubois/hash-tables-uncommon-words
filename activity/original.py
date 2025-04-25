def uncommon_from_sentences(s1, s2):
    word_list = (s1 + " " + s2).split()
    
    word_dict = {}
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1

    return [word for word in word_dict if word_dict[word] == 1]