from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error


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
gbr = GradientBoostingClassifier()

gbr.fit(
    trening_set[used_features].values,
    trening_set["points"])
y_pred = gbr.predict(test_set[used_features])
print("Number of mislabeled points out of a total {} points : {}, performance {:05.2f}%"
        .format(
        test_set.shape[0],
        (test_set["points"] != y_pred).sum(),
        100 * (1 - (test_set["points"] != y_pred).sum() / test_set.shape[0])
    ))

print(mean_squared_error(test_set["points"], y_pred))

#Number of mislabeled points out of a total 21983 points : 19013, performance 13.51%
#mean_squared_error = 11.610335259063822