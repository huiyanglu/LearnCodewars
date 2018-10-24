def dirReduc(arr):
    opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
    rst = []
    for x in arr:
        if rst and rst[-1] == opposite[x]:
            rst.pop()
        else:
            rst.append(x)
    return rst

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
