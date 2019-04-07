from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error
from sklearn.metrics import f1_score
import pandas as pd
import numpy as np

vina = pd.read_csv("dataCSV.csv")

vina["pointGroup"]=np.where(vina["pointGroup"]<0.1,0, vina["pointGroup"])
vina["pointGroup"]=np.where(vina["pointGroup"]<0.5,1, vina["pointGroup"])
vina["pointGroup"]=np.where(vina["pointGroup"]<0.75,2, vina["pointGroup"])
vina["pointGroup"]=np.where(vina["pointGroup"]<1.1,3, vina["pointGroup"])

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
clf = RandomForestClassifier(n_estimators=225, max_depth=27, random_state=3)
clf.fit(trening_set[used_features].values,
        trening_set["pointGroup"])
y_pred = clf.predict(test_set[used_features])
print("Number of mislabeled points out of a total {} points : {}, performance {:05.2f}%"
        .format(
        test_set.shape[0],
        (test_set["pointGroup"] != y_pred).sum(),
        100 * (1 - (test_set["pointGroup"] != y_pred).sum() / test_set.shape[0])
    ))

print(mean_squared_error(test_set["pointGroup"], y_pred))
print(f1_score(test_set["pointGroup"], y_pred, average='macro'))
print(f1_score(test_set["pointGroup"], y_pred, average='micro'))
print(f1_score(test_set["pointGroup"], y_pred, average=None))
#Number of mislabeled points out of a total 21983 points : 4605, performance 79.05%
#Number of mislabeled points out of a total 21983 points : 4300, performance 80.54% <- BEZ TITLE ATRIBUTA
