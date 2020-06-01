import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

from src.appdash.constants import DATA_DIR


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


# load our data
mtcars = pd.read_csv(
    DATA_DIR / "mtcars_dummy.csv", dtype={"cyl": str, "am": np.float64}
)

fit, cyl_enc = make_fit(mtcars)


if __name__ == "__main__":
    print(preds(fit, cyl_enc, 3650.0, 69.0, 0, "12"))
