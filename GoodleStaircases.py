import time


def answer(n):
    """
    Commander XXXXXX  may  not be  made  of  money, but  we still don't want
    to solve this in exponential time. So, after a few DP lectures, we'll be
    using  recursion  +  memorization.  Once  a recursive  function  call is
    made,  any identical subsequent  calls  would  not  be  recursive,  they
    would just be a value lookup, which is constant time.
    """

    # Nonetypes scare me so use negative number as placeholder
    mem = [[-1 for i in range(n + 2)] for i in range(n + 2)]

    def ct(height, rem):
        if mem[rem][height] != -1:
            return mem[rem][height]
        if rem == 0:  # Valid staircase base state
            return 1
        if height > rem:  # Invalid staircase
            return 0
        # Try next staircase-column and also entire new staircase
        res = ct(height + 1, rem) + ct(height + 1, rem - height)
        # Save result in memory for potential future use
        mem[rem][height] = res
        return res

    return ct(1, n) - 1

start = time.time()
print answer(200)
print "----- %d -----" % (time.time() - start)
