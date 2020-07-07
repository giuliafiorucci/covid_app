import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import numpy as np

from src.appdash.predictions import df


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


def get_layout_header(dash_app):
    return html.Div(
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
                        style={"height": "60px", "width": "auto", "float": "right",},
                    )
                ],
                className="four columns",
            ),
        ],
        className="row flex-display",
        style={"margin-bottom": "25px"},
    )


def get_layout_controls():
    return (
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
                                {"label": "Productive only ", "value": "productive",},
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
                                    [html.H6(id="well_text"), html.P("No. of Wells"),],
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
    )


def get_layout_graphs_main(go_figure):
    return html.Div(
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
    )


def get_layout_graphs_secondary():
    return html.Div(
        [
            html.Div(
                [dcc.Graph(id="pie_graph")], className="pretty_container seven columns",
            ),
            html.Div(
                [dcc.Graph(id="aggregate_graph")],
                className="pretty_container five columns",
            ),
        ],
        className="row flex-display",
    )


def make_new_template(dash_app, go_figure):
    return html.Div(
        [
            dcc.Store(id="aggregate_data"),
            # empty Div to trigger javascript file for graph resizing
            html.Div(id="output-clientside"),
            get_layout_header(dash_app),
            get_layout_controls(),
            get_layout_graphs_main(go_figure),
            get_layout_graphs_secondary(),
        ],
        id="mainContainer",
    )
