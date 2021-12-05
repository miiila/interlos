
dot = '⋅'
ddot = '∶'
tdot = '⋮'

numbers = ['⋅', '∶', '⋮', '∶⋮', '∶∶', '∶⋅', '⋮⋅', '⋮∶', '⋮⋮', '∶⋮⋮', '∶⋮∶', '∶⋮⋅', '∶∶⋅', '∶∶∶', '∶∶⋮', '∶⋅⋮', '∶⋅∶', '∶⋅⋅', '⋮⋅⋅', '⋮⋅∶', '⋮⋅⋮', '⋮∶⋮', '⋮∶∶', '⋮∶⋅','⋮⋮⋅', '⋮⋮∶','⋮⋮⋮']

# numbers = ['⋅', '∶', '⋮', '∶⋮', '∶∶', '∶⋅', '⋮⋅', '⋮∶', '⋮⋮']

def generate(a, width):
    c = a[:]
    for i in range(len(c)):
        while len(c[i]) < width:
            c[i] = dot + c[i]

    b = c[:]
    b.reverse()
    b = list(map(lambda x: ddot +x, b))
    c = list(map(lambda x: tdot +x, c))

    res = []
    res +=a
    res +=b
    res +=c

    return res

r = False

level = 3
while not r:
    numbers = generate(numbers, level)
    level +=1
    try:
        r = numbers.index('⋮⋮⋅∶⋅⋅⋮⋅∶∶⋅⋮∶⋅∶')
    except:
        pass

print(r)

