import wave
import numpy as np

from pyodide import create_proxy, to_js


from js import updateChart

from functions import difraccion


range1 = document.querySelector("#range1")
range2 = document.querySelector("#range2")


# sampling_frequency = 800

# seconds = 1.5

# time = np.linspace(0, seconds, int(seconds * sampling_frequency))

L = 1
a = 4.0e-6
lam0 = 400e-9
x_lim = 3.1*lam0*L/a
x = np.linspace(-x_lim, x_lim, 1000)


def on_range_update(event):

    label = event.currentTarget.nextElementSibling

    label.innerText = event.currentTarget.value

    plot_waveform()


def plot_waveform():

    longitud1 = float(range1.value)

    longitud2 = float(range2.value)


    waveform1 = difraccion(x, longitud1*1e-9, L, a)
    waveform2 = difraccion(x, longitud2*1e-9, L, a)

    updateChart(to_js(x), to_js(waveform1), to_js(waveform2))


proxy = create_proxy(on_range_update)

range1.addEventListener("input", proxy)

range2.addEventListener("input", proxy)


plot_waveform()