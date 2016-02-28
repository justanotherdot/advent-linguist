
import fileinput

###################################
# Functions                       #
###################################

def turn_on_light(coord, ls):
    ls[coord] = True

def turn_off_light(coord, ls):
    ls[coord] = False


def turn_on_many_lights(f_coords, t_coords, ls):
    x1,y1 = f_coords
    x2,y2 = t_coords
    for n in xrange(x1, x2+1):
        for m in xrange(y1, y2+1):
            coord = (n,m)
            turn_on_light(coord, ls)


def turn_off_many_lights(f_coords, t_coords, ls):
    x1,y1 = f_coords
    x2,y2 = t_coords
    for n in xrange(x1, x2+1):
        for m in xrange(y1, y2+1):
            coord = (n,m)
            turn_off_light(coord, ls)


def is_light_on(coord, ls):
    if coord in ls:
        return ls[coord]
    else:
        return False


def toggle_light(coord, ls):
    if is_light_on(coord, ls):
        ls[coord] = not ls[coord]
    else:
        # All lights begin off...
        ls[coord] = True


def toggle_many_lights(f_coords, t_coords, ls):
    x1,y1 = f_coords
    x2,y2 = t_coords
    for n in xrange(x1, x2+1):
        for m in xrange(y1, y2+1):
            coord = (n,m)
            toggle_light(coord, ls)


if __name__ == '__main__':
    lights = {}
    for line in fileinput.input():
        tokens = line.split()
        if tokens[0] == 'turn':
            from_coord =  tuple(map(int, tokens[2].split(',')))
            to_coord = tuple(map(int, tokens[4].split(',')))
            if tokens[1] == 'on':
                turn_on_many_lights(from_coord, to_coord, lights)
            elif tokens[1] == 'off':
                turn_off_many_lights(from_coord, to_coord, lights)
        elif tokens[0] == 'toggle':
            from_coord =  tuple(map(int, tokens[1].split(',')))
            to_coord = tuple(map(int, tokens[3].split(',')))
            toggle_many_lights(from_coord, to_coord, lights)
    # filter list
    res = [(k,v) for (k,v) in lights.iteritems() if v]
    print len(res)

###################################
# Tests                           #
###################################

def setup():
    lights = {} # Reset the lights global var -- All false (off)!
    return lights

def turn_on_many_test():
    lights = setup()
    turn_on_many_lights((499,499), (500,500), lights)
    for k,v in lights.iteritems():
        print k,v

def toggle_many_test():
    lights = setup()
    toggle_many_lights((0,0), (999,0), lights)
    for k,v in lights.iteritems():
        print k,v

def is_light_on_test():
    lights = setup()
    print is_light_on((0,0), lights)
    lights[(0,1)] = True
    print is_light_on((0,1), lights)
