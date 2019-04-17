from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error


vina = pd.read_csv("dataCSV_embedding.csv")
trening_set, test_set, validacioni = np.split(vina, [round(len(vina)/5*3), round(len(vina)/5*4)])

used_features = [
        "country",
        "province",
        "variety",
        "taster_name",
        "price",
        "description"
    ]
used_features_embedding = ["description","price","taster_name","title","variety","winery","longitude","latitude"]
gbr = GradientBoostingClassifier()

gbr.fit(
    trening_set[used_features_embedding].values,
    trening_set["points"])
y_pred = gbr.predict(test_set[used_features_embedding])
print("Number of mislabeled points out of a total {} points : {}, performance {:05.2f}%"
        .format(
        test_set.shape[0],
        (test_set["points"] != y_pred).sum(),
        100 * (1 - (test_set["points"] != y_pred).sum() / test_set.shape[0])
    ))

print(mean_squared_error(test_set["points"], y_pred))

#Number of mislabeled points out of a total 21983 points : 19013, performance 13.51%
#mean_squared_error = 11.610335259063822

#Number of mislabeled points out of a total 21983 points : 17491, performance 20.43% <- BEZ TITLE ATRIBUTA, WINERY
#5.2263112405040255

#Number of mislabeled points out of a total 21983 points : 19026, performance 13.45% - WORD EMBEDDING
#11.7876540963