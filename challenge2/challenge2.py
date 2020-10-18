# Found string of chars in inspect element
# Asked to find "rare" ones

from collections import Counter


with open('challenge2.txt', 'r') as file:
    data = file.read().replace('\n', '')

chars = Counter(data)
print(chars)
# Output: Counter({')': 6186, '@': 6157, '(': 6154, ']': 6152, '#': 6115, '_': 6112, '[': 6108, '}': 6105, '%': 6104, \
# '!': 6079, '+': 6066, '$': 6046, '{': 6046, '&': 6043, '*': 6034, '^': 6030, 'e': 1, 'q': 1, 'u': 1, 'a': 1, 'l': 1, \
# 'i': 1, 't': 1, 'y': 1})

# Thus, the URL is print("http://www.pythonchallenge.com/pc/def/___.html")
print("http://www.pythonchallenge.com/pc/def/equality.html")

# Now you can go to http://pythonchallenge.com/pcc/def/equality.html to view solution to level 2 on the wiki