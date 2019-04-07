from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Ridge
import pandas as pd
import numpy as np

vina = pd.read_csv("dataCSV.csv")
# vina["points"]=np.where(vina["points"]>99, 0, vina["points"])
# vina["points"]=np.where(vina["points"]>98, 1, vina["points"])
# vina["points"]=np.where(vina["points"]>97, 2, vina["points"])
# vina["points"]=np.where(vina["points"]>96, 3, vina["points"])
# vina["points"]=np.where(vina["points"]>95, 4, vina["points"])
# vina["points"]=np.where(vina["points"]>94, 5, vina["points"])
# vina["points"]=np.where(vina["points"]>93, 6, vina["points"])
# vina["points"]=np.where(vina["points"]>92, 7, vina["points"])
# vina["points"]=np.where(vina["points"]>91, 8, vina["points"])
# vina["points"]=np.where(vina["points"]>90, 9, vina["points"])
# vina["points"]=np.where(vina["points"]>89, 10, vina["points"])
# vina["points"]=np.where(vina["points"]>88, 11, vina["points"])
# vina["points"]=np.where(vina["points"]>87, 12, vina["points"])
# vina["points"]=np.where(vina["points"]>86, 13, vina["points"])
# vina["points"]=np.where(vina["points"]>85, 14, vina["points"])
# vina["points"]=np.where(vina["points"]>84, 15, vina["points"])
# vina["points"]=np.where(vina["points"]>83, 16, vina["points"])
# vina["points"]=np.where(vina["points"]>82, 17, vina["points"])
# vina["points"]=np.where(vina["points"]>81, 18, vina["points"])
# vina["points"]=np.where(vina["points"]>80, 19, vina["points"])
# vina["points"]=np.where(vina["points"]>79, 20, vina["points"])

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
clf = Ridge(alpha=0, normalize=True)
clf.fit(
        trening_set[used_features].values,
        trening_set["points"])
y_pred = clf.predict(test_set[used_features])
print("Number of mislabeled points out of a total {} points : {}, performance {:05.2f}%"
        .format(
        test_set.shape[0],
        (test_set["points"] != y_pred).sum(),
        100 * (1 - (test_set["points"] != y_pred).sum() / test_set.shape[0])
    ))
print(mean_squared_error(test_set["points"], y_pred))

