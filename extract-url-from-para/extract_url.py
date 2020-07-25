import re

def extract(text):
    """
    input: String 
    output: list of urls
    """
    url = re.findall(r'https:\/\/goo\.gl\/maps\/.*', text)
    return url

"""
Eg -
print(extract("the link to the location is https://goo.gl/maps/gaH6HQDWLjuULTPv6 "))

o/p - ['https://goo.gl/maps/gaH6HQDWLjuULTPv6']
"""