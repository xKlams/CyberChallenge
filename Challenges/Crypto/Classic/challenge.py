
from string import ascii_lowercase
import random
from secrets import flag

mapping = {}

alphabet     = list(ascii_lowercase)
substitution = alphabet[::]
random.shuffle(substitution)

for i in range(len(alphabet)):
    mapping[alphabet[i]] = substitution[i]
    
    
    
result = ""

for char in flag:
    if char in mapping:
        result += mapping[char]
    else:
        result += char
        
print(result)
    


