
def answer(M, F):
    """
    There's a few thing that we notice about the M-F algorithm
    from its nature and after doing a few examples by hand:
    (1) F and M can only be equal if they are equal to 1.
    (2) At least one of them must be odd
    (3) One of them can't be a multiple of the other unless it's multiple of 1 case
    (4) A state where F = 1 and M > 1, it takes M - 1 generations to reach.
    (5) When one is much bigger than the other, we repeat the same branch
    until they are of comparable sizes, these repetitions can be optimized
    into a single recursive call.
    """
    mach = int(M)
    facula = int(F)

    def validate(ma, fa):
        # According to (1)
        if ma == fa and ma > 1:
            return False
        # According to (2)
        if ma % 2 == 0 and fa % 2 == 0:
            return False
        # According to 3
        if (ma % fa == 0 and fa != 1) or (fa % ma == 0 and ma != 1):
            return False

        return True

    def run(ma, fa, calls=0):
        if not validate(ma, fa):
            return "impossible"

        if ma > fa:
            if fa > 1:  # See (5)
                return run(ma - ((ma / fa) * fa), fa, calls + (ma / fa))
            else:       # See (4)
                return run(1, 1, calls + ma - 1)

        elif fa > ma:
            if ma > 1:
                return run(ma, fa - ((fa / ma) * ma), calls + (fa / ma))
            else:
                return run(1, 1, calls + fa - 1)
        else:
            return calls

    return str(run(mach, facula))

print answer('2', '4')
