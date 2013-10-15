
Performance Benchmarks
======================

These historical benchmark graphs were produced with `vbench
<http://github.com/pydata/vbench>`__ (ATM with yet to be integrated
upstream changes in https://github.com/pydata/vbench/pull/33).

Original repository with the The `numpy_vb_common
<https://github.com/yarikoptic/numpy-vbench/blob/master/numpy_vb_common.py>`__
setup script defining various variables and data structures used
through-out the bench can be found on github_ .

.. _github: https://github.com/yarikoptic/numpy-vbench

Results were collected on a following machine:

  - Dual AMD Opteron(tm) Processor 246, 3GB RAM
  - Debian wheezy, amd-64 build (chroot on Debian with 3.2.0-4-amd64 kernel)
  - Python 2.7.3 64-bit

cpuinfo::

    vendor_id       : AuthenticAMD
    cpu family      : 15
    model           : 5
    model name      : AMD Opteron(tm) Processor 246
    stepping        : 8
    microcode       : 0x46
    cpu MHz         : 1994.032
    cache size      : 1024 KB
    fpu             : yes
    fpu_exception   : yes
    cpuid level     : 1
    wp              : yes
    flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx
	                  fxsr sse sse2 syscall nx mmxext lm 3dnowext 3dnow rep_good nopl
    bogomips        : 3988.06
    TLB size        : 1024 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 40 bits physical, 48 bits virtual
    power management: ts ttp


.. include:: analysis.rst



.. toctree::
    :hidden:
    :maxdepth: 3

    vb_vb_app
    vb_vb_core
    vb_vb_function_base
    vb_vb_indexing
    vb_vb_io
    vb_vb_linalg
    vb_vb_random
    vb_vb_reduce
    vb_vb_ufunc
