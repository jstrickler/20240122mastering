from pprint import pprint
import sys
import requests
import re


BASE_URL = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'

with open('dictionaryapikey.txt') as apikey_in:
    API_KEY = apikey_in.read().rstrip()

def main(args):
    if len(args) < 1:
        print("Please specify a search term")
        sys.exit(1)

    response = requests.get(
        BASE_URL + args[0],
        params={'key': API_KEY},
    )

    if response.status_code == requests.codes.OK:
        words = []  # list of Word objects
        data = response.json()
        for entry in data:
            if isinstance(entry, dict):
                meta = entry.get("meta")
                if meta:
                    word_name = meta.get("id")
                    print("word_name:", word_name)
                    if "shortdef" in entry:
                        word_definition = '\n'.join(entry['shortdef'])
                    else:
                        word_definition = None

                    def init(self, name, definition):
                        self._name = name
                        self._definition = definition

                    name_prop = property(lambda self: self._name)
                    def_prop = property(lambda self: self._definition)

                    word = type(clean_word(word_name), (), {'__init__': init, 'definition': def_prop, 'name': name_prop})


                    words.append(word(word_name, word_definition))
    else:
        print("Sorry, HTTP response", response.status_code)

    for word in words:
        print(f"{word.name.upper()}:\n{word.definition}\n")

def clean_word(w):
    return re.sub(r"\W+", "_", w)



if __name__ == '__main__':
    main(sys.argv[1:])
