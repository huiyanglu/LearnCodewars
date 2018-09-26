import math

def tankvol(h, d, vt):
    theta = math.acos((d/2-h)/(d/2))*(180/math.pi)
    rec = math.sqrt((d/2)**2-(d/2-h)**2)*(d/2-h)
    fan = math.pi*((d/2)**2)*2*theta/360
    s = math.pi*((d/2)**2)
    result1 = fan - rec
    result2 = result1/s * vt
    return int(result2)