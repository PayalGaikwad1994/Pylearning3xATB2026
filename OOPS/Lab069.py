#filter to find vowels

mylist=["a","b","c","d","e","f","g","h","i","j"]
print(mylist)

def find_vowel(val):
    return val in ["a","e","i","o","u"]

list_vowel=filter(find_vowel,mylist)
print(list(list_vowel))