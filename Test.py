anfrage = float(raw_input('Wurzel aus: '))
#s = float(raw_input('Schaetzwert: '))
s = anfrage
#a = float(raw_input('Maximale Abweichung: '))
a = 1.0/10000000

counter = 0

while counter < 10000 and abs(s*s-anfrage) > a:
    counter += 1
    s = 0.5*(s+anfrage/s)
    print('Durchgang ' + str(counter))
    print('s = ' + str(s))

print('Die Wurzel aus ' + str(anfrage) + ' = ' + str(s))
print(str(s*s))