def descent(func, params, cost, n = 100, delta = pow(10, -5), threshold = pow(10, -3), k = 0.01):
    original = cost(func(params))
    descended = params + []
    while True:
        vect = [0 for i in range(len(params))]
        for each in range(len(params)):
            newp = descended + []
            newp[each] += delta
            print("Newp:", newp, cost(func(newp)))
            deriv = (cost(func(newp)) - original)/delta
            vect[each] = (-1 * deriv * k)
            descended[each] += vect[each]
            original = cost(func(descended))
        if cost(func(descended)) <= threshold: return descended
    return descended



from math import cos, sin, pi
def position(radii, thetas):
    x, y = 0, 0
    for each in range(len(radii)):
        x += (radii[each] * cos(thetas[each]))
        y += (radii[each] * sin(thetas[each]))
    return (x, y)

def distance(current, target):
    return pow(  pow(current[0] - target[0], 2) + pow(current[1] - target[1], 2)  , 0.5)

targetp = (0.24, 0.085)
rs = [1, 0.5, 0.7, 0.2]

breh = (descent(lambda x: position(rs, x), [-0.6342203747384803, -0.45705114207042474, 1.8146139780661765, 0], lambda x: distance(x, targetp), 100000000, k = 0.01))
print('Angles:',breh)
print(position(rs, breh))
print(distance(position(rs, breh), targetp))