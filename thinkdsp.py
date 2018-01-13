

import thinkdsp
import thinkplot

import numpy

cos_sig = thinkdsp.CosSignal(freq=440)
cos_sig.plot()
thinkplot.config(xlabel='time', legend=False)