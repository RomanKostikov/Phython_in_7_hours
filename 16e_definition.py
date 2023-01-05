def count_list(par, par2 = False, count = 0 ): #parametr
    if par2 == True:
        typ = type(par[0])
        for i in par:
            count += 1
        return count, typ

    else:
        for i in par:
            count += 1
        return count


j = [9, 8, 7, 6]
h, p = count_list(j, True) #argument
