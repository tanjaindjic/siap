import json
from vino import Vino
from latlon_vino import LLVino
from atribut import Atribut
import statistics
import numpy as np
import pip
print(pip.__version__)
import re
import csv
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from geopy.geocoders import Nominatim
vazne_reci = []
atributi = []
allCategs = []
vecNajVina = []
zaPoredjenje = []
noveTezine = []

############################
def descriptionIsEnglish(sentence):
    try:
        sentence.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    return True
def loadAtributes():
    f = open("CWW.txt", "r")
    for x in f:
        rez = x.split('\t')
        saZnakom = rez[3].split('\n');
        rez[3] = saZnakom[0]
        atributi.append(Atribut(rez[0], rez[1], rez[2], rez[3]))
        str1111 = rez[0] + " " + rez[1] + " " + rez[2]
        if str1111 not in allCategs:
            allCategs.append(str1111)
    print('duzina vektora sa kategorijama - '+str(len(allCategs)))
def loadTezine():
    data = []
    for nv in najboljaVina:
        data.append(nv.__getattribute__('description'))
    print("data len: "+str(len(data)))
    sentences = [TaggedDocument(sentence, 'tag') for sentence in data]
    model = Doc2Vec(sentences, window=1, min_count=1, workers=1)
    model.train(sentences, epochs=model.iter, total_examples=model.corpus_count)
    print("duzina: "+str(len(model.docvecs)))
    print("nulti: "+str(model.docvecs[0]))
    print("prvi: "+str(model.docvecs[1]))
    print("drugi: "+str(model.docvecs[2]))
    for v0 in vina:
        description = v0.__getattribute__('description')
        words = []
        for i in sent_tokenize(description):
            temp = []
            for j in word_tokenize(i):
                temp.append(j.lower())
            words.append(temp)
        descNum = model.rank(sentences, words)
        v0.__setattr__('description', descNum)
        print("Doc2Vec: "+str(descNum))

#####################
def isEnglish(s):
    niz = []

    for sentence in s:
        try:
            sentence.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            print("")
        else:
            if(not sentence.isdigit()):
                niz.append(sentence)
    return niz




loadAtributes()
with open('winemag-data-130k-v2.json') as f:
    data = json.load(f)
print('velicina data seta: ' + str(len(data)))
vina = []
vreca = []
najboljaVina=[]
for v in data:
    if (v['points'] is not None and v['country'] is not None and v['variety'] is not None and v['title'] is not None):
        if (descriptionIsEnglish(v['description'])):
            vina.append(Vino.initialize(Vino(), v['country'], v['description'], v['points'], v['price'], v['province'], v['taster_name'],  v['title'], v['variety'],  v['winery'], 0))
            if(int(v['points'])>96):
                najboljaVina.append(Vino.initialize(Vino(), v['country'], v['description'], v['points'], v['price'], v['province'], v['taster_name'],  v['title'], v['variety'],  v['winery'], 0))
print('najbolja vina - duzina '+str(len(najboljaVina)))
#njabolja vina - duzina --> za >97 se dobija 82, za >96 232, za >95 570
countriesProvince = []
for v0 in vina:
    if(v0.__getattribute__('province') is not None):
        spojeno = v0.__getattribute__('province')+", "+v0.__getattribute__('country')
    else:
        spojeno = v0.__getattribute__('country')

    if spojeno not in countriesProvince:
        countriesProvince.append(spojeno)


listaKoordinata = []
for cp in countriesProvince:
    geolocator = Nominatim(user_agent="SIAP")
    location = geolocator.geocode(cp)
    listaKoordinata.append(location)
dictionaryLokacija = dict(zip(countriesProvince, listaKoordinata))

print("dzuina countriesProvince: "+str(len(countriesProvince)))
print(countriesProvince)
print('velicina data seta nakon uklanjanja suvisnih podataka: ' + str(len(vina)))
loadTezine()
nizDescriptiona = []
#for v0 in vina[:2000]:

# for v in vina:
#   vreca.extend(word_extraction(v.description))
#print(vreca)
#tokeni =  tokenize(vreca)
#print(tokeni)
#print("velicina tokena: " + str(tokeni.__len__()))
k1=[] #solidan kvalitet vina
k2=[] #vrlo dobar kvalitet vina
k3=[] #izuzetno dobar kvalitet
k4=[] #savrsen kvalitet
for v in vina:
    if(v.price is not None):
        if(int(v.points) < 85):
            k1.append(int(v.price))
        elif(int(v.points) < 90):
            k2.append(int(v.price))
        elif (int(v.points) < 95):
            k3.append(int(v.price))
        else:
            k4.append(int(v.price))
print('k1 - broj vina solidnog kvaliteta (80-84 poena): ' + str(len(k1)))
print('k2 - broj vina vrlo dobrog kvaliteta (85-90 poena): ' + str(len(k2)))
print('k3 - broj vina izuzetno dobrog kvaliteta (90-94 poena): ' + str(len(k3)))
print('k4 - broj vina savrsenog kvaliteta (95-100 poena): ' + str(len(k4)))

