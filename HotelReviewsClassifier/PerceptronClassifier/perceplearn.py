import glob
import operator
import os
import json
import random
import sys
import string
import math

filelist= []
path=sys.argv[1]
# path= "../PerceptronClassifier/op_spam_training_data"
all_files = glob.glob(os.path.join(sys.argv[1], '*/*/*/*.txt'))
# all_files = glob.glob(os.path.join(path, '*/*/*/*.txt'))
# analysing input
for root, dirs, files in os.walk(path):
    for file in files:
        filelist.append(os.path.join(root, file))
        # print(file)

deceptive_negative=[]
true_negative=[]
true_positive=[]
deceptive_positive=[]
fileslist=[]
filetype=[]
class_data = []
word_frequency = {}
# print all the file names
for name in filelist:
    # print(name)
    if("negative_polarity" in name):
        if("deceptive" in name):
            deceptive_negative.append(name)
            fileslist.append(name)
            filetype.append("nd")
        elif("tru" in name):
            true_negative.append(name)
            fileslist.append(name)
            filetype.append("nt")
    elif("positive_polarity" in name):
        if("deceptive" in name):
            deceptive_positive.append(name)
            fileslist.append(name)
            filetype.append("pd")
        elif ("tru" in name):
            true_positive.append(name)
            fileslist.append(name)
            filetype.append("pt")

paths=[]
for f in all_files:
    class1, class2, fold, fname = f.split('/')[-4:]
    paths.append(f)
dataList=[]
stop_words = ['doing', 'most', "when's", 'at', "they've", 'quite', 'these', 'am', 'as', 'she', 'but', 'he', 'rooms', 'her', 'during', 'after', 'him', "you'll",
            'whom', 'itself', 'some', 'high', 'old', 'once', 'nor', 'his', 'under', 'which', "you've", 'each', 'many', 'ours', 'when',
            "where's", 'for', 'herself', 'from', 'below', 'himself', 'though', 'before', 'ourselves', 'yourselves',
            'your', 'myself', 'are', 'if', 'where', 'until', 'the', 'having', 'too', 'against', 'me', 'further', 'have',
            'over', 'asked', 'our', 'had', 'same', "there's", "how's", 'away', 'you', 'hers', "what's", 'yours',
            'with', 'and', 'between', 'here', 'we', 'what', 'been', 'were', 'should','theirs', 'is', 'do', "i'm", 'being', 'them',
            'said', 'all', "i'd",  'to', 'now', 'on', 'such','their', 'yourself',  'both',  "she's", 'its','that',
            'they', 'down', "she'll", 'i', "we'd", 'could', 'this', "that's", 'of', "they'll", "it's", "who's",
            'there',  "they'd", 'because', 'again',  'does', 'every', 'very', 'next',  'own', 'those', "we're",
            "she'd", "we'll", "here's", 'while',  "he'll", "i've", 'how', 'than', 'or','a', 'an', 'into', 'who', 'why',
            "you're", "they're", "i'll", "he'd", 'by', 'themselves', 'so','only', "you'd",  'ought', 'more',
            'was', 'other',  'out', "we've", 'did', "he's", 'be', 'about', 'my', 'make', 'up', 'two',  'it',
            'then', 'through', 'above', 'also','would', "let's", "why's", 'few', 'any', 'has',  'in', 'a','this'
            ]

for i in range(len(paths)):
    data_type = []
    filedata = open(paths[i]).read()
    filedata = filedata.lower()
    punctuations = string.punctuation
    punctuations = punctuations.replace("\'", "")
    punctuation_list = list(punctuations)
    for j in range(0, len(filedata)):
        if filedata[j] in punctuation_list:
            filedata = filedata[:j] + ' ' + filedata[j + 1:]
    filedata = filedata.replace("\n", '')
    filedata = filedata.split()
    curr_class_name = filetype[i]
    if curr_class_name == "pt":
        data_type.append(1)
        data_type.append(1)
    if curr_class_name == "pd":
        data_type.append(1)
        data_type.append(-1)
    if curr_class_name == "nt":
        data_type.append(-1)
        data_type.append(1)
    if curr_class_name == "nd":
        data_type.append(-1)
        data_type.append(-1)
    wordCount = {}
    for word in filedata:
        if word not in stop_words:
            if word in wordCount.keys():
                count=wordCount[word]+1
                wordCount[word]=count
            else:
                count = 1
                wordCount[word] = count
            if word in word_frequency.keys():
                count1=word_frequency[word]+1
                word_frequency[word]=count1
            else:
                count1 = 0
                word_frequency[word] = count1
    data_type.append(wordCount)
    class_data.append(data_type)
removedwords=[]
word_frequency_final = {}
for feature in word_frequency:
    if word_frequency[feature] > 1:
        word_frequency_final[feature] = word_frequency[feature]
    else:
        removedwords.append(word_frequency[feature])
