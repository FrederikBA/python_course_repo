import re

with open('addresses.txt') as f:
    addresses = f.read()

name_reg = re.compile(r'\w+')

phone_reg = re.compile(r'\d{2} \d{2} \d{2} \d{2}')

zip_reg = re.compile(r'\d{4}')

zip_city_reg = re.compile(r'\d{4} \w+')

street_reg = re.compile(r'\w+ \d+ ')

names = name_reg.findall(addresses)
phone_numbers = phone_reg.findall(addresses)
zip_codes = zip_reg.findall(addresses)
zip_cities = zip_city_reg.findall(addresses)
streets = street_reg.findall(addresses)


#print(names)
#print(phone_numbers)
#print(zip_codes)
#print(zip_cities)
print(streets)