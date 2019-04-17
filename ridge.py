from sklearn.metrics import mean_squared_error
from sklearn.linear_model import RidgeClassifier
import pandas as pd
import numpy as np

vina = pd.read_csv("dataCSV_embedding.csv")

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
used_features_embedding = ["description","price","taster_name","title","variety","winery","longitude","latitude"]
clf = RidgeClassifier(alpha=20)
#parametters = {'alpha': [1e-15, 1e-10, 1e-8, 1e-4, 1e-2, 1, 5, 10, 20]}
#rr = GridSearchCV(clf, parametters, scoring='neg_mean_squared_error', cv=5)
clf.fit(
        trening_set[used_features_embedding].values,
        trening_set["points"])
y_pred = clf.predict(test_set[used_features_embedding])
print("Number of mislabeled points out of a total {} points : {}, performance {:05.2f}%"
        .format(
        test_set.shape[0],
        (test_set["points"] != y_pred).sum(),
        100 * (1 - (test_set["points"] != y_pred).sum() / test_set.shape[0])
    ))
print(mean_squared_error(test_set["points"], y_pred))

#Number of mislabeled points out of a total 21983 points : 18460, performance 16.03%
#7.102533776099714

#Number of mislabeled points out of a total 21983 points : 18557, performance 15.58% - WORD EMBEDDING
#7.44538961925