#emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*-
#ex: set sts=4 ts=4 sw=4 noet:
from vbench.benchmark import Benchmark
setup = """\
import numpy
"""
# empty lines below are somewhat of importance for deriving names of the benchmarks
vb_constructors = []

for b in [
    "numpy.array(1)",
    "numpy.array([])",
    "numpy.array([1])",
    ("numpy.array(l100)", "l100 = range(100);"),
    ("numpy.array(l)", "l = [numpy.arange(1000), numpy.arange(1000)];"),
    ("numpy.vstack(l)", "l = [numpy.arange(1000), numpy.arange(1000)];"),
    ("numpy.hstack(l)", "l = [numpy.arange(1000), numpy.arange(1000)];"),
    ("numpy.dstack(l)", "l = [numpy.arange(1000), numpy.arange(1000)];"),
    #
    "numpy.arange(100)",
    "numpy.zeros(100)",
    "numpy.ones(100)",
    "numpy.empty(100)",
    "numpy.eye(100)",
    "numpy.identity(100)",
    ("numpy.diag(l100)", "l100 = range(100);"),
    ("numpy.diagflat(l100)", "l100 = range(100);"),
    ("numpy.diagflat([l50, l50])", "l50 = range(50);"),
    # some additional constructs
    ("numpy.triu(l10x10)", "l10x10 = numpy.ones((10,10));"),
    ("numpy.tril(l10x10)", "l10x10 = numpy.ones((10,10));"),
    # some masked arrays constructs for a good broth
    "numpy.ma.masked_array()",
    ("numpy.ma.masked_array(l100)", "l100 = range(100);"),
    ("numpy.ma.masked_array(l100,t100)", "l100 = range(100); t100=[True]*100"),
    ]:
    if isinstance(b, tuple):
        bm, setup_ = b
    else:
        bm = b
        setup_ = ""
    vb_constructors.append(
        Benchmark(bm, setup=setup+setup_, name=bm))
