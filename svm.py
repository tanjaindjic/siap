from sklearn import svm
import pandas as pd
import numpy as np

vina = pd.read_csv("dataCSV_embedding.csv")

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
used_features_embedding = ["description","points","price","taster_name","title","variety","winery","pointGroup","longitude","latitude"]

clf = svm.SVC(gamma='scale', decision_function_shape='ovo')
clf.fit(trening_set[used_features_embedding].values,
        trening_set["pointGroup"])
y_pred = clf.predict(test_set[used_features_embedding])
print("Number of mislabeled points out of a total {} points : {}, performance {:05.2f}%"
        .format(
        test_set.shape[0],
        (test_set["pointGroup"] != y_pred).sum(),
        100 * (1 - (test_set["pointGroup"] != y_pred).sum() / test_set.shape[0])
    ))

#Number of mislabeled points out of a total 21983 points : 5454, performance 75.19%
#ERROR TypeError: must be real number, not str line 28 - WORD EMBEDDING