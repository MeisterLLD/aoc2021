segments = [ ]
with open('5','r') as f:
    lignes = f.read().splitlines()
    for ligne in lignes:
        deb, fin = ligne.split(' -> ')
        x1, y1 = map(int, deb.split(','))
        x2, y2 = map(int, fin.split(','))
        segments.append(  ((x1,y1),(x2,y2))      )


def count_overlaps(segments, part):
    points = {}

    for segment in segments:
        (x1, y1), (x2, y2) = segment
        xmin, xmax = min(x1,x2), max(x1, x2)
        ymin, ymax = min(y1,y2), max(y1, y2)

        if xmin == xmax: # vertical
            for y in range(ymin, ymax + 1):
                key = (x1, y)
                points[key] = points.get(key, 0) + 1
        elif ymin == ymax: # horizontal
            for x in range(xmin, xmax + 1):
                key = (x, y1)
                points[key] = points.get(key, 0) + 1

        elif part == 2: # diagonal
            for c in range( xmax -  xmin + 1):
                key = (xmin+c, ymin+c) if (y2-y1)*(x2-x1) > 0 else (xmin+c, ymax-c) # +45° or -45°
                points[key] = points.get(key, 0) + 1

    return sum( v >= 2 for v in points.values() )


print('Part 1 :', count_overlaps(segments, 1))
print('Part 2 :', count_overlaps(segments, 2))