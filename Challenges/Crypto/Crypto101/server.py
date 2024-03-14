#/usr/bin/python3

import random, os
from secrets import flag


def main():
    secret = int.from_bytes(os.urandom(12), byteorder = 'big')

    for _ in range(10):
        
        rnd = int.from_bytes(os.urandom(12), byteorder = 'big')
        
        if random.randint(0, 1) == 0:
            print(secret & rnd)
        else:
            print(secret | rnd)
            
    guess = int(input('Enter your guess: '))
    
    if guess == secret:
        print('Congratulations, that\'s what you were looking for! ' + flag)
    else:
        print('Nope!')


if __name__ == '__main__':
    try:
        main()
    except:
        pass
