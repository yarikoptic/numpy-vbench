#emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
from vbench.benchmark import Benchmark
from datetime import datetime

from numpy_vb_common import TYPES1

common_setup = """\
from numpy_vb_common import *
"""
setup = common_setup

vb_random = []
# Simple generators
for f in ('normal', 'uniform', 'weibull'):
    cmd = 'numpy.random.%s(size=(nx, ny))' % f
    vb_random.append(Benchmark(cmd, setup, name=cmd))

# shuffle
vb_random_shuffle100000 = Benchmark("numpy.random.shuffle(a)", setup + "a=numpy.arange(100000)")

#print [x.name for x in vb_random], vb_random_shuffle100000.name
