import json
from pprint import pprint

with open('DATA/presidents.json') as pres_in:
    pres_data = json.load(pres_in)

pprint(pres_data)
print()

for president in pres_data['presidents']:
    print(president['lastname'], president['birthstate'])

with open('potus.json', 'w') as potus_out:
    json.dump(pres_data['presidents'], potus_out)





