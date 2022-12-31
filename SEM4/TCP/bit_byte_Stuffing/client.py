test_str = ""

FLAG="01111110"
print("The original string is : " + str(test_str))
res = ''.join(format(ord(i), '08b') for i in test_str)
for i in test_str:
    if 
print("The string after binary conversion : " + str(res))