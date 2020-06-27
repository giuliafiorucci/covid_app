import dash
import numpy as np
import os
import flask
import plotly.graph_objects as go

# import plotly.express as px

from src.appdash.predictions import df, regions
from src.appdash.layouts import make_layout_centered


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
app.title = "Visualise Stuff"


MAPBOX_API_KEY = os.getenv("MAPBOX_TOKEN", None)

# fig = px.choropleth_mapbox(
#     df,
#     geojson=regions,
#     locations="COD_REG",
#     featureidkey="properties.COD_REG",
#     color="val",
#     color_continuous_scale="Viridis",
# )

fig = go.Figure(
    data=[
        go.Choroplethmapbox(
            geojson=regions,
            colorscale="viridis",
            featureidkey="properties.COD_REG",
            locations=df["COD_REG"].astype(str),
            z=df["val"].astype(float),
        )
    ]
)

custom_layout = dict(
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
fig.update_layout(custom_layout)


app.layout = make_layout_centered(fig)


# for running the app
if __name__ == "__main__":
    app.server.run(debug=False)
