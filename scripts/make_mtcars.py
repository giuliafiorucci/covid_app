if __name__ == "__main__":
    from appdash.constants import DATA_DIR
    import pandas as pd
    import numpy as np

    OUTPUT_FILE = DATA_DIR / "mtcars_dummy.csv"
    np.random.seed(31415)

    n_cars = 100
    mtcars = pd.DataFrame(
        data=None, index=None, columns=["disp", "qsec", "am", "cyl", "mpg"]
    )
    mtcars["disp"] = np.random.uniform(1200, 5000, n_cars)
    mtcars["qsec"] = np.random.uniform(30, 90, n_cars)
    mtcars["am"] = np.random.choice([True, False], n_cars).astype(int)
    mtcars["cyl"] = np.random.choice([4, 6, 8, 10, 12], n_cars).astype(int)
    mtcars["mpg"] = np.random.uniform(20, 150, n_cars)

    mtcars.to_csv(OUTPUT_FILE, index=False)
