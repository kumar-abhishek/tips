def blesenhamLine(start, end):
    cdef int nextX = start[0]
    cdef int nextY = start[1]
    cdef deltaX = end[0] - start[0]
    cdef deltaY = end[1] - start[1]
    cdef int stepX = 0
    cdef int stepY = 0
    cdef int step = 0
    cdef int fraction = 0
    lines = []
    if deltaX < 0:
        stepX = -1
    else:
        stepX = 1
    if deltaY < 0:
        stepY = -1
    else:
        stepY = 1
    deltaX = abs(deltaX * 2)
    deltaY = abs(deltaY * 2)
    lines.append([nextX, nextY])
    step += 1
    if deltaX > deltaY:
        fraction = deltaY - deltaX / 2
        while nextX != end[0]:
            if fraction >= 0:
                nextY += stepY
                fraction -= deltaX
            nextX += stepX
            fraction += deltaY
            lines.append([nextX, nextY])
            step += 1
    else:
        fraction = deltaX - deltaY / 2;
        while nextY != end[1]:
            if fraction >= 0:
                nextX += stepX
                fraction -= deltaY
            nextY += stepY
            fraction += deltaX
            lines.append([nextX, nextY])
            step += 1
    return lines

if __name__ == '__main__':
    start = [1,1]
    goal = [10,5]
    result = blesenhamLine(start, goal)
    print(result)
