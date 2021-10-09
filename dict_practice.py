def without_duplicates(words):
    # counter_dict = {}
    # for word in words:
    #     if word in counter_dict:
    #         counter_dict[word] += 1
    #     else:
    #         counter_dict[word] = 1
    # no_dupes_list = []
    # for key in counter_dict:
    #     if counter_dict.values() != 1:
    #         no_dupes_list.append(key)
    # return no_dupes_list
    return list(set(words))
     
#print(without_duplicates(['bee', 'bee', 'bumblebee']))

# def find_unique_common_items(items1, items2):

#     return set(items1) & set(items2)

# print(find_unique_common_items(['apple', 'sad', 'happy'], ['sad', 'window']))

# my_nums = [1, 2, -1, 3, 1, -1, -2, -2, 0]
# zeros_dict = {}
# for number in my_nums:
#     if -number in my_nums:
#         zeros_dict[abs(number)] = [number, -number]
# values_list = []
# for key, value in zeros_dict.items():
#     values_list.append(value)
# print(values_list)

# def top_chars(phrase):
#     init_dict = {}
#     for item in phrase:
#         if item != ' ':
#             if item in init_dict:
#                 init_dict[item] += 1
#             else:
#                 init_dict[item] = 1
#     highest_value = max(init_dict.values())
#     answers_list = []
#     for key, value in init_dict.items():
#         if value == highest_value:
#             answers_list.append(key)
#     return sorted(answers_list)


        
# print(top_chars('za stzring! ssz'))

# phrase = "hello there"
# phrase_list = []
# words = phrase.split(' ')
# print(words)
# print(type(words))


ENG_PIRATE_LOOKUP = {
    "sir": "matey",
    "hotel": "fleabag inn",
    "student": "swabbie",
    "man": "matey",
    "professor": "foul blaggart",
    "restaurant": "galley",
    "your": "yer",
    "excuse": "arr",
    "students": "swabbies",
    "are": "be",
    "restroom": "head",
    "my": "me",
    "is": "be",
}


def translate_to_pirate_talk(phrase):
    words_list = phrase.split(' ')
    new_phrase = ''
    for word in words_list[:-1]:
        if word in ENG_PIRATE_LOOKUP:
            word = "needs to change "
            new_phrase += word
        else:
            new_phrase += word
    for word in words_list[-1]:
        if word in ENG_PIRATE_LOOKUP:
            word = "needs to change "
            new_phrase += 'word'
        else:
            new_phrase += word 
    return new_phrase

print(translate_to_pirate_talk('sir testing swabbies'))
