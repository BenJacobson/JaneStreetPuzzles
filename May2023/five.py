nums = [
    0b01101,
    0b01001,
    0b00100,
    0b00100,
    0b01100,
    0b00101,
    0b01100,
    0b00101,
    0b10100,
    0b10100,
    0b00101,
    0b10010,
    0b01111,
    0b00110,
]

alpha = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(alpha)):
    print(''.join(alpha[(n+i)%len(alpha)] for n in nums))

"middleletterof"
