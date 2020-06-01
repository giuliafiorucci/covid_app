import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import numpy as np
from src.appdash.predictions import mtcars

# I compute these up front to avoid having to
# calculate thes twice
unq_cyl = np.sort(mtcars["cyl"].unique().astype(int)).astype(str)
opts_cyl = [{"label": i, "value": str(i)} for i in unq_cyl]


layout_left_aligned = html.Div(
    [
        html.H5("Displacement (in cubic inches):"),
        html.Br(),
        html.Br(),
        daq.Slider(
            id="input-disp",
            min=np.floor(mtcars["disp"].min()),
            max=np.ceil(mtcars["disp"].max()),
            step=0.5,
            dots=False,
            handleLabel={"showCurrentValue": True, "label": "Value"},
            value=np.floor(mtcars["disp"].mean()),
        ),
        html.H5("Quarter mile time:"),
        html.Br(),
        html.Br(),
        daq.Slider(
            id="input-qsec",
            min=np.floor(mtcars["qsec"].min()),
            max=np.ceil(mtcars["qsec"].max()),
            dots=False,
            handleLabel={"showCurrentValue": True, "label": "Value"},
            step=0.25,
            value=np.floor(mtcars["qsec"].mean()),
        ),
        html.H5("Number of cylinders:"),
        html.Br(),
        dcc.RadioItems(
            id="input-cyl",
            options=opts_cyl,
            value=opts_cyl[0].get("value"),
            labelStyle={"display": "inline-block"},
        ),
        html.Br(),
        daq.BooleanSwitch(
            id="input-am",
            label="Has manual transmission",
            on=True,
            style={"display": "inline-block"},
        ),
        html.H2(id="output-prediction"),
        html.Br(),
        dcc.Dropdown(
            id="my-dropdown",
            options=[
                {"label": "Linear", "value": "LINEAR"},
                {"label": "Log", "value": "LOG"},
            ],
            value="LINEAR",
            style={
                "background-color": "lightblue",
                "width": "200px",
                "margin": "0 auto",
                "display": "inline-block",
            },
        ),
        html.Br(),
        dcc.Graph(
            id="my-graph",
            style={"width": "1000px", "text-align": "left", "display": "inline-block",},
        ),
    ],
)

params_div = html.Div(
    [
        html.Div(
            [
                html.H5("Displacement (in cubic inches):"),
                html.Br(),
                html.Br(),
                daq.Slider(
                    id="input-disp",
                    min=np.floor(mtcars["disp"].min()),
                    max=np.ceil(mtcars["disp"].max()),
                    step=0.5,
                    dots=False,
                    handleLabel={"showCurrentValue": True, "label": "Value"},
                    value=np.floor(mtcars["disp"].mean()),
                ),
                html.H5("Quarter mile time:"),
                html.Br(),
                html.Br(),
                daq.Slider(
                    id="input-qsec",
                    min=np.floor(mtcars["qsec"].min()),
                    max=np.ceil(mtcars["qsec"].max()),
                    dots=False,
                    handleLabel={"showCurrentValue": True, "label": "Value"},
                    step=0.25,
                    value=np.floor(mtcars["qsec"].mean()),
                ),
                html.H5("Number of cylinders:"),
                html.Br(),
                dcc.RadioItems(
                    id="input-cyl",
                    options=opts_cyl,
                    value=opts_cyl[0].get("value"),
                    labelStyle={"display": "inline-block"},
                ),
                html.Br(),
                daq.BooleanSwitch(
                    id="input-am", label="Has manual transmission", on=True
                ),
            ],
            style={"display": "inline-block",},
        )
    ],
    style={"text-align": "center",},
)

prediction_div = html.Div(
    [
        html.Div(
            [
                html.H2(id="output-prediction"),
                html.Br(),
                html.Br(),
                dcc.Dropdown(
                    id="my-dropdown",
                    options=[
                        {"label": "Linear", "value": "LINEAR"},
                        {"label": "Log", "value": "LOG"},
                    ],
                    value="LINEAR",
                    style={
                        "background-color": "lightblue",
                        "width": "200px",
                        "margin": "0 auto",
                    },
                ),
                html.Br(),
                html.Br(),
                dcc.Graph(id="my-graph", style={"width": "1000px",},),
            ],
            style={"display": "inline-block",},
        )
    ],
    style={"text-align": "center",},
)

layout_centered = html.Div([params_div, prediction_div])
