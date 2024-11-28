def most_students(classroom):
    '''
    classroom is a list of lists
    Each ' ' is an empty seat
    Each 'S' is a student
    How many new students can sit in a row?
    >>> most_students([['S', ' ', 'S', 'S', 'S', 'S'], [' ', 'S', 'S', 'S', 'S', 'S'], [' ', 'S', ' ', 'S', ' ', ' ']])    
    4
    '''
    max_students = 0
    for row in classroom:
        students = 0
        for seat in row:
            if seat == 'S':
                students += 1
            else:
                students = 0
            if students > max_students:
                max_students = students
    return max_students
import doctest
doctest.testmod(verbose=True)