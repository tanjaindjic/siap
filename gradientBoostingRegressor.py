from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd
import numpy as np

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
clf = GradientBoostingRegressor()
clf.fit(trening_set[used_features].values,
        trening_set["points"])
y_pred = clf.predict(test_set[used_features])
print("Number of mislabeled points out of a total {} points : {}, performance {:05.2f}%"
        .format(
        test_set.shape[0],
        (test_set["points"] != y_pred).sum(),
        100 * (1 - (test_set["points"] != y_pred).sum() / test_set.shape[0])
    ))
