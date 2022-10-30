def wyszukiwanie_wzorca(wyr, dł_wyr, wzorzec, dł_wzorzec):
   pierwsza_litera_wzorzec = wzorzec[0]

   for i in range(0, dł_wyr):
        if wyr[i] == pierwsza_litera_wzorzec and dł_wyr-i-dł_wzorzec >= 0:
            czy_wzorzec = True
            for j in range(0, dł_wzorzec):
                if wyr[i + j] != wzorzec [j]:
                    czy_wzorzec = False
            if czy_wzorzec:
                return True
   return False


print(wyszukiwanie_wzorca('153351', '450'))