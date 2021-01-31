
def get_input():
    with open('input.txt') as f:
        commands = []
        for line in f:
            line=line.strip()
            if line.find('mask') >= 0:
                mask = line.split(' ')[2]
            else:
                register = line.split(' ')[0]
                register = register[4:]
                register = int(register.replace(']',''))

                val = int(line.split(' ')[2])
                commands.append([mask, register, val])
        return commands

def initialize_bitmap():
    bitmap = '000000000000000000000000000000000000'
    #return bitmap
    array = []
    for b in bitmap:
        array.append(int(b))
    return array

def apply_memcopy(bitmap, mask):
    index = 0
    all_options = {}

    for m in mask:
        if m == '1':
            bitmap[index] = '1'
        if m == '0':
            bitmap[index] = '0'
        index +=1
    return bitmap

def apply_bitmask(bitmap, mask):
    index = 0
    for m in mask:
        if m == '1':
            bitmap[index] = '1'
        if m == '0':
            bitmap[index] = '0'
        index +=1
    return bitmap

def convert_to_binary(val):
    bit_rep = '{0:b}'.format(val)
    for i in range(0,36-len(bit_rep)):
        bit_rep = '0{0}'.format(bit_rep)
    return bit_rep

def convert_to_string(bit_array):
    string = ''
    for b in bit_array:
        string = '{0}{1}'.format(string,b)
    return string

commands = get_input()
registers = {}
for com in commands:
    print(com)
    reg = com[1]
    if reg not in registers:
        registers[reg] = initialize_bitmap()
    bit_rep = convert_to_binary(com[2])
    registers[reg] = apply_bitmask(registers[reg], bit_rep)
    registers[reg] = apply_bitmask(registers[reg], com[0])
sum = 0
for r in registers.values():
    val = convert_to_string(r)
    sum += int(val, 2)
    print(val, int(val,2))
print(sum)





