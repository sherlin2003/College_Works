dataW = input('Enter data: ')
dataW = [
            int(x) for x in dataW
        ]
m = len(dataW)
r = 1

#finding the value of 'r'
while 2**r < m + r + 1:
    r =r +1 

for i in range(r):
    dataW.insert(2**i - 1, 0)  #inserting 0s at parity bits

for i in range(r):
    j = 2**i
    value = 0
    while j < len(dataW) + 1:
        value += dataW[j - 1]
        if (j + 1) % (2**i) == 0:
            j += 2**i
        j += 1
    dataW[2**i - 1] = value  #changing parity bit values

print('Resulting code word: ' + "".join([str(x) for x in dataW]))
