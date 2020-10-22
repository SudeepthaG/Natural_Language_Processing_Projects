import json
import sys

# f = open(sys.argv[1], encoding='UTF-8')
# f = open('hmm-training-data/it_isdt_dev_raw.txt', encoding='UTF-8')
f = open('hmm-training-data/ja_gsd_dev_raw.txt', encoding='UTF-8')
model = open('hmmmodel.txt', encoding='UTF-8')
inputdata = json.loads(model.read())
model.close()
outfile = open("hmmoutput.txt", mode='w', encoding='UTF-8')

# for each sentence do this
for line in f.readlines():
    # get the words..
    words = line.split()
    tags_dict = inputdata[1]
    words_tags_dict = inputdata[2]
    res = {}
    wordscount = len(words)+1
    tagged_sent = ""
    for i in range(0, wordscount):
        res[i] = {}
        if i == 0:
            word = words[i]
            if word in words_tags_dict.keys():
                for tag in words_tags_dict[word].keys():
                    res[i][tag] = {'prob':words_tags_dict[word][tag] + tags_dict['start'][tag], 'backptr':'start'}
                continue
            else:
                for tag in inputdata[0].keys():
                    if tag != 'start' and tag != 'end':
                        res[i][tag] = {'prob':tags_dict['start'][tag], 'backptr':'start' }
                continue

        elif i == len(words):
            maxValue = -sys.maxsize - 1
            result = ''
            for prev_tag,val in res[i - 1].items():
                prob = res[i - 1][prev_tag]['prob'] + tags_dict[prev_tag]['end']
                if maxValue < prob:
                    maxValue = prob
                    result = prev_tag
                else:
                    # print(prob+" checkpoint y"+maxValue)
                    pass
            res[i]['end'] = {'prob':maxValue, 'backptr' :result}
            continue
        else:
            # print("not found")
            pass
        word = words[i]
        if word in words_tags_dict.keys():
            for tag,valu in words_tags_dict[word].items():
                maxValue = -(sys.maxsize + 1)
                result = ''
                res[i][tag] = {}

                for prev_tag,val in res[i - 1].items():
                    prevProb=res[i - 1][prev_tag]['prob']
                    prob = prevProb + words_tags_dict[word][tag] + tags_dict[prev_tag][
                        tag]
                    if  maxValue < prob:
                        maxValue = prob
                        result = prev_tag
                    else:
                        # print(prob+" checkpoint y"+maxValue)
                        pass
                res[i][tag] = {'prob':maxValue, 'backptr' :result}
        else:
            for tag in inputdata[0].keys():
                if tag not in ['start','end']:
                    maxValue = -(sys.maxsize + 1)
                    res[i][tag] = {}
                    result = ''
                    for prev_tag,val in res[i - 1].items():
                        prevProb=res[i - 1][prev_tag]['prob']
                        prob = prevProb + tags_dict[prev_tag][tag]
                        if maxValue < prob:
                            maxValue = prob
                            result = prev_tag
                        else:
                            # print(prob+" checkpoint z"+maxValue)
                            pass
                    res[i][tag] = {'prob':maxValue, 'backptr' :result}

    # tag the results
    length=len(res)
    p = length - 1
    q = length - 2
    startTag = 'end'
    while p - 1 >= 0:
        tag = res[p][startTag]['backptr']
        r = length - 1
        if (p == r):
            tagged_sent = words[q] + "/" + tag
        elif (p !=r):
            tagged_sent = words[q] + "/" + tag + " " + tagged_sent
        startTag = tag
        p -= 1
        q -= 1
    outfile.write(tagged_sent+ '\n')

# write to the file
outfile.close()
f.close()