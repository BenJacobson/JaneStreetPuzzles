nums = [
    0b10011,
    0b00011,
    0b10010,
    0b00001,
    0b00010,
    0b00010,
    0b01100,
    0b00101,
    0b10011,
    0b10101,
    0b01101,
    0b01111,
    0b00100,
    0b00100,
    0b00000,
]

alpha = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(alpha)):
    print(''.join(alpha[(n+i)%len(alpha)] for n in nums))

"scrabblesumoddz"
