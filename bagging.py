from sklearn.ensemble import BaggingClassifier
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
        "title",
        "price",
        "description"
    ]
#clf1 = BaggingClassifier(KNeighborsClassifier(), max_samples=0.5, max_features=0.5)

clf = BaggingClassifier(n_estimators=50, warm_start=False, random_state=3141)
clf.fit(trening_set[used_features].values,
        trening_set["pointGroup"])
y_pred = clf.predict(test_set[used_features])
print("Number of mislabeled points out of a total {} points : {}, performance {:05.2f}%"
        .format(
        test_set.shape[0],
        (test_set["pointGroup"] != y_pred).sum(),
        100 * (1 - (test_set["pointGroup"] != y_pred).sum() / test_set.shape[0])
    ))
#Number of mislabeled points out of a total 21983 points : 7363, performance 66.51%
#Number of mislabeled points out of a total 21983 points : 5032, performance 77.11% -> CLF1 - Bagging meta-estimator
