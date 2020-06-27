import pandas as pd
import numpy as np
import json

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

from src.appdash.constants import DATA_DIR, PROJECT_DIR


def make_fit(mtcars_df):
    cyl_enc = OneHotEncoder(categories="auto", sparse=False)
    cyl_enc.fit(mtcars_df["cyl"].values.reshape(-1, 1))
    y = mtcars_df["mpg"]
    X = np.concatenate(
        (
            mtcars_df[["disp", "qsec", "am"]].values,
            cyl_enc.transform(mtcars_df["cyl"].values.reshape(-1, 1)),
        ),
        axis=1,
    )
    fit = LinearRegression()
    fit.fit(X=X, y=y)
    return fit, cyl_enc


def preds(fit, cyl_enc, disp, qsec, am, cyl):
    # construct our matrix
    X = np.concatenate(
        (np.array([[disp, qsec, am]]), cyl_enc.transform([[cyl]])), axis=1
    )
    # find predicted value
    pred = fit.predict(X)[0]
    # return a rounded string for nice UI display
    return str(round(pred, 2))


# import requests
# file_name = "dpc-covid19-ita-regioni-latest.json"
# url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/" + file_name
# r = requests.get(url)
# with open(file_name , 'wb') as f:
#     f.write(r.content)


# from urllib.request import urlopen
# import json
# with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
#     counties = json.load(response)


with open(PROJECT_DIR / "data" / "italy_regions_light.geojson", "r") as json_regions:
    regions = json.load(json_regions)

df = pd.DataFrame({"COD_REG": range(1, 22), "val": np.random.randn(21)})
df["COD_REG"] = df["COD_REG"].astype(str)


# df = pd.read_csv(
#     "https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv"
# )
# for col in df.columns:
#     df[col] = df[col].astype(str)
#
# df["text"] = (
#     df["state"]
#     + "<br>"
#     + "Beef "
#     + df["beef"]
#     + " Dairy "
#     + df["dairy"]
#     + "<br>"
#     + "Fruits "
#     + df["total fruits"]
#     + " Veggies "
#     + df["total veggies"]
#     + "<br>"
#     + "Wheat "
#     + df["wheat"]
#     + " Corn "
#     + df["corn"]
# )


# load our data
mtcars = pd.read_csv(
    DATA_DIR / "mtcars_dummy.csv", dtype={"cyl": str, "am": np.float64}
)

# fit, cyl_enc = make_fit(mtcars)


if __name__ == "__main__":
    pass
    # print(preds(fit, cyl_enc, 3650.0, 69.0, 0, "12"))
