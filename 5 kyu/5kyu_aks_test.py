def aks_test(p):
    a = []
    if p>=2:
        for x in range(0,10):
            m = (x-1)**p-(x**p-1)
            if m%p ==0:
                a.append(x)
        if len(a)==10:
            return True
        else:
            return False
    else:
        return None