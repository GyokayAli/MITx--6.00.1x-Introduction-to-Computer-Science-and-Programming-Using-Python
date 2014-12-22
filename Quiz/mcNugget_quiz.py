def McNuggets(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    else:
        return any(McNuggets(n - x) for x in [6, 9, 20])