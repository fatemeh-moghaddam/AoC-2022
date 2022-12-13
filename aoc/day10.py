with open("day10.txt", "rt") as input_file:
    program = [line.strip() for line in input_file]


def sigread(program):
    cycle = 1
    x = 1
    for instr in program:
        yield x, cycle
        if instr != 'noop':
            cycle += 1
            yield x, cycle
            [instr, value] = instr.split("addx ")
            x += int(value)
        cycle += 1
        


def tube(program):
    signals = [i+20 for i in range(240, 0, -40)]
    lines = [i for i in range(40, 280, 40)]
    line = 0
    strength = []
    signal = 20
    CRT = ''
    for x, cycle in sigread(program):
        CRT_pos = (cycle-1) - line 
        if CRT_pos >= x-1 and CRT_pos <= x+1: 
            CRT += '#'
        else:
            CRT += '.'
        if cycle == signal:
            strength.append(x*signal)
            signal = signals.pop()
        if cycle % 40 == 0 and cycle >= 40:
            CRT += '\n'
            line = lines.pop(0)
        if len(lines) == 0:
            return sum(strength), CRT


strength, CRT = tube(program)

print(f"{strength=}")
print(CRT)

