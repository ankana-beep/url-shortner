
BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode(num):
    base = len(BASE62)
    res = []
    while num:
        num, rem = divmod(num, base)
        res.append(BASE62[rem])
    return ''.join(reversed(res))
