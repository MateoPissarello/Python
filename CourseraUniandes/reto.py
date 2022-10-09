import math as m

def area_triangulo(s1,s2,s3):
    s = (s1+s2+s3)/2
    x = ( s * (s-s1) * (s-s2) * (s-s3) )
    if x < 0:
        x *= -1
        sqrt = m.sqrt(x)
    else:
        sqrt = m.sqrt(x)
    xrounded = round(sqrt,1)
    return xrounded

s1 =9
s2=20.6
s3=60.6

area_triangulo(s1,s2,s3)