prosek_k1 = statistics.median(k1)
print('prosecna cena k1: ' + str(prosek_k1) + '$')
prosek_k2 = statistics.median(k2)
print('prosecna cena k2: ' + str(prosek_k2) + '$')
prosek_k3 = statistics.median(k3)
print('prosecna cena k3: ' + str(prosek_k3) + '$')
prosek_k4 = statistics.median(k4)
print('prosecna cena k4: ' + str(prosek_k4) + '$')
pairs_k1 = []
pairs_k2 = []
pairs_k3 = []
pairs_k4 = []
for v in vina:

    if (v.price is None):
        if (int(v.points) < 85):
            v.price = prosek_k1
            pair = [int(v.price), int(v.points)]
            pairs_k1.append(pair)
        elif (int(v.points) < 90):
            v.price = prosek_k2
            pair = [int(v.price), int(v.points)]
            pairs_k2.append(pair)
        elif (int(v.points) < 95):
            v.price = prosek_k3
            pair = [int(v.price), int(v.points)]
            pairs_k3.append(pair)
        else:
            v.price = prosek_k4
            pair = [int(v.price), int(v.points)]
            pairs_k4.append(pair)
    else:
        if (int(v.points) < 85):
            pair = [int(v.price), int(v.points)]
            pairs_k1.append(pair)
        elif (int(v.points) < 90):
            pair = [int(v.price), int(v.points)]
            pairs_k2.append(pair)
        elif (int(v.points) < 95):
            pair = [int(v.price), int(v.points)]
            pairs_k3.append(pair)
        else:
            pair = [int(v.price), int(v.points)]
            pairs_k4.append(pair)




axes = plt.gca()
axes.set_xlim([0,1000])
axes.set_xlabel('Cena')
axes.set_title('Odnos cene i kvalilteta')
axes.set_ylabel('Poeni')
a = np.array(pairs_k1)
#plt.plot(a[:,0], a[:,1], 'ro')
a = np.array(pairs_k2)
#plt.plot(a[:,0], a[:,1], 'mo')
a = np.array(pairs_k3)
#plt.plot(a[:,0], a[:,1], 'yo')
a = np.array(pairs_k4)
#plt.plot(a[:,0], a[:,1], 'go')
#plt.show()
#print(str(vina[0]))
#print(str(vina[1]))

#trening_set, test_set, validacioni = np.split(vina, [round(len(vina)/5*3), round(len(vina)/5*4)])
def makeCSVfile():
    countries = []
    provinces = []
    varieties = []
    wineries = []
    taster_names = []
    titles = []

    for v in vina:
        if v.__getattribute__('variety') not in varieties:
            varieties.append(v.__getattribute__('variety'))
        if v.__getattribute__('winery') not in wineries:
            wineries.append(v.__getattribute__('winery'))
        if v.__getattribute__('taster_name') not in taster_names:
            taster_names.append(v.__getattribute__('taster_name'))
        if v.__getattribute__('title') not in titles:
            titles.append(v.__getattribute__('title'))
    len_countries = len(countries)
    len_provinces = len(provinces)
    len_varieties = len(varieties)
    len_wineries = len(wineries)
    len_taster_names = len(taster_names)
    len_title = len(titles)
    ll_vina = []
    for v in vina:
        ll = LLVino.initialize(LLVino(), 0, v.__getattribute__('description'), v.__getattribute__('points'), v.__getattribute__('price'), 0,v.__getattribute__('taster_name'), v.__getattribute__('title'), v.__getattribute__('variety'), v.__getattribute__('winery'), v.__getattribute__('pointGroup'))
        if (v.__getattribute__('province') is not None):
            spojeno = v.__getattribute__('province') + ", " + v.__getattribute__('country')
        else:
            spojeno = v.__getattribute__('country')
        loc = dictionaryLokacija[spojeno]
        ll.__setattr__('longitude', loc.longitude)
        ll.__setattr__('latitude', loc.latitude)


        variety_index = varieties.index(v.__getattribute__('variety')) + 1
        value_variety = (1 / len_varieties) * variety_index
        ll.__setattr__('variety', value_variety)

        winery_index = wineries.index(v.__getattribute__('winery')) + 1
        value_winery = (1 / len_wineries) * winery_index
        ll.__setattr__('winery', value_winery)

        taster_name_index = taster_names.index(v.__getattribute__('taster_name')) + 1
        value_taster_name = (1 / len_taster_names) * taster_name_index
        ll.__setattr__('taster_name', value_taster_name)

        title_index = titles.index(v.__getattribute__('title')) + 1
        value_title = (1 / len_title) * title_index
        ll.__setattr__('title', value_title)

        if (int(v.__getattribute__('points')) < 85):
            ll.__setattr__('pointGroup', 0)
        elif (int(v.__getattribute__('points')) < 90):
            ll.__setattr__('pointGroup', 1)
        elif (int(v.__getattribute__('points')) < 95):
            ll.__setattr__('pointGroup', 2)
        else:
            ll.__setattr__('pointGroup', 3)
        ll_vina.append(ll)
    with open('dataCSV_embedding.csv', 'w', ) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ['longitude', 'description', 'points', 'price', 'latitude', 'taster_name', 'title', 'variety', 'winery',
             'pointGroup'])
        for d in ll_vina:
            writer.writerow(
                [d.__getattribute__('longitude'), d.__getattribute__('description'), d.__getattribute__('points'),
                 d.__getattribute__('price'), d.__getattribute__('latitude'), d.__getattribute__('taster_name'),
                 d.__getattribute__('title'), d.__getattribute__('variety'), d.__getattribute__('winery'),
                 d.__getattribute__('pointGroup')])
    print("zavrsio4")
