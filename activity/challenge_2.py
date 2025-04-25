def uncommon_from_sentences(sentences):

    sentence_dict = {}
    for sentence in sentences:
        sentence_dict[sentence] = sentence.split()
    
    word_list = []
    word_in_sentences = None
    for sentence, sentence_list in sentence_dict.items():
        for word in sentence_list:
            word_in_sentences = False
            for sentence1, sentence_list1 in sentence_dict.items():
                if sentence != sentence1:
                    if word in sentence_list1:
                        word_in_sentences = True
            if not word_in_sentences:
                word_list.append(word)


    return list(set(word_list))

