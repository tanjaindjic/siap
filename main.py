from sklearn.metrics import jaccard_similarity_score
import formData
import pandas as pd
import numpy as np
import csv
from vino import Vino
import nltk
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
atributi = []
allCategs = []
zaPoredjenje = []
noveTezine = []
treningSet = []
testSet = []

####################
countries = []
provinces = []
varieties = []
wineries = []
taster_names = []
titles = []
############

def get_word_vec(sentence):
    vec = []
    kategorije = []
    sentence = sentence.upper();
    for a in atributi:
        word = a.__getattribute__('normalized')
        if(word in sentence):
            str = a.__getattribute__('category') + " " +  a.__getattribute__('subcategory') + " " +  a.__getattribute__('specific')
            if str not in kategorije:
                kategorije.append(str)
    for c in allCategs:
        if(c in kategorije):
            vec.append(1)
        else:
            vec.append(0)
    return vec
def nadjiDescNum(description):
    y_pred = get_word_vec(description)
   # y_pred = list(map(lambda x,y:x*y,y_pred,noveTezine))
    ret = jaccard_similarity_score(zaPoredjenje, y_pred, True, noveTezine)
   # print('description --> '+str(ret))
    return ret
def nadjiTitlove():
    dataSetic = formData.convertFromJson("trening")
    for ds in dataSetic:
        print(ds['title'])
def loadTreningSet():
    data = formData.convertFromJson("trening")
    for v in data:
        treningSet.append(Vino.initialize(Vino(), v['country'], v['description'], v['points'], v['price'], v['province'],
                                v['taster_name'], v['title'], v['variety'], v['winery'], 0))
def processTreningSet():
    # print("length: "+str(len(treningSet)))
    for v in treningSet:
        if v.__getattribute__('country') not in countries:
            countries.append(v.__getattribute__('country'))
        if v.__getattribute__('province') not in provinces:
            provinces.append(v.__getattribute__('province'))
        if v.__getattribute__('variety') not in varieties:
            varieties.append(v.__getattribute__('variety'))
        if v.__getattribute__('winery') not in wineries:
            wineries.append(v.__getattribute__('winery'))
        if v.__getattribute__('taster_name') not in taster_names:
            taster_names.append(v.__getattribute__('taster_name'))
        if v.__getattribute__('title') not in titles:
            titles.append(v.__getattribute__('title'))
            #print(v['title'])
    # print("countries: "+str(len(countries)))
    # print("provinces: "+str(len(provinces)))
    # print("varieties: "+str(len(varieties)))
    # print("wineries: "+str(len(wineries)))
    # print("taster_names: "+str(len(taster_names)))
    # print("titles: "+str(len(titles)))
    len_countries = len(countries)
    len_provinces = len(provinces)
    len_varieties = len(varieties)
    len_wineries = len(wineries)
    len_taster_names = len(taster_names)
    len_title = len(titles)
    for v in treningSet:
        country_index = countries.index(v.__getattribute__('country')) + 1
        value_country = (1 / len_countries) * country_index
        v.__setattr__('country', value_country)

        province_index = provinces.index(v.__getattribute__('province')) + 1
        value_province = (1 / len_provinces) * province_index
        v.__setattr__('province', value_province)

        variety_index = varieties.index(v.__getattribute__('variety')) + 1
        value_variety = (1 / len_varieties) * variety_index
        v.__setattr__('variety', value_variety)

        winery_index = wineries.index(v.__getattribute__('winery')) + 1
        value_winery = (1 / len_wineries) * winery_index
        v.__setattr__('winery', value_winery)

        taster_name_index = taster_names.index(v.__getattribute__('taster_name')) + 1
        value_taster_name = (1 / len_taster_names) * taster_name_index
        v.__setattr__('taster_name', value_taster_name)

        title_index = titles.index(v.__getattribute__('title')) + 1
        value_title = (1 / len_title) * title_index
        v.__setattr__('title', value_title)

        if(int(v.__getattribute__('points'))<85):
           v.__setattr__('points', 0)
        elif(int(v.__getattribute__('points'))<90):
           v.__setattr__('points', 0.33)
        elif(int(v.__getattribute__('points'))<95):
           v.__setattr__('points', 0.67)
        else:
           v.__setattr__('points', 1)

def loadTestSet():
    data = formData.convertFromJson("test")
    for v in data:
        testSet.append(
            Vino.initialize(Vino(), v['country'], v['description'], v['points'], v['price'], v['province'],
                            v['taster_name'], v['title'], v['variety'], v['winery'], 0))
