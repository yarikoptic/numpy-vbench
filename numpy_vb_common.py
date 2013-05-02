import numpy

# Various pre-crafted datasets/variables for testing
# !!! Must not be changed -- only appended !!!
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

