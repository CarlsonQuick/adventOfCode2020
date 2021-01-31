class Instruction():


    def __init__(self, command, direction,count):
        self.command = command
        self.direction =direction
        self.count = count

    def __str__(self):
        return '{0} {1}{2}'.format(self.command, self.direction, self.count)
    def __repr__(self):
        return self.__str__()
def parse(line):
    parsed = line.split(' ')
    command = parsed[0]
    direction = parsed[1][0]
    count  =  int(parsed[1][1:len(parsed[1])-1])
    return Instruction(command, direction, count)


def run_program(inst_set):
    sum = 0
    visited = [False for f in range(0,len(inst_set))]
    pointer = 0
    while pointer < len(visited) and visited[pointer] != True:
        inst = inst_set[pointer]
        visited[pointer] = True
        if inst.command == 'nop':
            pointer+=1
        elif inst.command == 'acc':
            if inst.direction == '+':
                sum += inst.count
            else:
                sum -= inst.count
            pointer +=1
        else:
            if inst.direction == '+':
                pointer += inst.count
            else:
                pointer -= inst.count
    print(sum, pointer)
    if pointer >= len(visited):
        return True
    else:
        return False

with open('input.txt') as f:
    base_instructions = list()
    for instruction in f:
        base_instructions.append(parse(line=instruction))

    changed_pointer = 0


    exited = False
    while exited == False:
        copied_inst = [Instruction(inst.command, inst.direction, inst.count) for inst in base_instructions]
        changed = False
        while changed == False:
            if copied_inst[changed_pointer].command == 'nop':
                copied_inst[changed_pointer].command = 'jmp'
                print('changing line ', changed_pointer, copied_inst[changed_pointer])
                changed = True
            elif copied_inst[changed_pointer].command == 'jmp':
                copied_inst[changed_pointer].command = 'nop'
                print('changing line ', changed_pointer, copied_inst[changed_pointer])
                changed = True
            changed_pointer +=1
        exited = run_program(copied_inst)