def processTestSet():
    len_countries = len(countries)
    len_provinces = len(provinces)
    len_varieties = len(varieties)
    len_wineries = len(wineries)
    len_taster_names = len(taster_names)
    len_title = len(titles)
    for v in testSet:
        if v.__getattribute__('country') not in countries:
            v.__setattr__('country', 0)
        else:
            country_index = countries.index(v.__getattribute__('country')) + 1
            value_country = (1 / len_countries) * country_index
            v.__setattr__('country', value_country)

        if v.__getattribute__('province') not in provinces:
           v.__setattr__('province', 0)
        else:
            province_index = provinces.index(v.__getattribute__('province')) + 1
            value_province = (1 / len_provinces) * province_index
            v.__setattr__('province', value_province)

        if v.__getattribute__('variety') not in varieties:
            v.__setattr__('variety', 0)
        else:
            variety_index = varieties.index(v.__getattribute__('variety')) + 1
            value_variety = (1 / len_varieties) * variety_index
            v.__setattr__('variety', value_variety)

        if v.__getattribute__('winery') not in wineries:
            v.__setattr__('winery',  0)
        else:
            winery_index = wineries.index(v.__getattribute__('winery')) + 1
            value_winery = (1 / len_wineries) * winery_index
            v.__setattr__('winery', value_winery)

        if v.__getattribute__('taster_name') not in taster_names:
            v.__setattr__('taster_name', 0)
        else:
            taster_name_index = taster_names.index(v.__getattribute__('taster_name')) + 1
            value_taster_name = (1 / len_taster_names) * taster_name_index
            v.__setattr__('taster_name', value_taster_name)

        if v.__getattribute__('title') not in titles:
            v.__setattr__('title',  0)
        else:
            title_index = titles.index(v.__getattribute__('title')) + 1
            value_title = (1 / len_title) * title_index
            v.__setattr__('title', value_title)

        if (int(v.__getattribute__('points')) < 85):
            v.__setattr__('points', 0)
        elif (int(v.__getattribute__('points')) < 90):
            v.__setattr__('points', 0.33)
        elif (int(v.__getattribute__('points')) < 95):
            v.__setattr__('points', 0.67)
        else:
            v.__setattr__('points', 1)



def naiveBayes():
    gnb = GaussianNB()#Number of mislabeled points out of a total 21983 points : 7215, performance 67.18%
    bnb = BernoulliNB()#Number of mislabeled points out of a total 21983 points : 7206, performance 67.22%
    mnb = MultinomialNB()#Number of mislabeled points out of a total 21983 points : 7206, performance 67.22%
    used_features = [
        "country",
        "province",
        "variety",
        "winery",
        "taster_name",
        "title"
    ]
   # treningFrame = pd.DataFrame(np.array(treningSet).reshape(len(treningSet), 10), columns=['country', 'description', 'points', 'price', 'province', 'taster_name', 'title', 'variety', 'winery', 'pointGroup'])
   # testFrame = pd.DataFrame(np.array(testSet).reshape(len(testSet), 10), columns=['country', 'description', 'points', 'price', 'province', 'taster_name', 'title', 'variety', 'winery', 'pointGroup'])
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

# loadTreningSet()
# print("zavrsio1")
# processTreningSet()
# print("zavrsio2")
# #loadTestSet()
# print("zavrsio3")
# #processTestSet()
# print("test: "+str(len(testSet)))
# print("trening: "+str(len(treningSet)))
# with open('treningCSV.csv', 'w',) as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['country', 'description', 'points', 'price', 'province', 'taster_name', 'title', 'variety', 'winery', 'pointGroup'])
#     for d in treningSet:
#         writer.writerow([d.__getattribute__('country'), d.__getattribute__('description'), d.__getattribute__('points'), d.__getattribute__('price'), d.__getattribute__('province'), d.__getattribute__('taster_name'), d.__getattribute__('title'), d.__getattribute__('variety'), d.__getattribute__('winery'), d.__getattribute__('pointGroup')])
# print("zavrsio4")
vina = pd.read_csv("dataCSV.csv")
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(vina[:10])
#vina["pointGroup"]=np.where(vina["pointGroup"]!="",float(vina["pointGroup"]), 0)
vina["pointGroup"]=np.where(vina["pointGroup"]<0.1,0, vina["pointGroup"])
vina["pointGroup"]=np.where(vina["pointGroup"]<0.5,1, vina["pointGroup"])
vina["pointGroup"]=np.where(vina["pointGroup"]<0.75,2, vina["pointGroup"])
vina["pointGroup"]=np.where(vina["pointGroup"]<1.1,3, vina["pointGroup"])
trening_set, test_set, validacioni = np.split(vina, [round(len(vina)/5*3), round(len(vina)/5*4)])
naiveBayes()#Number of mislabeled points out of a total 21983 points : 7215, performance 67.18%
