import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import numpy as np

from src.appdash.predictions import mtcars
from src.appdash.constants import PROJECT_DIR


def make_display_block_div(content):
    return html.Div(content, style={"display": "inline-block",},)


def make_text_align_center_div(content):
    return html.Div(content, style={"text-align": "center",},)


def make_centered_div(content):
    inner_div = make_display_block_div(content)
    outer_div = make_text_align_center_div(inner_div)
    return outer_div


def make_layout_centered(go_figure):
    return make_centered_div([dcc.Graph(figure=go_figure)])


def make_oil_gas_layout(dash_app, go_figure):
    return html.Div(
        [
            dcc.Store(id="aggregate_data"),
            # empty Div to trigger javascript file for graph resizing
            html.Div(id="output-clientside"),
            html.Div(
                [
                    html.Div(
                        [html.H2("COVID-19 Dashboard - Regional Overview",)],
                        className="eight columns",
                        id="title",
                    ),
                    html.Div(
                        [
                            html.Img(
                                src=dash_app.get_asset_url("dash-logo.png"),
                                style={
                                    "height": "60px",
                                    "width": "auto",
                                    "float": "right",
                                },
                            )
                        ],
                        className="four columns",
                    ),
                ],
                # id="header",
                className="row flex-display",
                style={"margin-bottom": "25px"},
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.P(
                                "Filter by construction date (or select range in histogram):",
                                className="control_label",
                            ),
                            dcc.RangeSlider(
                                id="year_slider",
                                min=1960,
                                max=2017,
                                value=[1990, 2010],
                                className="dcc_control",
                            ),
                            html.P("Filter by well status:", className="control_label"),
                            dcc.RadioItems(
                                id="well_status_selector",
                                options=[
                                    {"label": "All ", "value": "all"},
                                    {"label": "Active only ", "value": "active"},
                                    {"label": "Customize ", "value": "custom"},
                                ],
                                value="active",
                                labelStyle={"display": "inline-block"},
                                className="dcc_control",
                            ),
                            dcc.Dropdown(
                                id="well_statuses",
                                options=["on", "off"],
                                multi=True,
                                value=["a", "b"],
                                className="dcc_control",
                            ),
                            dcc.Checklist(
                                id="lock_selector",
                                options=[{"label": "Lock camera", "value": "locked"}],
                                className="dcc_control",
                                value=[],
                            ),
                            html.P("Filter by well type:", className="control_label"),
                            dcc.RadioItems(
                                id="well_type_selector",
                                options=[
                                    {"label": "All ", "value": "all"},
                                    {
                                        "label": "Productive only ",
                                        "value": "productive",
                                    },
                                    {"label": "Customize ", "value": "custom"},
                                ],
                                value="productive",
                                labelStyle={"display": "inline-block"},
                                className="dcc_control",
                            ),
                            dcc.Dropdown(
                                id="well_types",
                                options=["on", "off"],
                                multi=True,
                                value=["a", "b"],
                                className="dcc_control",
                            ),
                        ],
                        className="pretty_container four columns",
                        id="cross-filter-options",
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H6(id="well_text"),
                                            html.P("No. of Wells"),
                                        ],
                                        id="wells",
                                        className="mini_container",
                                    ),
                                    html.Div(
                                        [html.H6(id="gasText"), html.P("Gas")],
                                        id="gas",
                                        className="mini_container",
                                    ),
                                    html.Div(
                                        [html.H6(id="oilText"), html.P("Oil")],
                                        id="oil",
                                        className="mini_container",
                                    ),
                                    html.Div(
                                        [html.H6(id="waterText"), html.P("Water")],
                                        id="water",
                                        className="mini_container",
                                    ),
                                ],
                                id="info-container",
                                className="row container-display",
                            ),
                            html.Div(
                                [dcc.Graph(id="count_graph")],
                                id="countGraphContainer",
                                className="pretty_container",
                            ),
                        ],
                        id="right-column",
                        className="eight columns",
                    ),
                ],
                className="row flex-display",
            ),
            html.Div(
                [
                    html.Div(
                        [dcc.Graph(figure=go_figure, id="main_graph")],
                        className="pretty_container seven columns",
                    ),
                    html.Div(
                        [dcc.Graph(id="individual_graph")],
                        className="pretty_container five columns",
                    ),
                ],
                className="row flex-display",
            ),
            html.Div(
                [
                    html.Div(
                        [dcc.Graph(id="pie_graph")],
                        className="pretty_container seven columns",
                    ),
                    html.Div(
                        [dcc.Graph(id="aggregate_graph")],
                        className="pretty_container five columns",
                    ),
                ],
                className="row flex-display",
            ),
        ],
        id="mainContainer",
    )


def make_new_template(dash_app, go_figure):
    return html.Div(
        [
            html.Div(
                [
                    html.Div("item1", className="p-2"),
                    html.Div("item2", className="p-2"),
                ],
                className="d-flex flex-row justify-content-between",
            )
        ],
        className="container",
        style={"flex-direction": "column"},
    )


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
