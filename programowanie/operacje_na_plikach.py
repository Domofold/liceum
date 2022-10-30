plik = open('tekst.txt_1','r')
tablica = plik.readlines()
pliczek = open('tekst.txt_2','w')
for wartość in tablica:
    if int(wartość)==1:
        pliczek.write(str(int(wartość)*1))
        pliczek.write('\n')
    else:
        pliczek.write(str(int(wartość)*int(tablica[int(wartość)-2])))
        pliczek.write('\n')