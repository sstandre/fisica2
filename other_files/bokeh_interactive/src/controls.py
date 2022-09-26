import asyncio
import json
import pyodide

from js import Bokeh, console, JSON

from bokeh import __version__
from bokeh.document import Document
from bokeh.embed.util import OutputDocumentFor, standalone_docs_json_and_render_items
from bokeh.models import Slider, Div
from bokeh.layouts import Row, layout
from bokeh.protocol.messages.patch_doc import process_document_events
from bokeh.plotting import figure
from bokeh.resources import CDN


# create a new plot with default tools, using figure
f = figure(plot_width=400, plot_height=400)

# add a circle renderer with x and y coordinates, size, color, and alpha
f.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=15, line_color="navy", fill_color="orange", fill_alpha=0.5)


# create a new plot with default tools, using figure
p = Slider(start=0.1, end=10, value=1, step=.1, title="Amplitude")
div = Div(text=f'Amplitude is: {p.value}')

def callback(attr, old, new):
    div.text = f'Amplitude is: {new}'

p.on_change('value', callback)

# row = Row(children=[p, div])
row = layout([[p,div], [f]])















def doc_json(model, target):
    with OutputDocumentFor([model]) as doc:
        doc.title = ""
        docs_json, _ = standalone_docs_json_and_render_items(
            [model], suppress_callback_warning=True
        )

    doc_json = list(docs_json.values())[0]
    root_id = doc_json['roots']['root_ids'][0]

    return doc, json.dumps(dict(
        target_id = target,
        root_id   = root_id,
        doc       = doc_json,
        version   = __version__,
    ))

def _link_docs(pydoc, jsdoc):
    def jssync(event):
        if getattr(event, 'setter_id', None) is not None:
            return
        events = [event]
        json_patch = jsdoc.create_json_patch_string(pyodide.to_js(events))
        pydoc.apply_json_patch(json.loads(json_patch))

    jsdoc.on_change(pyodide.create_proxy(jssync), pyodide.to_js(False))

    def pysync(event):
        json_patch, buffers = process_document_events([event], use_buffers=True)
        buffer_map = {}
        for (ref, buffer) in buffers:
            buffer_map[ref['id']] = buffer
        jsdoc.apply_json_patch(JSON.parse(json_patch), pyodide.to_js(buffer_map), setter_id='js')

    pydoc.on_change(pysync)

async def show(plot, target):
    pydoc, model_json = doc_json(plot, target)
    views = await Bokeh.embed.embed_item(JSON.parse(model_json))
    jsdoc = views[0].model.document
    _link_docs(pydoc, jsdoc)


await show(row, 'myplot')