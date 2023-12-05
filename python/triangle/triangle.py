def equilateral(sides):
        return (
            (sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]) and
            all(x > 0 for x in sides) and 
            (sides[0] is sides[1] and sides[1] is sides[2])
        )

def isosceles(sides):
    return (
         (sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]) and
         all(x > 0 for x in sides) and 
         (sides[0] is sides[1] or sides[0] is sides[2] or sides[1] is sides[2])
    )

def scalene(sides):
    return (
         (sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]) and
         all(x > 0 for x in sides) and 
         (sides[0] is not sides[1] and sides[0] is not sides[2] and sides[1] is not sides[2])
    )
