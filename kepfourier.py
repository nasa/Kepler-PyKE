#!/usr/bin/env python

import numpy as np

# -----------------------------------------------------------
# Fourier Transform

def ft(x,y,f1,f2,df,verbose):

    ft_real = []; ft_imag = []; power = []; fr = []; nstep = 0
    for freq in np.arange(f1,f2,df):
        ft_real.append(0.0)
        ft_imag.append(0.0)
        omega = 2.0 * np.pi * freq
        ndata = len(x)
        for i in range(ndata):
            expo = omega * x[i]
            c = np.cos(expo)
            s = np.sin(expo)
            ft_real[-1] += y[i] * c
            ft_imag[-1] += y[i] * s
        fr.append(freq)
        if ndata > 0:
            power.append((ft_real[-1]**2 + ft_imag[-1]**2) / ndata**2)
        else:
            power.append(np.nan)
        nstep += 1
        if verbose:
            print('Step: %5d  Period: %10.6f (d)  Power: %e' %
                  (nstep, 1.0 / fr[-1], power[-1]))
    fr = np.array(fr,dtype='float32')
    power = np.array(power,dtype='float32')

    return fr, power
