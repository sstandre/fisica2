import numpy as np

from pyodide import create_proxy, to_js


from js import updateChart

from functions import difraccion, wavelength_to_rgb


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

def wave_color(range):
    longitud = float(range.value)
    waveform = difraccion(x, longitud*1e-9, L, a)
    color = wavelength_to_rgb(longitud)
    return waveform, color

def plot_waveform():

    waveform1, color1 = wave_color(range1)
    waveform2, color2 = wave_color(range2)

    updateChart(*map(to_js, (
        x,
        waveform1,
        waveform2,
        color1,
        color2
        )
    ))


proxy = create_proxy(on_range_update)

range1.addEventListener("input", proxy)

range2.addEventListener("input", proxy)


plot_waveform()