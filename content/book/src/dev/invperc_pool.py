#!/usr/bin/env python

'''Invasion Percolation Simulation

usage: invperc.py grid_size value_range random_seed

grid_size:   the width/height of the grid
             must be a positive odd integer

value_range: number of distinct values in grid
             must be a positive integer
             values will be selected randomly in 1..value_range

random_seed:   random number generation seed
             must be a positive integer
'''

import sys, random

FILLED = -1    # Used to mark filled cells.

def fail(msg):
    '''Print error message and halt program.'''
    print >> sys.stderr, msg
    sys.exit(1)

def create_grid(N):
    '''Return an NxN grid of zeros.'''

    assert N > 0, 'Grid size must be positive'
    assert N%2 == 1, 'Grid size must be odd'
    grid = []
    for x in range(N):
        grid.append([])
        for y in range(N):
            grid[-1].append(0)
    return grid

def fill_random_grid(grid, Z):
    '''Fill a grid with random values in 1..Z.
    Assumes the RNG has already been seeded.'''

    N = len(grid)
    assert N > 0, 'Grid size must be positive'
    assert N%2 == 1, 'Grid size must be odd'
    assert Z > 0, 'Random range must be positive'
    for x in range(N):
        for y in range(N):
            grid[x][y] = random.randint(1, Z)
    return grid

def mark_filled(grid, x, y):
    '''Mark a grid cell as filled.'''

    assert 0 <= x < len(grid), \
           'X coordinate out of range (%d vs %d)' % \
           (x, len(grid))
    assert 0 <= y < len(grid), \
           'Y coordinate out of range (%d vs %d)' % \
           (y, len(grid))

    grid[x][y] = FILLED

def is_candidate(grid, x, y):
    '''Is a cell a candidate for filling?'''

    N = len(grid)
    return (x > 0) and (grid[x-1][y] == FILLED) \
        or (x < N-1) and (grid[x+1][y] == FILLED) \
        or (y > 0) and (grid[x][y-1] == FILLED) \
        or (y < N-1) and (grid[x][y+1] == FILLED)

def get_next(pool):
    '''Take a cell randomly from the equal-valued front section.'''

    temp = list(pool)
    temp.sort()
    v = temp[0][0]
    i = 1
    while (i < len(temp)) and (temp[i][0] == v):
        i += 1
    i = random.randint(0, i-1)
    v, x, y = temp[i]
    pool.discard((v, x, y))
    return x, y

def make_candidate(grid, pool, x, y):
    '''Ensure that (x, y, v) is a candidate.'''

    v = grid[x][y]
    if v == FILLED:
        return
    pool.add((v, x, y))

def fill_grid(grid):
    '''Fill an NxN grid until filled region hits boundary.'''

    size = len(grid)
    x, y = size/2, size/2
    pool = set()
    pool.add((grid[x][y], x, y))
    num_filled = 0
    on_edge = False

    while not on_edge:
        x, y = get_next(pool)
        mark_filled(grid, x, y)
        num_filled += 1
        if (x == 0) or (x == size-1) or (y == 0) or (y == size-1):
            on_edge = True
        else:
            if x > 0:      make_candidate(grid, pool, x-1, y)
            if x < size-1: make_candidate(grid, pool, x+1, y)
            if y > 0:      make_candidate(grid, pool, x,   y-1)
            if y < size-1: make_candidate(grid, pool, x,   y+1)

    return num_filled

def do_random(arguments):
    '''Run a random simulation.'''

    # Parse arguments.
    try:
        grid_size = int(arguments[0])
        value_range = int(arguments[1])
        random_seed = int(arguments[2])
    except IndexError:
        fail('Expected 3 arguments, got %d' % len(arguments))
    except ValueError:
        fail('Expected integer arguments, got %s' % str(arguments))

    # Run simulation.
    random.seed(random_seed)
    grid = create_grid(grid_size)
    fill_random_grid(grid, value_range)
    mark_filled(grid, grid_size/2, grid_size/2)
    num_filled_cells = fill_grid(grid) + 1
    print '%d cells filled' % num_filled_cells

def is_star(x):
    '''Is this cell supposed to be filled?'''
    return x == '*'

def parse_general(fixture, converter):
    '''Turn a string representation of a grid into a grid of values.'''

    result = [x.strip().split() for x in fixture.split('\n')]
    size = len(result)
    for row in result:
        if len(row) != size:
            fail('Badly formed fixture')
        for i in range(len(row)):
            row[i] = converter(row[i])
    return result

def check_result(expected, grid, num_filled):
    '''Check the results of filling.'''
    expected, count = convert_grid(expected)

    if len(expected) != len(grid):
        fail('Mis-match between size of expected result and size of grid')
    if count != num_filled:
        fail('Wrong number of cells filled')

    for i in range(len(expected)):
        g = grid[i]
        e = expected[i]
        if len(g) != len(e):
            fail('Rows are not the same length')
        for j in range(len(g)):
            if g[j] and (e[j] != FILLED):
                fail('Cell %d,%d should be filled but is not' % (i, j))
            elif (not g[j]) and (e[j] == FILLED):
                fail('Cell %d,%d should not be filled but is' % (i, j))
    return result

def do_5x5_line():
    '''Run a test on a 5x5 grid with a run to the border.'''

    fixture  = '''2 2 2 2 2
                  2 2 2 2 2
                  1 1 1 2 2
                  2 2 2 2 2
                  2 2 2 2 2'''

    expected = '''. . . . .
                  . . . . .
                  * * * . .
                  . . . . .
                  . . . . .'''

    fixture = parse_general(fixture, int)
    num_filled_cells = fill_grid(fixture)
    expected = parse_general(fixture, is_star)
    check_result(expected, fixture, num_filled_cells)

def main(scenario, arguments):
    '''Run the simulation.'''

    if scenario == 'random':
        do_random(arguments)
    elif scenario == '5x5_line':
        do_5x5_line(arguments)
    else:
        fail('Unknown scenario "%s"' % scenario)

# Main driver.
if __name__ == '__main__':
    assert len(sys.argv) > 1, 'Must have at least a scenario name'
    main(sys.argv[1], sys.argv[2:])
