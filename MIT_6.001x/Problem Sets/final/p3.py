def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    for a in range(10):
        for b in range(10):
            for c in range(10):
                t = 6*a + 9*b + 20*c
                if t == n:
                    return True
    return False
    
n = int(input())
McNuggets(n)