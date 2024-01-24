d1 = dict()   # empty dict
d2 = {'a': 10, 'm': 42, 'c': 15}
d3 = {}   # empty dict

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

print(f"{airports['RDU'] = }")
print(f"{airports['YCC'] = }")

airports['MSP'] = "Minneapolis"
print(f"{airports = }\n")

airports['AUS'] = "Austin"
print(f"{airports = }\n")

del airports['MCI']
print(f"{airports = }\n")

# print(f"{airports['DIA'] = }\n")
print(f"{airports.get('DIA') = }\n")
print(f"{airports.get('DIA', 'Not Found') = }\n")

print(f"{airports.setdefault('DIA', 'Denver') = }\n")
print(f"{airports = }\n")

print(f"{airports.keys() = }\n")
print(f"{airports.values() = }\n")

for code, city in airports.items():
    print(code, city)
print()











