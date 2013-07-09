#emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
from vbench.benchmark import Benchmark

laplace_setup = """\
import numpy as np
N = 150 
Niter = 1000
dx = 0.1
dy = 0.1
dx2 = dx*dx
dy2 = dy*dy

def num_update(u, dx2, dy2):
    u[1:-1,1:-1] = ((u[2:,1:-1]+u[:-2,1:-1])*dy2 + 
                    (u[1:-1,2:] + u[1:-1,:-2])*dx2) / (2*(dx2+dy2))

def num_inplace(u, dx2, dy2):
    tmp = u[:-2,1:-1].copy()
    np.add(tmp, u[2:,1:-1], out=tmp)
    np.multiply(tmp, dy2, out=tmp)
    tmp2 = u[1:-1,2:].copy()
    np.add(tmp2, u[1:-1,:-2], out=tmp2)
    np.multiply(tmp2, dx2, out=tmp2)
    np.add(tmp, tmp2, out=tmp)
    np.multiply(tmp, 1./(2.*(dx2+dy2)), out=u[1:-1,1:-1])

def laplace(N, Niter=100, func=num_update, args=()):
    u = np.zeros([N, N], order='C')
    u[0] = 1 
    for i in range(Niter):
        func(u,*args)
    return u
"""


vb_norm = Benchmark("laplace(N, Niter, func=num_update, args=(dx2, dy2))",
                    setup=laplace_setup, name="laplace_normal")
vb_inpl = Benchmark("laplace(N, Niter, func=num_inplace, args=(dx2, dy2))",
                    setup=laplace_setup, name="laplace_inplace")
