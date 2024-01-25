#
from jsonpickle import encode
from jsonpickle_classes import Wombat, Yeti

# make a list of 5 Wombats and 5 Yetis
data = (
    [Wombat(i) for i in range(1, 6)]
    +
    [Yeti(i) for i in range(1, 6)]
)

encoded_json = encode(data)
with open('beasts.json', 'w') as beasts_out:
    beasts_out.write(encoded_json)
