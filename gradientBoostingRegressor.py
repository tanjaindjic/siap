from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd
import numpy as np
from sklearn import ensemble


vina = pd.read_csv("dataCSV.csv")
trening_set, test_set, validacioni = np.split(vina, [round(len(vina)/5*3), round(len(vina)/5*4)])

used_features = [
        "country",
        "province",
        "variety",
        "winery",
        "taster_name",
        "price",
        "title",
        "description"
    ]
gbr = ensemble.GradientBoostingRegressor(n_estimators=500, max_depth=4, min_samples_split=2, learning_rate=0.01, loss='ls')

gbr.fit(
    trening_set[used_features].values,
    trening_set["points"].values)
y_pred = gbr.predict(test_set[used_features])
print("Number of mislabeled points out of a total {} points : {}, performance {:05.2f}%"
        .format(
        test_set.shape[0],
        (test_set["points"] != y_pred).sum(),
        100 * (1 - (test_set["points"] != y_pred).sum() / test_set.shape[0])
    ))
