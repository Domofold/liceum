#zadanie 1
#def ile_opakowan(masa):
#    opakowania = [2,1,15,5]
#    liczba_opakowań = 0
#    while masa > 0:
#        masa_opakowania = 0
#        for opakowanie in opakowania:
#            if opakowanie <= masa and masa_opakowania < opakowanie:
#                masa_opakowania = opakowanie
#        masa -= masa_opakowania
#        liczba_opakowań += 1
#    return liczba_opakowań
#print(ile_opakowan(68))

#zadanie 2
#def minimalna_liczba_opakowan(tablica, masa):
#    liczba_opakowan = 0
#    pozostala_masa = masa
#    while pozostala_masa > 0:
#        for opakowanie in tablica:
#            while pozostala_masa - opakowanie > 0:
#                liczba_opakowan += 1
#                pozostala_masa -= opakowanie
#        if masa > 0:
#            liczba_opakowan +=1
#            pozostala_masa = 0
#    return liczba_opakowan
#print(minimalna_liczba_opakowan([7, 4, 2], 68))
