with open("box.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)
big_surface = 0
for wl in array:
    wl = wl.split('x')
    wl = [ int(x) for x in wl]
    surface = 2 * wl[0] * wl[1] + 2 * wl[1] * wl[2] + 2 * wl[2] * wl[0]
    wl = sorted(wl)
    small_side = wl[0] * wl[1]
    big_surface = big_surface + surface + small_side

print(big_surface)
        
