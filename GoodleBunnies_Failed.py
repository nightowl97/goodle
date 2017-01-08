test = [3, 1, 4, 1, 5, 9]

# Construct int from list
def makeint(l):
    if len(l) > 0:
        return int(''.join(map(str, l)))
    else:
        return 0


def answer(l):
    """
    If (sum of digits) mod 3 is 0, reverse sort the list and
    return the digit from it.
    If (sum of digits) mod 3 is 1, remove smallest digit whose
    mod of 3 is 1, if unavail, remove 2 smallest digits whose
    mod of 3 is 2, if unavail, number is impossible.
    If sum of digits mod 3 is 2, inverse of previous case.
    """
    res = sorted(l, key=int, reverse=True)
    s = sum(res)
    rem1list = sorted([i for i in res if i % 3 == 1], key=int)
    rem2list = sorted([i for i in res if i % 3 == 2], key=int)

    if s % 3 == 0:
        return makeint(res)

    elif s % 3 == 1:
        if not rem1list and len(rem2list) < 2:
            return 0
        elif not rem1list:
            res.remove(rem2list[0])
            res.remove(rem2list[1])
            return makeint(res)
        else:
            res.remove(rem1list[0])
            return makeint(res)
    elif s % 3 == 2:
        if not rem2list and len(rem1list) < 2:
            return 0
        elif not rem2list:
            res.remove(rem1list[0])
            res.remove(rem1list[1])
            return makeint(res)
        else:
            res.remove(rem2list[0])
            return makeint(res)

print answer(test)