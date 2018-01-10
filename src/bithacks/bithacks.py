# Computes the sign of an integer.
def computeSign(v):
    return (v > 0) - (v < 0)

# Detects if two integers have opposite signs
def detectOppositeSigns(x, y):
    return (x ^ y) < 0
