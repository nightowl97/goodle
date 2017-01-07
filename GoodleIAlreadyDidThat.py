"""
Goodle Challenge: get length of the cycle that inevitably results from the
following algorithm:
take a number n in base b, k is the length of n. Output z = x - y where x is the
digits of n in descending order and y is the digits of n in ascending order.
z is also in base b and keeps the length k by keeping any leading zeros.
"""


def answer(n, b):
    def iterate(num, ba):  # Gets next iteration
        k = len(num)
        x = int(''.join(sorted(num, key=str, reverse=True)), base=ba)
        y = int(''.join(sorted(num, key=str)), base=ba)
        z = x - y

        zrep = []
        while z > 0:  # Get representation of z in base b
            zrep.insert(0, str(z % ba))
            z = z // ba

        return ((k - len(zrep)) * '0') + ''.join(zrep)

    l = []
    while True:  # fill list until next iteration already exists there
        if len(l) == 0:
            l.append(n)
        elif iterate(l[-1], b) not in l:
            l.append(iterate(l[-1], b))
        else:
            ind = l.index(iterate(l[-1], b))
            l = l[ind:]  # Slice list from first cycle element
            break

    return len(l)

print answer('100000010001', 2)
