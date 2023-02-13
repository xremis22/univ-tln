def table_log(P):
    Llog = [-1, 0, 1]
    r = len(bin(P)) - 3
    elem = (1 << r) - 3
    j = 0
    while j < elem :
        Llog.append(0)
        j += 1
    i = 1
    exp = 1
    while i < elem + 2:
        exp = multbyalpha(exp,P)
        Llog[exp] = i
        i += 1
    return Llog
