#emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
from vbench.benchmark import Benchmark
from datetime import datetime

from numpy_vb_common import TYPES1

common_setup = """\
from numpy_vb_common import *
"""
setup = common_setup

vb_indexing = []
vb_indexing_separate = []
for l in ['indexes', 'indexes_rand']:
    for dim in ('', ':,'):
        for op in ['', '=1']:
            act = "a[%s%s]%s" % (dim, l, op)
            name = act

            vb_indexing.append(
                Benchmark('for a in squares.itervalues(): %s' % (act,), setup, name=name))

            for t in TYPES1:
                vb_indexing_separate.append(
                    Benchmark(act, setup + "\na = squares[%r]" % t,
                              name='%s_%s' % (name, t)))

setup = """\
import tempfile
from numpy import memmap, float32, array
fp = memmap(tempfile.NamedTemporaryFile(), dtype=float32, mode='w+', shape=(50,60))"""

act_slicing = """\
for i in range(1000):
     fp[5:10]
"""

act_indexing = """\
for i in range(1000):
     fp[indexes]
"""
clean = "del fp"

vb_indexing_separate += [
    Benchmark(act_slicing, setup,
              name='mmap_slicing', cleanup=clean),
    Benchmark(act_indexing, setup + "\nindexes = array([3,4,6,10,20])",
              name='mmap_fancy_indexing', cleanup=clean),
    ]

_vb_names = [x.name for x in vb_indexing_separate]
del x                                         # so it doesn't leak
assert(len(_vb_names) == len(set(_vb_names)))   # all are unique
#print '\n'.join(_vb_names)
