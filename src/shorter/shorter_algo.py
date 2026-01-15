# inplementation de l'algorithme pour
# shoter les url
import random


def strip_char(s : str) -> list:
    s = [char for char in s]
    return [ c for c in s if c.isalpha()]

def shorter_algo(url:str) -> str:
    new_url = ''
    url = strip_char(url.strip())
    for i in range(0,6):
        new_url += url[random.randint(0,(len(url)-5))]
    return new_url

print(shorter_algo('https://github.com/femiojoawo/miny-shorter-url.git'))
