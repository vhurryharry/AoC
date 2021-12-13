
with open('2.in') as infile:
    input = infile.read()

x = list(map(str, input.split()))

aim = 0
depth = 0
horizontal = 0

ddepth = 0
dhorizontal = 0

for dir in x:
    if dir == 'forward':
        ddepth = 0
        dhorizontal = 1
    elif dir == 'up':
        ddepth = -1
        dhorizontal = 0
    elif dir == 'down':
        ddepth = 1
        dhorizontal = 0
    else:
        aim += ddepth * int(dir)
        if(dhorizontal == 1):
            depth += aim * int(dir)
        horizontal += dhorizontal * int(dir)

print(depth * horizontal)
