s1 = [  212, 232, 167, 254, 232, 242, 160, 245, 226, 167, 
  224, 232, 232, 227, 167, 230, 243, 167, 243, 239, 
  238, 244, 167, 216, 197,   0]
s2 = []

# for i in range(len(s1) - 2):
#     s1[i] = s1[i] ^42
#     # print(chr(s1[i]), end="")
# string = "So you're good at this uh"
# for i in range (len(string)):
#     print(ord(string[i])^s1[i])
# print()
# stirng_list = []
# for i in range(len(string)):
#     stirng_list.append(ord(string[i]) ^0x42
for  i in range(len(s1)):
    s1[i] = s1[i] ^ 0xad
for i in range(len(s1) - 3):
    s1[i] = s1[i] ^ 42
for i in s1:
    print(chr(i), end="")
print()

ans = ["ad", "42", "68", "84", "00", "6a"]
print("".join(ans))
# ad4268846b6b

'''
ad426885006a
0 ad - 
1 42  -
2 68 -
3 84 - 
4 00 
5 6a
'''