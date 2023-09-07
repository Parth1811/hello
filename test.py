import re 


f = open("data.txt", "r")
lines = [x.split('\n')[0] for x  in f.readlines()]

regex = "(\\DS|\\DE|\\DO|\\DT|\\TSE|\\TSO|\\TST|\\TTO|\\TTT|\\LL|\\SN|\\WLX|\\WLZ|\\EQZ|\\EQX|\\DI|\\WLIX|\\WLIZ)"
param = ["DS","DE","DO","DT","TSE","TSO","TST","TTO","TTT","LL","SN","WLX","WLZ","EQZ","EQX","DI","WLIX","WLIZ"]
slm = []

for equation in lines:
    terms = re.split("([\\+|\\-][0-9A-z.]*)", equation)
    mp = { x:0 for x in param}
    for term in terms:
        if term == "" or term == None:
            continue
        num, var, _ = re.split("([A-Z]+)", term)
        mp[var.upper()] = float(num)
    slm.append(mp)
    
print(slm)
l = []
result = "Ultimate,"
for p in param:
    result += p + ','

l.append(result + "\n")

for i in range(len(lines)):
    result = lines[i] + ','
    for p in param:
        result += str(slm[i][p]) + ','

    result += '\n'
    l.append(result)

fr = open("data.csv", 'w')
fr.writelines(l)

fr.close()
f.close()