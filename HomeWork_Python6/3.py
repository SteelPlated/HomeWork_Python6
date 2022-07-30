import math

orbits=[(1,3),(2.5,10),(7,2),(6,6), (4,3)]

def find_farthest_orbit(list):
    max=0
    s_ind=-1
    S = [i[0]*i[1] for i in orbits]
    for i in S:
        if i>max:
            max=i
            s_ind=S.index(i)
    if s_ind!=-1:
        return (list[s_ind])
    else:
       return ("ОШИБКА") 
  
print(*find_farthest_orbit(orbits))