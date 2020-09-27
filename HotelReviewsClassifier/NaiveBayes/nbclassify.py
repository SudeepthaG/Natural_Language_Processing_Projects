import json
import os
import string
import glob
import sys
import math

modelfile = open('nbmodel.txt', 'r')
class_word_prob = json.loads(modelfile.read())
modelfile.close()

all_files = glob.glob(os.path.join(sys.argv[1], '*/*/*/*.txt'))
# all_files = glob.glob(os.path.join("./op_spam_training_data", '*/*/*/*.txt'))
paths = []
file_type = []
for f in all_files:
    class1, class2, fold, fname = f.split('/')[-4:]
    if "positive" in class1:
        if "truthful" in class2:
            file_type.append("pt")
            paths.append(f)
        else:
            file_type.append("pd")
            paths.append(f)
    elif "negative" in class1:
        if "truthful" in class2:
            file_type.append("nt")
            paths.append(f)
        else:
            file_type.append("nd")
            paths.append(f)

result = {}
outfile = open("nboutput.txt", "w")
for i in range(len(paths)):
    filedata = open(paths[i]).read()
    filedata = filedata.lower()
    punctuations = string.punctuation
    punctuations = punctuations.replace("\'", "")
    punctuation_list = list(punctuations)
    for j in range(0, len(filedata)):
        if filedata[j] in punctuation_list:
            filedata = filedata[:j] + ' ' + filedata[j + 1:]
    filedata = filedata.replace("\n", '')
    class_results = {}
    for key in class_word_prob.keys():
        value = class_word_prob[key]
        prob = 0
        for word in filedata.split():
            val_file_type = class_word_prob[key]
            if word in val_file_type:
                val = val_file_type[word]
            else:
                val_file_type[word] = "no val found"
                val = val_file_type[word]
            if val != "no val found":
                val = math.log(val)
                prob += val
            else:
                pass
        class_results[key] = prob * 0.25
    # print(class_results)
    max = -10000.00
    class_res = 0
    for key in class_results.keys():
        value = class_results[key]
        if value > max:
            max = value
            class_res = key
        else:
            count = 1
    #    print(filename + str(class_res))
    final_type = class_res
    if final_type == "pt":
        outfile.write("truthful positive " + paths[i] + "\n")
    elif final_type == "pd":
        outfile.write("deceptive positive " + paths[i] + "\n")
    elif final_type == "nt":
        outfile.write("truthful negative " + paths[i] + "\n")
    elif final_type == "nd":
        outfile.write("deceptive negative " + paths[i] + "\n")
    else:
        pass
    current_file_type = file_type[i]
    if current_file_type in result:
        resultDict = result[current_file_type]
    else:
        result[current_file_type] = {}
        resultDict = result[current_file_type]
    if final_type in resultDict:
        newSum = resultDict[final_type] + 1
        resultDict[final_type] = newSum
    else:
        resultDict[final_type] = 0
        newSum = resultDict[final_type]
        resultDict[final_type] = newSum + 1
    result[file_type[i]] = resultDict
outfile.close()