
singles = {
    1: 'jedna',
    2: 'dva',
    3: 'tri',
    4: 'ctyri',
    5: 'pet',
    6: 'sest',
    7: 'sedm',
    8: 'osm',
    9: 'devet',
}

doubles = {
    10: 'deset',
    11: 'jedenact',
    12: 'dvanact',
    13: 'trinact',
    14: 'ctrnact',
    15: 'patnact',
    16: 'sestnact',
    17: 'sedmnact',
    18: 'osmnact',
    19: 'devatenact',
    20: 'dvacet',
    30: 'tricet',
    40: 'ctyricet',
    50: 'padesat',
    60: 'sedesat',
    70: 'sedmdesat',
    80: 'osmdesat',
    90: 'devadesat',
}

doubless = {
    2: 'dvacet',
    3: 'tricet',
    4: 'ctyricet',
    5: 'padesat',
    6: 'sedesat',
    7: 'sedmdesat',
    8: 'osmdesat',
    9: 'devadesat',
}

triples = {
    1: 'sto',
    2: 'dve ste',
    3: 'tri sta',
    4: 'ctyri sta',
    5: 'pet set',
    6: 'sest set',
    7: 'sedm set',
    8: 'osm set',
    9: 'devet set',
}

tripless = {
    100: 'jedno sto',
    200: 'dve ste',
    300: 'tri sta',
    400: 'ctyri sta',
    500: 'pet set',
    600: 'sest set',
    700: 'sedm set',
    800: 'osm set',
    900: 'devet set',
}
triplesss = {
    100: 'sto',
    200: 'dve ste',
    300: 'tri sta',
    400: 'ctyri sta',
    500: 'pet set',
    600: 'sest set',
    700: 'sedm set',
    800: 'osm set',
    900: 'devet set',
}

quadr = {
    1: 'jeden tisic',
    2: 'dva tisice'
}

quadrs = {
    1000: 'jeden tisic',
    2000: 'dva tisice'
}

def wordNum(num):
    word = ''
    t = quadrs.get(num)
    if t:
        word = t+" "+word
        return word
    t = tripless.get(num)
    if t:
        word = t+" "+word
        return word
    t = doubles.get(num%100)
    if t:
        word = t + " "+word
        # num = num//100
    else:
        i = num%10
        if i > 0:
            word = singles[i]+" "+word
        if num >20: 
            i = (num//10)%10
            if i > 0:
                word = doubless[i]+" "+word
    if num >99: 
        t = triplesss.get(num%100)
        if t:
            word = t + word
            # num = num//100
        else:
            i = (num//100)%10
            if i > 0:
                word = triples[i]+" "+word
    if num >999: 
        i = (num//1000)
        if i > 0:
            word = quadr[i]+" "+word


    return word

wordsD = {} 
wordsL = [] 
for i in range(2619):
    if i == 0: 
        continue

    n = wordNum(i)
    wordsL.append(n)
    wordsD.update({i: n})


wordsL.sort()

j = 1
res = ''
for w in wordsL:
    print(j,w, wordsD[j])
    if w == wordsD[j]:
        res += str(j)
    j+=1

print(res)

