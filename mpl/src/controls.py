import pandas as pd

import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,30)
from functions import difraccion, wavelength_to_rgb


from pyodide.http import open_url
from pyodide import create_proxy

url = (
    "https://raw.githubusercontent.com/Cheukting/pyscript-ice-cream/main/bj-products.csv"
)
ice_data = pd.read_csv(open_url(url))
current_selected = []
flavour_elements = document.getElementsByName("flavour")





"""
LAMBDA1 = 400
LAMBDA2 = 500

fig = plot(lambda1, lambda2)

callback(lambda1, lambda2):
    nwdata (lambda1, lambda2)
    fig.update_data(nwdata)

bind_callback

"""












def plot(data):
    fig, ax = plt.subplots()
    bars = ax.barh(data["name"], data["rating"], height=0.7)
    ax.bar_label(bars)
    plt.title("Rating of ice cream flavours of your choice")
    pyscript.write("viz",fig)

@create_proxy
def select_flavour(event):
    for ele in flavour_elements:
        if ele.checked:
            current_selected = ele.value
            break
    if current_selected == "ALL":
        plot(ice_data)
    else:
        filter = ice_data.apply(lambda x: ele.value in x["ingredients"], axis=1)
        plot(ice_data[filter])

# ele_proxy = create_proxy(select_flavour)

for ele in flavour_elements:
    if ele.value == "ALL":
      ele.checked = True
      current_selected = ele.value
    ele.addEventListener("change", select_flavour)

plot(ice_data)