nums = [
    0b01100,
    0b01111,
    0b01110,
    0b00111,
    0b00101,
    0b10010,
    0b10100,
    0b01000,
    0b00001,
    0b01110,
    0b00110,
    0b01001,
    0b10110,
    0b00101,
]

alpha = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(alpha)):
    print(''.join(alpha[(n+i)%len(alpha)] for n in nums))

"longerthanfive"
