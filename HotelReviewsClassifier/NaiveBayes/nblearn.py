import glob
import os
import json
import sys
import string
import math

filelist= []
# path=sys.argv[1]
path="./op_spam_training_data"


# analysing input

for root, dirs, files in os.walk(path):
    for file in files:
        # append the file name to the list
        filelist.append(os.path.join(root, file))
        # print(file)

deceptive_negative=[]
true_negative=[]
true_positive=[]
deceptive_positive=[]
fileslist=[]
filetype=[]
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

total_files_count=len(fileslist)
count_nd=0
count_pd=0
count_nt=0
count_pt=0
# print(deceptive_negative)
# print("\n\n\n\n")
# print(deceptive_positive)
# print("\n\n\n\n")
# print(true_positive)
# print("\n\n\n\n")
# print(true_negative)

paths=[]
class_name=[]

# all_files = glob.glob(os.path.join(sys.argv[1], '*/*/*/*.txt'))
all_files = glob.glob(os.path.join("./op_spam_training_data", '*/*/*/*.txt'))

for f in all_files:
      #print(f)
      class1, class2, fold, fname = f.split('/')[-4:]
      paths.append(f)

# reading input data and data cleaning
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
    filedata=open(paths[i]).read()
    filedata=filedata.lower()
    punctuations = string.punctuation
    punctuations = punctuations.replace("\'","")
    punctuation_list = list(punctuations)
    for i in range(0, len(filedata)):
            if filedata[i] in punctuation_list:
                filedata = filedata[:i] + ' ' + filedata[i+1:]
    filedata=filedata.replace("\n",'')
    filedata=filedata.split()
    filedata2=list(filedata)
    for word in filedata:               #check later for possible errors
        if word in stop_words:
            filedata2.remove(word)
    dataList.append(filedata2)
# if "a" in stop_words:
#     print("true")

# performing naive bayes algorithm

for i in range(len(dataList)):
    length=len(dataList[i])
    if filetype[i] == "nd":
        count_nd += length
    elif filetype[i]=="nt":
        count_nt+=length
    elif filetype[i] == "pd":
        count_pd += length
    elif filetype[i] == "pt":
        count_pt += length
class_counts={"nd":count_nd,"nt":count_nt,"pd":count_pd,"pt":count_pt}
class_word_frequency={"nd":{},"nt":{},"pd":{},"pt":{}}
word_frequency = {}
for i in range(len(dataList)):
    for j in range(len(dataList[i])):
        word=dataList[i][j]
        count=0
        if filetype[i] == "nd":
            if word in class_word_frequency["nd"]:
                count=class_word_frequency["nd"][word] +1
                class_word_frequency["nd"][word]=count
            else:
                class_word_frequency["nd"][word] = 1
        elif filetype[i]=="nt":
            if word in class_word_frequency["nt"]:
                count = class_word_frequency["nt"][word] + 1
                class_word_frequency["nt"][word] = count
            else:
                class_word_frequency["nt"][word] = 1
        elif filetype[i] == "pd":
            if word in class_word_frequency["pd"]:
                count = class_word_frequency["pd"][word] + 1
                class_word_frequency["pd"][word] = count
            else:
                class_word_frequency["pd"][word] = 1
        elif filetype[i] == "pt":
            if word in class_word_frequency["pt"]:
                count = class_word_frequency["pt"][word] + 1
                class_word_frequency["pt"][word] = count
            else:
                class_word_frequency["pt"][word] = 1
        word_count=0
        if word in word_frequency:
            word_count=word_frequency[word]+1
            word_frequency[word]=word_count
        else:
            word_frequency[word]=1

common_word_frequency = {key:val for key, val in word_frequency.items() if val != 1}
# print(word_frequency)

class_word_prob={"nd":{},"nt":{},"pd":{},"pt":{}}
alpha = 0.6
# print(len(vocab_set_final))

for key, val in class_word_frequency.items():
    word_prob=class_word_prob[key]
    for word,freq in common_word_frequency.items():
        if(word in val)    :
            value=val[word]
            probability= (value+alpha)/(class_counts[key]+ alpha*len(word_frequency))
            word_prob[word]=probability
        else:
            probability= (alpha)/(class_counts[key]+ alpha*len(word_frequency))
            word_prob[word]=probability
    class_word_prob[key]=word_prob

f = open("nbmodel.txt", "w")
f.write(json.dumps(class_word_prob))
f.close()


