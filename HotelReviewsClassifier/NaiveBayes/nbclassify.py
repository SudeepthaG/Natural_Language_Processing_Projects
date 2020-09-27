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
    else:
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

    words = filedata.split()
    class_results = {}
    for key, value in class_word_prob.items():
        probablity = 0
        for word in words:
            val = class_word_prob.get(key).get(word, None)
            if val != None:
                val = math.log(val)
                probablity += val
            else:
                pass
        class_results[key] = probablity * 1 / 4
    # print(class_results)
    max = float('-inf')
    class_res = 0
    for key, value in class_results.items():
        if value > max:
            max = value
            class_res = key
        else:
            count = 1
    #    print(filename + str(class_res))
    final_type = class_res
    if final_type == "pt":
        outfile.write("truthful positive " + paths[i])
    if final_type == "pd":
        outfile.write("deceptive positive " + paths[i])
    if final_type == "nt":
        outfile.write("truthful negative " + paths[i])
    if final_type == "nd":
        outfile.write("deceptive negative " + paths[i])
    else:
        pass
    outfile.write("\n")
    current_file_type = file_type[i]
    if current_file_type in result:
        resMap = result[current_file_type]
    else:
        resMap = result.get(current_file_type, {})
    if final_type in resMap:
        currTotal = resMap[final_type] + 1
        resMap[final_type] = currTotal
    else:
        currTotal = resMap.get(final_type, 0)
        resMap[final_type] = currTotal + 1
    result[file_type[i]] = resMap
outfile.close()