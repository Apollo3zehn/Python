# zero-padding: http://www.bitweenie.com/listings/fft-zero-padding/#
# + Increases the frequency resolution
# + Fastens the FFT
# - Introduces new frequencies due to the sudden drop to zero
# => implementation details: http://pageperso.lif.univ-mrs.fr/~francois.denis/IAAM1/scipy-html-1.0.0/generated/scipy.fftpack.next_fast_len.html
#
# Parseval's theorem: http://math.stackexchange.com/questions/636847/understanding-fourier-transform-example-in-matlab
# AmplitudePhase = fft(Data, FftLength) / Frequency;

from typing import List
import numpy
from scipy import fftpack

def FFT(data: list, samplingFrequency: int, zeroPadding: bool) -> (List[float], List[float], List[float]):

    signalLength = len(data)

    if zeroPadding:
        fftLength = fftpack.next_fast_len(signalLength)
    else:
        fftLength = signalLength

    amplitudePhase = fftpack.fft(data, fftLength) / signalLength

    if fftLength % 2 == 0:
        binCount = int(fftLength / 2 + 1)
        amplitude = abs(amplitudePhase[0:binCount])
        amplitude[1:-1] = 2 * amplitude[1:-1]
    else:
        binCount = int((fftLength + 1) / 2)
        amplitude = abs(amplitudePhase[0:binCount])
        amplitude[1:] = 2 * amplitude[1:]

    phase = numpy.angle(amplitudePhase[0:binCount])
    frequency = samplingFrequency / 2 * numpy.linspace(0, 1, binCount)

    return (frequency, amplitude, phase)
