from sklearn.metrics import jaccard_similarity_score
import formData

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
    treningSet = formData.convertFromJson("validacioni")
    # for v in data:
    #     treningSet.append(Vino.initialize(Vino(), v['country'], v['description'], v['points'], v['price'], v['province'],
    #                             v['taster_name'], v['title'], v['variety'], v['winery'], 0))
def processTreningSet():
    # print("length: "+str(len(treningSet)))
    for v in treningSet:
        if v['country'] not in countries:
            countries.append(v['country'])
        if v['province'] not in provinces:
            provinces.append(v['province'])
        if v['variety'] not in varieties:
            varieties.append(v['variety'])
        if v['winery'] not in wineries:
            wineries.append(v['winery'])
        if v['taster_name'] not in taster_names:
            taster_names.append(v['taster_name'])
        if v['title'] not in titles:
            titles.append(v['title'])
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
        country_index = countries.index(v['country'])+1
        value_country = (1/len_countries)*country_index
        v['country'] =  value_country


        province_index = provinces.index(v['province'])+1
        value_province = (1/len_provinces)*province_index
        v['province'] =  value_province

        variety_index = varieties.index(v['variety']) + 1
        value_variety = (1 / len_varieties) * variety_index
        v['variety'] =  value_variety


        winery_index = wineries.index(v['winery']) + 1
        value_winery = (1 / len_wineries) * winery_index
        v['winery'] =  value_winery

        taster_name_index = taster_names.index(v['taster_name']) + 1
        value_taster_name = (1 / len_taster_names) * taster_name_index
        v['taster_name'] =  value_taster_name

        title_index = titles.index(v['title']) + 1
        value_title = (1 / len_title) * title_index
        v['title'] =  value_title

        if(int(v['points'])<85):
           v['points'] =  0
        elif(int(v['points'])<90):
           v['points'] =  0.33
        elif(int(v['points'])<95):
           v['points'] =  0.67
        else:
           v['points'] =  1

def loadTestSet():
    testSet = formData.convertFromJson("test")
    # for v in data:
    #     testSet.append(
    #         Vino.initialize(Vino(), v['country'], v['description'], v['points'], v['price'], v['province'],
    #                         v['taster_name'], v['title'], v['variety'], v['winery'], 0))
def processTestSet():
    len_countries = len(countries)
    len_provinces = len(provinces)
    len_varieties = len(varieties)
    len_wineries = len(wineries)
    len_taster_names = len(taster_names)
    len_title = len(titles)
    for v in testSet:
        if v['country'] not in countries:
            v['country'] = 0
        else:
            country_index = countries.index(v['country'])+1
            value_country = (1/len_countries)*country_index
            v['country'] = value_country

        if v['province'] not in provinces:
           v['province'] = 0
        else:
            province_index = provinces.index(v['province'])+1
            value_province = (1/len_provinces)*province_index
            v['province'] = value_province

        if v['variety'] not in varieties:
            v['variety'] = 0
        else:
            variety_index = varieties.index(v['variety']) + 1
            value_variety = (1 / len_varieties) * variety_index
            v['variety'] = value_variety

        if v['winery'] not in wineries:
            v['winery'] = 0
        else:
            winery_index = wineries.index(v['winery']) + 1
            value_winery = (1 / len_wineries) * winery_index
            v['winery'] = value_winery

        if v['taster_name'] not in taster_names:
            v['taster_name'] = 0
        else:
            taster_name_index = taster_names.index(v['taster_name']) + 1
            value_taster_name = (1 / len_taster_names) * taster_name_index
            v['taster_name'] = value_taster_name

        if v['title'] not in titles:
            v['title'] = 0
        else:
            title_index = titles.index(v['title']) + 1
            value_title = (1 / len_title) * title_index
            v['title'] =  value_title

        if (int(v['points']) < 85):
            v['points'] = 0
        elif (int(v['points']) < 90):
            v['points'] = 0.33
        elif (int(v['points']) < 95):
            v['points'] = 0.67
        else:
            v['points'] = 1


def naiveBayes():
    gnb = GaussianNB()
    used_features = [
        "country",
        "province",
        "variety",
        "winery",
        "taster_name",
        "title"
    ]
    gnb.fit(
        treningSet[used_features].values,
        treningSet["points"]
    )
    y_pred = gnb.predict(testSet[used_features])
    print("Number of mislabeled points out of a total {} points : {}, performance {:05.2f}%"
        .format(
        testSet.shape[0],
        (testSet["points"] != y_pred).sum(),
        100 * (1 - (testSet["points"] != y_pred).sum() / testSet.shape[0])
    ))

loadTreningSet()
print("zavrsio1")
processTreningSet()
print("zavrsio2")
loadTestSet()
print("zavrsio3")
processTestSet()
print("zavrsio4")
naiveBayes()
