# Algorithm 6 PerceptronTest(w0, w1, . . . , wD, b, xˆ)
#     a ← ∑D w xˆ + b           // compute activation for the test example
# return sign(a)


import json
import os
import glob
import sys
import string


modelfile = open(sys.argv[1] ,'r')
# modelfile=open("testing",'r')
fileData = json.loads(modelfile.read())
modelfile.close()
outfile = open("percepoutput.txt", "w")

all_files = glob.glob(os.path.join(sys.argv[2], '*/*/*/*.txt'))
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



soln = {}
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
    # res = find_class(weights_true_deceptive ,bias_True_Deceptive,
    #                                   fileData["wts_pn"], fileData["bias_pn"],
    #                                   content, paths[i])

    words = filedata.split()
    class_results = {}
    for word in words:
        if word in class_results.keys():
            count=class_results[word]+1
            class_results[word]=count
        else:
            count=1
            class_results[word]=count
        # class_results[word] = class_results.get(word, 0) + 1
    true_deceptive = 0
    positive_negative = 0
    for feature in class_results:
        if feature in fileData["wts_td"]:
            true_deceptive = true_deceptive + fileData["wts_td"][feature] * class_results[feature]
        else:
            print("not found in fileData[weights_True_Deceptive]")
        if feature in fileData["wts_pn"]:
            positive_negative = positive_negative + fileData["wts_pn"][feature] * class_results[feature]
        else:
            print("not found in fileData[weights_Positive_Negative]")
    true_deceptive = true_deceptive + fileData["bias_td"]
    positive_negative = positive_negative + fileData["bias_pn"]

    if positive_negative >= 0 and true_deceptive >= 0:
        class_res = "pt"
    elif positive_negative >= 0 and true_deceptive < 0:
        class_res = "pd"
    elif positive_negative < 0 and true_deceptive >= 0:
        class_res = "nt"
    else:
        class_res = "nd"
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
    if current_file_type in soln:
        resultDict = soln[current_file_type]
    else:
        soln[current_file_type] = {}
        resultDict = soln[current_file_type]
    if final_type in resultDict:
        newSum = resultDict[final_type] + 1
        resultDict[final_type] = newSum
    else:
        resultDict[final_type] = 0
        newSum = resultDict[final_type]
        resultDict[final_type] = newSum + 1
    soln[file_type[i]] = resultDict
outfile.close()
