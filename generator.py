import random
import time
import os

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

num1 = int(input('Enter the number of generated links:'))
len = 16
for n in range(num1):
    link = ''
    for i in range(len):
        link += random.choice(chars)
    with open ('links.txt', 'a') as file:
        print(link, file=file)
