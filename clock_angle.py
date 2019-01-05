import math
def clock_angle(hour, min, second, type):
    if type in ['degree', 'radian']:
        hour_hand = (hour + min/60 + second/3600)
        min_hand = (min + second/60)
        difference = abs(hour_hand - min_hand)/12
        if type == 'degree':
            return difference*360
        if type == 'radian':
            return difference*2*math.pi
    else:
        return '{} is an invald formate choose either degree, or radian'.format(type)


print(clock_angle(3,29,0,'degree'))
