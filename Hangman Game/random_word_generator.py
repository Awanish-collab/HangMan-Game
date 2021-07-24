from random import randint
def random_word_selector():
    word_list = ['above','about','awanish','kumar','galgotias', 'university','brajesh']
    selected_index = randint(0,len(word_list)-1)
    return word_list[selected_index]

#print(random_word_selector())
