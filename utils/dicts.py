coll = {'word1': 'dog', 'word2': 'cat'}
def get_val(coll, key, default='fish'):
    for key_dict, values in coll.items():
        if key == key_dict:
            return values

    if key == '':
        return default

print(get_val(coll, 'word2'))