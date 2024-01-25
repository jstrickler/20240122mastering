#
from jsonpickle import decode

TEST_STRING = 'weasel yeti wombat gopher'

with open('beasts.json') as beasts_in:
    encoded_json = beasts_in.read()

decoded_json = decode(encoded_json)

for x in decoded_json:
    print(x.id)
    print(x.date)
    print(x.rx.search(TEST_STRING))
    print(x.listclass.some_list)
    print(x.dictclass.some_dict)
    print('=' * 60)

print()
