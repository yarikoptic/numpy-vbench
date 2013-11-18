#emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
from vbench.benchmark import Benchmark

common_setup = """\
import numpy
from tempfile import TemporaryFile
"""
#----------------------------------------------------------------------
# mappers
setup_tempfile = common_setup + """\
outfile = TemporaryFile()
"""
cleanup = "outfile.close()"

vb_savez_squares = Benchmark('numpy.savez(outfile, squares)',
                             "from numpy_vb_common import squares;\n" + setup_tempfile,
                             cleanup=cleanup)

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

setup = common_setup + """
d = numpy.ones(50000)
e = d.copy()
m = d == 1
im = ~m
m8 = m.copy()
m8[::8] = ~(m[::8])
im8 = ~m8
"""
prereq_copyto = "assert(hasattr(np, 'copyto'))"
vb_copy.append(Benchmark('np.copyto(d, e)', setup,
                         name='copyto', prereq=prereq_copyto))
vb_copy.append(Benchmark('np.copyto(d, e, where=m)', setup,
                         name='copyto_sparse', prereq=prereq_copyto))
vb_copy.append(Benchmark('np.copyto(d, e, where=im)', setup,
                         name='copyto_dense', prereq=prereq_copyto))
vb_copy.append(Benchmark('np.copyto(d, e, where=m8)', setup,
                         name='copyto_8_sparse', prereq=prereq_copyto))
vb_copy.append(Benchmark('np.copyto(d, e, where=im8)', setup,
                         name='copyto_8_dense', prereq=prereq_copyto))
