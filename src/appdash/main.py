import dash
import numpy as np
import os
import flask

from src.appdash.predictions import mtcars, preds, make_fit
from src.appdash.layouts import layout_centered


"""
# Setup the app
# the template is configured to execute 'server' on 'src/main.py'

dash apps are unstyled by default
external CSS stylesheets
https://dash.plotly.com/external-resources
"""

server = flask.Flask(__name__)
server.secret_key = os.environ.get("secret_key", str(np.random.randint(0, 1000000)))

external_stylesheets = [
    "https://codepen.io/chriddyp/pen/bWLwgP.css",
]

# create an instance of a dash app
app = dash.Dash(
    __name__,
    external_scripts=None,
    external_stylesheets=external_stylesheets,
    server=server,
)
app.title = "Predicting MPG"
app.layout = layout_centered


# callback will watch for changes in inputs and re-execute when any
# changes are detected.
@app.callback(
    dash.dependencies.Output("output-prediction", "children"),
    [
        dash.dependencies.Input("input-disp", "value"),
        dash.dependencies.Input("input-qsec", "value"),
        dash.dependencies.Input("input-cyl", "value"),
        dash.dependencies.Input("input-am", "on"),
    ],
)
def callback_pred(disp: float, qsec: float, cyl: str, am: bool) -> str:
    """Pass values from the UI on to our prediction function defined in
    predictions.py.

    Parameters
    ----------
    disp
    qsec
    cyl
    am

    Returns
    -------
    None
    """
    fit, cyl_enc = make_fit(mtcars)
    pred = preds(
        fit=fit, cyl_enc=cyl_enc, disp=disp, qsec=qsec, am=np.float64(am), cyl=cyl
    )
    # return a string that will be rendered in the UI
    return "Predicted MPG: {}".format(pred)


@app.callback(
    dash.dependencies.Output("my-graph", "figure"),
    [dash.dependencies.Input("my-dropdown", "value")],
)
def update_graph(selected_dropdown_value):
    if selected_dropdown_value == "LINEAR":
        return {
            "data": [{"x": mtcars.index, "y": mtcars.disp}],
            "layout": {"margin": {"l": 200, "r": 200, "t": 20, "b": 30}},
        }
    else:
        return {
            "data": [{"x": mtcars.index, "y": np.log(mtcars.disp)}],
            "layout": {"margin": {"l": 200, "r": 200, "t": 20, "b": 30}},
        }


# for running the app
if __name__ == "__main__":
    app.server.run(debug=True, threaded=True)
