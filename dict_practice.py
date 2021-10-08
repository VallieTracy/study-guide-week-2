def without_duplicates(words):
    counter_dict = {}
    for word in words:
        if word in counter_dict:
            counter_dict[word] += 1
        else:
            counter_dict[word] = 1
    
        
    return counter_dict
print(without_duplicates(['Here', 'words', 'is', 'a', 'group', 'of', 'words', 'words']))

# not done, but I have it counting correctly
