def do_potegi(podstawa, wykladnik):
    if wykladnik == 0:
        return 1
    if wykladnik % 2 == 0:
        a = do_potegi(podstawa, wykladnik/2)
    else:
        return podstawa * do_potegi(podstawa,wykladnik - 1)
    return a*a
