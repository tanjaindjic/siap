from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
import pandas as pd
import numpy as np

vina = pd.read_csv("dataCSV.csv")
vina["pointGroup"]=np.where(vina["pointGroup"]<0.1,0, vina["pointGroup"])
vina["pointGroup"]=np.where(vina["pointGroup"]<0.5,1, vina["pointGroup"])
vina["pointGroup"]=np.where(vina["pointGroup"]<0.75,2, vina["pointGroup"])
vina["pointGroup"]=np.where(vina["pointGroup"]<1.1,3, vina["pointGroup"])
trening_set, test_set, validacioni = np.split(vina, [round(len(vina)/5*3), round(len(vina)/5*4)])

gnb = GaussianNB()  # Number of mislabeled points out of a total 21983 points : 6192, performance 71.83%
bnb = BernoulliNB()  # Number of mislabeled points out of a total 21983 points : 7206, performance 67.22%
mnb = MultinomialNB()  # Number of mislabeled points out of a total 21983 points : 6571, performance 70.11%
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
gnb.fit(
    trening_set[used_features].values,
    trening_set["pointGroup"]
)
y_pred = gnb.predict(test_set[used_features])
print("Number of mislabeled points out of a total {} points : {}, performance {:05.2f}%"
    .format(
    test_set.shape[0],
    (test_set["pointGroup"] != y_pred).sum(),
    100 * (1 - (test_set["pointGroup"] != y_pred).sum() / test_set.shape[0])
))
