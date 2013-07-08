#emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
from vbench.benchmark import Benchmark

common_setup = """\
from numpy_vb_common import *
from tempfile import TemporaryFile
"""
#----------------------------------------------------------------------
# mappers
setup = common_setup + """\
outfile = TemporaryFile()
"""
cleanup = "outfile.close()"

vb_savez_squares = Benchmark('numpy.savez(outfile, squares)', setup, cleanup=cleanup)

vb_copy = []
for type in ("int8", "int16", "float32", "float64",
             "complex64", "complex128"):
    setup = """\
    d = np.arange(50*500, dtype=%s).reshape((500,50))
    e = np.arange(50*500, dtype=%s).reshape((50,500))
    dflat = np.arange(50*500, dtype=%s)
    """ % (type, type, type)
    vb_copy.append(Benchmark('d[...] = e', setup,
                             name='memcpy_' + type))
    vb_copy.append(Benchmark('d[...] = 1', setup,
                             name='cont_assign_' + type))
    vb_copy.append(Benchmark('d[...] = e.T', setup,
                             name='strided_copy_' + type))
    vb_copy.append(Benchmark('dflat[::2] = 2', setup,
                             name='strided_assign_' + type))
