import json, sys, math

tags_dict = {}
no_of_tags = {}
words_tags_dict = {}
res = []

# f = open('hmm-training-data/it_isdt_train_tagged.txt', encoding='UTF-8')
f = open('hmm-training-data/ja_gsd_train_tagged.txt', encoding='UTF-8')
# f = open(sys.argv[1], encoding='UTF-8')
# print(sys.argv[1])
lines = f.readlines()

no_of_tags["start"]=len(lines)
no_of_tags["end"]=len(lines)
tagslist = ["start", "end"]
# lines = f.readlines()
# print(lines)

for line in lines:
    last_tag = ""
    prev_tag = "start"
    # print(line)
    for word in line.split():

        tag = word.split("/") [1]
        tagslist.append(tag)
        # increment the tag
        if tag in no_of_tags.keys():
            no_of_tags[tag] = no_of_tags[tag] + 1
        else:
            no_of_tags[tag]=1
        currWord = word.split("/") [0]
        # increment  word -> tag -> count
        if currWord in words_tags_dict.keys():
            no_of_tagsForGivenWord = words_tags_dict[currWord]
        else:
            words_tags_dict[currWord]={}
            no_of_tagsForGivenWord = words_tags_dict[currWord]

        if tag in no_of_tagsForGivenWord.keys():
            no_of_tagsForGivenWord[tag] = no_of_tagsForGivenWord[tag] + 1
        else:
            no_of_tagsForGivenWord[tag]=1
        words_tags_dict[currWord] = no_of_tagsForGivenWord 

        # increment tag->tag -> count
        if prev_tag in tags_dict.keys():
            curr_tag_count = tags_dict[prev_tag]
        else:
            tags_dict[prev_tag]= {}
            curr_tag_count = tags_dict[prev_tag]
        if tag in curr_tag_count.keys():
            curr_tag_count[tag] = curr_tag_count[tag] + 1
        else:
            curr_tag_count[tag] = 1
        tags_dict[prev_tag] = curr_tag_count
        last_tag = tag
        prev_tag = tag 
    # increment tag->tag -> count
    if last_tag in tags_dict.keys():
        curr_tag_count = tags_dict[last_tag]
    else:
        curr_tag_count = {}
    if 'end' in curr_tag_count.keys():
        curr_tag_count['end'] = curr_tag_count['end']+ 1
    else:
        curr_tag_count['end']=1
    tags_dict[last_tag] = curr_tag_count

for prev_tag in tags_dict.keys():
    nextTag= tags_dict[prev_tag]
    for tag in tagslist:
        if tag in nextTag:
            pass
        else:
            # print(tags_dict[prev_tag][tag])
            tags_dict[prev_tag][tag] = 0



res.append(no_of_tags)

for prev_tag in tags_dict:
    for curr_tag in tags_dict[prev_tag]:
        a=tags_dict[prev_tag][curr_tag]
        a+=1
        a= math.log(a)
        b=no_of_tags[prev_tag]
        b+=1
        b=math.log(b)
        tags_dict[prev_tag][curr_tag] =a-b


res.append(tags_dict)

for word in words_tags_dict:
    for tag in words_tags_dict[word]:
        a=words_tags_dict[word][tag]
        a=math.log(a)
        b=no_of_tags[tag]
        b=math.log(b)
        words_tags_dict[word][tag] = a-b

res.append(words_tags_dict)
# print(res)
modelfile = open('hmmmodel.txt', mode='w', encoding='UTF-8')
modelfile.write(json.dumps(res))
modelfile.close()