class_data_final = []
ascending_sorted_map={k: v for k, v in sorted(word_frequency_final.items(), key=lambda item: item[1])}
sorted_map={}
for k in reversed(list(ascending_sorted_map.keys())):
    sorted_map[k]=ascending_sorted_map[k]

for data in class_data:
    data_type = []
    l=[data[0],data[1], data[2] ]
    data_type.extend(l[0:2])
    class_change = {}
    classData = l[2]
    for key in sorted_map.keys():
        if key in classData.keys():
            count=classData[key]
            class_change[key] = count
        else:
            count=0
            class_change[key] = count
    data_type.append(class_change)
    class_data_final.append(data_type)


avg_p  = {"wts_td":{},"bias_td":0,"wts_pn":{},"bias_pn":0}
vanilla  = {"wts_td":{},"bias_td":0,"wts_pn":{},"bias_pn":0}

c = 1

for iter in range(20):
    random.shuffle(class_data_final) 
    converge = 1
    falseres=0
    for data_type_final in class_data_final:
        for i in range(3):
            # print(data_type_final[i])
            pass
        true_deceptive = 0
        expectedTrueDeceptive = data_type_final[1]
        positive_negative = 0
        expectedPositiveNegative = data_type_final[0]
        result = []
        vector = data_type_final[2]
        for feature in sorted_map:
            if feature in vanilla["wts_td"].keys():
                wt_td=vanilla["wts_td"][feature]
            else:
                wt_td=0
            if feature in vanilla["wts_pn"].keys():
                wt_np=vanilla["wts_pn"][feature]
            else:
                wt_np=0
            if feature in vector.keys():
                vect=vector[feature]
            else:
                vect=0
            true_deceptive = true_deceptive + wt_td * vect
            positive_negative = positive_negative + wt_np * vect
        true_deceptive = true_deceptive + vanilla["bias_td"]
        positive_negative = positive_negative + vanilla["bias_pn"]
        result.append(true_deceptive)
        result.append(positive_negative)
        if result[0] * expectedTrueDeceptive <= 0:
            converge = 0 
            for feature in sorted_map:
                if feature in vanilla["wts_td"]:
                    if feature in vector.keys():
                        vect = vector[feature]
                    else:
                        vect = 0
                    vanilla["wts_td"][feature] =vanilla["wts_td"][feature] + expectedTrueDeceptive * vect
                    avg_p ["wts_td"][feature] = avg_p ["wts_td"][feature] + expectedTrueDeceptive * vect * c
                else:
                    if feature in vector.keys():
                        vect = vector[feature]
                    else:
                        vect = 0
                    vanilla["wts_td"][feature] = expectedTrueDeceptive * vect
                    avg_p ["wts_td"][feature] = expectedTrueDeceptive * vect * c

            vanilla["bias_td"] =vanilla["bias_td"] + expectedTrueDeceptive
            avg_p ["bias_td"] = avg_p ["bias_td"] + expectedTrueDeceptive * c
        res=result[1] * expectedPositiveNegative
        if  result[1] * expectedPositiveNegative <= 0:
            converge = 0 
            for feature in sorted_map.keys():
                if feature in vanilla["wts_pn"]:
                    if feature in vector.keys():
                        vect = vector[feature]
                    else:
                        vect = 0
                    vanilla["wts_pn"][feature] =vanilla["wts_pn"][feature] + expectedPositiveNegative * vect
                    avg_p ["wts_pn"][feature] =avg_p ["wts_pn"][feature] + expectedPositiveNegative * vect * c
                else:
                    if feature in vector.keys():
                        vect = vector[feature]
                    else:
                        vect = 0
                    vanilla["wts_pn"][feature] = expectedPositiveNegative * vect
                    avg_p ["wts_pn"][feature] = expectedPositiveNegative * vect * c

            vanilla["bias_pn"] =vanilla["bias_pn"] + expectedPositiveNegative
            avg_p ["bias_pn"] =avg_p ["bias_pn"] + expectedPositiveNegative * c
        else:
            falseres=falseres+1
        c =c + 1
    if converge == 1:
        break 


for feature in  avg_p ["wts_td"]:
     avg_p ["wts_td"][feature] = vanilla["wts_td"][feature] - ( avg_p ["wts_td"][feature] / c)
avg_p ["bias_td"] = vanilla["bias_td"] - (avg_p ["bias_td"] / c)


for feature in avg_p ["wts_pn"]:
    avg_p ["wts_pn"][feature] = vanilla["wts_pn"][feature] - (
                avg_p ["wts_pn"][feature] / c)
avg_p ["bias_pn"] = vanilla["bias_pn"] - (avg_p ["bias_pn"] / c)



vanilla_model = open("vanillamodel.txt", "w")
vanilla_model.write(json.dumps(vanilla ))
avg_model = open("averagedmodel.txt", "w")
avg_model.write(json.dumps(avg_p))