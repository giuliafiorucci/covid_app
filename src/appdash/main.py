import dash
import numpy as np
import os
import flask
import plotly.graph_objects as go

# import plotly.express as px

from src.appdash.predictions import df, regions
from src.appdash.layouts import (
    make_layout_centered,
    make_oil_gas_layout,
    make_new_template,
)
from src.appdash.constants import PROJECT_DIR


"""
# Setup the app
# the template is configured to execute 'server' on 'src/main.py'
"""

server = flask.Flask(__name__)
server.secret_key = os.environ.get("secret_key", str(np.random.randint(0, 1000000)))

# external_stylesheets = [
#     "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css",
# ]

# create an instance of a dash app
app = dash.Dash(
    __name__,
    server=server,
    # external_stylesheets=external_stylesheets)
    assets_folder=PROJECT_DIR.joinpath("assets"),
)
app.title = "Visualise Stuff"

with open(PROJECT_DIR / ".mapbox_token", "r") as mapbox_file:
    MAPBOX_API_KEY = mapbox_file.read()

choropleth_layout = dict(
    title="Covid Data",
    autosize=False,
    width=700,
    height=800,
    hovermode="closest",
    hoverdistance=30,
    mapbox=dict(
        accesstoken=MAPBOX_API_KEY,
        bearing=0,
        center=dict(lat=41.871941, lon=12.567380),  # the centre of Italy
        pitch=0,
        zoom=4.9,
        style="light",
    ),
)

fig = go.Figure(
    data=[
        go.Choroplethmapbox(
            geojson=regions,
            colorscale="viridis",
            featureidkey="properties.COD_REG",
            locations=df["COD_REG"].astype(str),
            z=df["val"].astype(float),
        )
    ],
    layout=choropleth_layout,
)


# app.layout = make_layout_centered(fig)
app.layout = make_oil_gas_layout(app, fig)
# app.layout = make_new_template(app, fig)


# for running the app
if __name__ == "__main__":
    app.server.run(debug=True)  # production
