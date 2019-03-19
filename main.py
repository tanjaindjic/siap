import json
from vino import Vino
import statistics
import numpy as np
import pip
print(pip.__version__)
import nltk
import re
#from nltk.corpus import stopwords
from atributes import Atribut
#stop_words = set(stopwords.words('english'))
#stop_words.add("the")
from collections import Counter

from pprint import pprint
import matplotlib.pyplot as plt

vazne_reci = []
atributi = []
categs = []

def get_important_words(vreca):
    cnt = Counter(vreca)
    vazne_reci = []
    vazne_reci.append([k for k, v in cnt.items() if v > 100])
    return vazne_reci

def word_extraction(sentence):
    sentence = sentence.lower()
    words = re.sub("[^\w]", " ", sentence).split()
    #cleaned_text = [w.lower() for w in words if w not in stop_words]
    #return cleaned_text
############################
def descriptionIsEnglish(sentence):
    try:
        sentence.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    return True
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
    for c in categs:
        if(c in kategorije):
            vec.append(1)
        else:
            vec.append(0)
    return (vec)
def loadAtributes():
    f = open("CWW.txt", "r")
    for x in f:
        rez = x.split('\t')
        saZnakom = rez[3].split('\n');
        rez[3] = saZnakom[0]
        atributi.append(Atribut(rez[0], rez[1], rez[2], rez[3], 1))
        str1111 = rez[0] + " " + rez[1] + " " + rez[2]
        if str1111 not in categs:
            categs.append(str1111)

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

def tokenize(sentences):
    words = []

    vazne_reci = get_important_words(sentences)
    for sentence in vazne_reci:
        #print(sentence)
        sentence = isEnglish(sentence)
        words.extend(sentence)
    words = sorted(list(set(words)))

    return words





loadAtributes()
with open('winemag-data-130k-v2.json') as f:
    data = json.load(f)
print('velicina data seta: ' + str(len(data)))
vina = []
vreca = []
for v in data:
    if (v['points'] is not None and v['country'] is not None and v['variety'] is not None and v['title'] is not None):
        if (descriptionIsEnglish(v['description'])):
            vec = get_word_vec(v['description'])
            print(vec)
            vina.append(Vino(v['country'], v['description'], v['points'], v['price'], v['province'], v['taster_name'],  v['title'], v['variety'],  v['winery']))


print('velicina data seta nakon uklanjanja suvisnih podataka: ' + str(len(vina)))
#print(str(round(len(vina)/5*3)) + " " + str(round(len(vina)/5*4)))
trening_set, test_set, validacioni = np.split(vina, [round(len(vina)/5*3), round(len(vina)/5*4)])
#for v in trening_set:
#    vreca.extend(word_extraction(v.description))
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