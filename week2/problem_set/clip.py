__author__ = 'vanja'

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    # Your code here
    values = [lo, x, hi]
    values.remove(min(values))
    values.remove(max(values))
    return values[0]


def clip_better(lo, x, hi):
    return min(max(x, lo), hi)