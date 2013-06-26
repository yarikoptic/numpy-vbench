import numpy
import random

# Various pre-crafted datasets/variables for testing
# !!! Must not be changed -- only appended !!!
random.seed(1)
numpy.random.seed(1)

nx, ny = 1000, 1000
# a set of interesting types to test
TYPES1 = [
        'int16', 'float16',
        'int32', 'float32',
        'int64', 'float64',  'complex64',
                 'float128', 'complex128',
                             'complex256',
        ]


squares = {t: numpy.arange(nx*ny, dtype=getattr(numpy, t)).reshape((nx, ny))
           for t in TYPES1}

indexes = range(nx)
# so we do not have all items
indexes.pop(5)
indexes.pop(95)

# while testing numpy we better not rely on numpy to produce random
# sequences
indexes_rand = indexes[:]       # copy
random.shuffle(indexes_rand)         # in-place shuffle

# only now make them arrays
indexes = numpy.array(indexes)
indexes_rand = numpy.array(indexes_rand)
