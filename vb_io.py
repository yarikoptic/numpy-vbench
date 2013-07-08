#emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
from vbench.benchmark import Benchmark

common_setup = """\
from numpy_vb_common import *
from tempfile import TemporaryFile
"""
#----------------------------------------------------------------------
# mappers
setup_tempfile = common_setup + """\
outfile = TemporaryFile()
"""
cleanup = "outfile.close()"

vb_savez_squares = Benchmark('numpy.savez(outfile, squares)', setup_tempfile, cleanup=cleanup)

vb_copy = []
for type in ("int8", "int16", "float32", "float64",
             "complex64", "complex128"):
    setup = common_setup + """
d = numpy.arange(50*500, dtype=numpy.%s).reshape((500,50))
e = numpy.arange(50*500, dtype=numpy.%s).reshape((50,500))
e_d = e.reshape(d.shape)
dflat = numpy.arange(50*500, dtype=numpy.%s)
""" % (type, type, type)
    vb_copy.append(Benchmark('d[...] = e_d', setup,
                             name='memcpy_' + type))
    vb_copy.append(Benchmark('d[...] = 1', setup,
                             name='cont_assign_' + type))
    vb_copy.append(Benchmark('d[...] = e.T', setup,
                             name='strided_copy_' + type))
    vb_copy.append(Benchmark('dflat[::2] = 2', setup,
                             name='strided_assign_' + type))
