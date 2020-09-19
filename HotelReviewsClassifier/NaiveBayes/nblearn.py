import os
import sys
import pandas

filelist = []
path="./op_spam_training_data"
for root, dirs, files in os.walk(path):
    for file in files:
        # append the file name to the list
        filelist.append(os.path.join(root, file))
        # print(file)

deceptive_negative=[]
true_negative=[]
true_positive=[]
deceptive_positive=[]
# print all the file names
for name in filelist:
    # print(name)
    if("negative_polarity" in name):
        if("deceptive" in name):
            deceptive_negative.append(name)
        else:
            true_negative.append(name)
    else:
        if("deceptive" in name):
            deceptive_positive.append(name)
        else:
            true_positive.append(name)

# print(deceptive_negative)
# print("\n\n\n\n")
# print(deceptive_positive)
# print("\n\n\n\n")
# print(true_positive)
# print("\n\n\n\n")
# print(true_negative)
