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
                       name="median_odd_inplace"),
             Benchmark("np.median(e[:500], overwrite_input=True)", setup=setup,
                       name="median_even_small"),
             Benchmark("np.median(o[:500], overwrite_input=True)", setup=setup,
                       name="median_odd_small"),
             ]

vb_perc = [Benchmark("np.percentile(e, [25, 75])", setup=setup, name="quartile"),
           Benchmark("np.percentile(e, [25, 35, 55, 65, 75])", setup=setup,
                     name="percentile")]

vb_sort = [Benchmark("np.sort(e)", setup=setup, name="sort"),
           Benchmark("e.sort()", setup=setup, name="sort_inplace"),
           Benchmark("e.argsort()", setup=setup, name="argsort")]

vb_bincount = Benchmark("np.bincount(d)",
                        setup="d = np.arange(80000, dtype=np.intp)",
                        name="bincount")
vb_bincountw = Benchmark("np.bincount(d, weights=e)",
                        setup="d = np.arange(80000, dtype=np.intp); "\
                        "e = d.astype(np.float64)",
                        name="bincount_weights")

vb_where = [Benchmark("np.where(cond)",
                      setup="d = np.arange(20000); cond = d > 5000",
                      name="where_1"),
            Benchmark("np.where(cond, d, e)",
                      setup="d = np.arange(20000); "\
                      "e = d.copy(); cond = d > 5000",
                      name="where_2"),
            Benchmark("np.where(cond, d, 0)",
                      setup="d = np.arange(20000); cond = d > 5000",
                      name="where_2_broadcast"),
           ]

vb_select = [Benchmark("np.select(cond, [d, e])",
                       setup="d = np.arange(20000); e = d.copy();"\
                       "cond = [d > 4, d < 2]",
                       name="select"),
             Benchmark("np.select(cond, [d, e] * 10)",
                       setup="d = np.arange(20000); e = d.copy();"\
                       "cond = [d > 4, d < 2] * 10",
                       name="select_larger"),
            ]
