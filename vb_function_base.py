#emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
from vbench.benchmark import Benchmark
setup = """\
import numpy as np
e = np.arange(10000, dtype=np.float32)
o = np.arange(10001, dtype=np.float32)
"""

vb_median = [Benchmark("np.median(e)", setup=setup, name="median_even"),
             Benchmark("np.median(o)", setup=setup, name="median_odd"),
             Benchmark("np.median(e, overwrite_input=True)", setup=setup,
                       name="median_even_inplace"),
             Benchmark("np.median(o, overwrite_input=True)", setup=setup,
                       name="median_odd_inplace")]

vb_perc = [Benchmark("np.percentile(e, [25, 75])", setup=setup, name="quartile"),
           Benchmark("np.percentile(e, [25, 35, 55, 65, 75])", setup=setup,
                     name="percentile")]

vb_sort = [Benchmark("np.sort(e)", setup=setup, name="sort"),
           Benchmark("e.sort()", setup=setup, name="sort_inplace"),
           Benchmark("e.argsort()", setup=setup, name="argsort")]
