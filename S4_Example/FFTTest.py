import numpy
import matplotlib.pyplot as pyplot
import SpectralAnalysis

fs = 10
f1 = 1
f2 = 3

t = numpy.arange(0, 2, 1/fs)
x1 = numpy.sin(2 * numpy.pi * f1 * t)
x2 = numpy.sin(2 * numpy.pi * f2 * t)
x = x1 + x2

(frequency, amplitude, phase) = SpectralAnalysis.FFT(x, fs, True)

pyplot.subplot(2, 1, 1)
pyplot.plot(t, x)

pyplot.subplot(2, 1, 2)
pyplot.plot(frequency, amplitude)

pyplot.show()
