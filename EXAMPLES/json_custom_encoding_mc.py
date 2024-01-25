import json
from datetime import date
from dataclasses import dataclass

@dataclass
class Parrot():  # sample user-defined class (not JSON-serializable)
    name: str
    color: str

@dataclass
class Dog:
    name: str

    def to_json(self):
        return {"name": self.name}

parrots = [  # list of Parrot objects
    Parrot('Polly', 'green'),  #
    Parrot('Peggy', 'blue'),
    Parrot('Roger', 'red'),
]

def encode(obj):  # custom JSON encoder function
    match obj:
        case object() as obj if hasattr(obj, 'to_json'):
            return obj.to_json()
        case date():
            return obj.ctime()  # convert date to string
        case Parrot():
            return {'name': obj.name, 'color': obj.color}  # convert Parrot to dictionary
    return obj  # if not processed, return object for JSON to parse with default parser


data = {  # dictionary of arbitrary data
    'spam': [1, 2, 3],
    'ham': ('a', 'b', 'c'),
    'toast': date(2014, 8, 1),
    'parrots': parrots,
    'dogs': [Dog('Andy'), Dog('Nellie')],
}

# convert Python data to JSON data;
# 'default' parameter specifies function for custom encoding;
# 'indent' parameter says to indent and add newlines for readability
print(json.dumps(data, default=encode, indent=4))
