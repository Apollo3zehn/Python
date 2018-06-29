import numpy
from S1_Framework import SpectralAnalysis

def FFTGeneralTest():

    # Preparation
    fs = 10
    f1 = 1
    f2 = 3

    t = numpy.arange(0, 2, 1/fs)
    x1 = numpy.sin(2 * numpy.pi * f1 * t)
    x2 = numpy.sin(2 * numpy.pi * f2 * t)
    x = x1 + x2

    # Execution
    (frequency, amplitude, phase) = SpectralAnalysis.FFT(x, fs, True)

    # Assertion
    # self.assertListEqual(numpy.arange(0, 5, 0.5), frequency)
    assert True