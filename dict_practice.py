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

my_nums = [1, 2, -1, 3, 1, -1, -2, -2, 0]
zeros_dict = {}
for number in my_nums:
    if -number in my_nums:
        zeros_dict[abs(number)] = [number, -number]
values_list = []
for key, value in zeros_dict.items():
    values_list.append(value)
print(values_list)


