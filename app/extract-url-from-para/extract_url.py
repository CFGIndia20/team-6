import re

def extract(text):
    """
    input: String 
    output: list of urls
    """
    url = re.findall(r'https:\/\/www.google.com\/maps\/.*', text)
    lat = re.findall(r'\@(-?[\d\.]*)',url[0])
    lon = re.findall(r'\@[-?\d\.]*\,([-?\d\.]*)',url[0])
    print(lat)
    print(lon)
    return url

print(extract("the link to the location is https://www.google.com/maps/place/Charai+Hindu+Samshaan+Bhoomi/@19.0492292,72.8922557,18z/data=!4m5!3m4!1s0x3be7c8a8d4029427:0x991bade397542b3a!8m2!3d19.049521!4d72.8932652"))
"""
Eg -
print(extract("the link to the location is https://goo.gl/maps/gaH6HQDWLjuULTPv6 "))

o/p - ['https://goo.gl/maps/gaH6HQDWLjuULTPv6']
"""