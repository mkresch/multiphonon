"""
This is a simple example where I(Q,E) data is already in the form 
of a histogram, reduced from the raw experimental data.
All this script does is to convert I(Q,E) to Density of States
by performing multiphonon correction.
"""
import histogram.hdf as hh, os, numpy as np
from matplotlib import pyplot as plt
# load data
iqehist = hh.load("data/Al-iqe.h5") 
# interpolate data
from multiphonon.sqe import interp
newiqe = interp(iqehist, newE = np.arange(-40, 70, 1.))
# save interpolated data
hh.dump(newiqe, 'data/Al-iqe-interped.h5')
# create processing engine
from multiphonon.backward import sqe2dos
iterdos = sqe2dos.sqe2dos(
    newiqe, T=300, Ecutoff=50., 
    elastic_E_cutoff=(-10., 7), M=26.98,
    C_ms=0.2, Ei=80., workdir='work-Al')
# process and plot
for i, dos in enumerate(iterdos):
    plt.plot(dos.E, dos.I, label='%d' % i)
plt.show()
