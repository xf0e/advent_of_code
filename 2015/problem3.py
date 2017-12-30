houses = 1

with open("prob3.txt", "r") as ins:
    array = []
    current_pos = [0, 0]
    pos_tulp = (0,0)
    array.append(pos_tulp[:])
    while True:
        c = ins.read(1)
        if c == '>':
            current_pos[1] = current_pos[1] + 1
        elif c == '<':
            current_pos[1] = current_pos[1] - 1
        elif c == 'v':
            current_pos[0] = current_pos[0] - 1
        elif c == '^':
            current_pos[0] = current_pos[0] + 1
        else:
            print("")
        if not c:
            uniq_arr = set(array)
            print(uniq_arr)
            print(len(array), len(uniq_arr))
            break
        pos_tulp = (current_pos[0], current_pos[1])
        array.append(pos_tulp[:])
        #print(current_pos)
