import numpy as np

def parseInput():
    # Reading input data and type
    input_names = np.genfromtxt('dev-key.csv',delimiter=',',usecols=0,dtype=str)
    print("Input names")
    print(type(input_names))
    print(input_names.shape[0])
    print(input_names[:10])

    print("Full names")
    full_names = np.genfromtxt('dev-key.csv',delimiter=',',usecols=1,dtype=str)
    print(full_names[:10])


    female_list=np.genfromtxt('dist.female.first.txt',usecols=0,dtype=str)
    print("Female first names list")
    print(female_list.shape[0])

    male_list = np.genfromtxt('dist.male.first.txt',usecols=0,dtype=str)
    print("Male first names list")
    print(male_list.shape[0])

    surnames = np.genfromtxt('Names_2010Census.csv', delimiter=',',usecols=0,dtype=str)
    print("Surnames list")
    print(type(surnames))
    print(surnames.shape[0])
    return input_names,full_names,female_list,male_list,surnames



if __name__ == "__main__":
    input_names,full_names,female_list,male_list,surnames=parseInput()
    female_list=female_list.tolist()
    male_list=male_list.tolist()
    prefix=['MAJOR','COLONEL','REVEREND','DOCTOR','PROFESSOR', 'MARSHALL']
    input_names= [[j.replace(',', '') for j in i.split(' AND ')] for i in input_names]
    print(input_names[:10])


    # Analying input based on length of names
    same = 0
    smaller = 0
    single=0
    bigger=0
    for name in input_names:
        first_name=name[0].split(' ')
        second_name=name[1].split(' ')
        if(len(first_name)==1):
            single=single+1
        elif(len(first_name)==len(second_name)):
            same=same+1
        elif(len(first_name)<len(second_name)):
            smaller=smaller+1
        else:
            bigger=bigger+1
    print(same)
    print(smaller)
    print(single)
    print(bigger)


    # Calculating new full names
    new_names = []
    full_names = [[j.replace(',', '') for j in i.split(' ')] for i in full_names]
    i=0
    for name in input_names:
        first_name=name[0].split(' ')
        second_name=name[1].split(' ')

        if(len(first_name)==1):
            if(len(second_name)>=3):
                if(len(second_name)==3):
                    if(first_name[0] in female_list and second_name[-2] not in female_list and second_name[-2] not in male_list and second_name[-2] in surnames):
                        first_name.append(second_name[-2])
                    elif(first_name[0] in male_list and second_name[-2] not in female_list and second_name[-2] not in male_list and second_name[-2] in surnames):
                        first_name.append(second_name[-2])
                else:
                        first_name.append(second_name[-2])
            first_name.append(second_name[-1])
            new_names.append(first_name)
            # if((new_names[i]==full_names[i])==False):
            #     print("1  false")
            #     print(new_names[i]+full_names[i])

        elif(len(first_name)==len(second_name)):
            current_prefix=''
            if(first_name[0] in prefix):
                current_prefix=first_name[0]
                first_name.remove(current_prefix)
            if(len(first_name)==3):
                new_names.append(first_name)
                # if((new_names[i]==full_names[i])==False):
                #     print("2  ")
                #     print(new_names[i]+full_names[i])
            elif(second_name[-1] in surnames and first_name[-1] in (female_list+male_list)):
                first_name.append(second_name[-1])
                if(len(current_prefix)!=0):
                    first_name=[current_prefix]+first_name
                new_names.append(first_name)
                # if((new_names[i]==full_names[i])==False):
                #     print("3  ")
                #     print(new_names[i]+full_names[i])
            else:
                new_names.append(first_name)
                # if ((new_names[i] == full_names[i]) == False):
                #     print("4  ")
                #     print(new_names[i] + full_names[i])

        elif(len(first_name)<len(second_name)):
            if(first_name[-1] in surnames and first_name[-1] not in female_list and first_name[-1] not in male_list):
                new_names.append(first_name)
                # if ((new_names[i] == full_names[i]) == False):
                #     print("5a")
                #     print(new_names[i] + full_names[i])
            elif(second_name[-1] in surnames and first_name[-1] not in surnames):
                    if(len(second_name)>3 and second_name[-2] in surnames):
                        first_name.append(second_name[-2])
                    first_name.append(second_name[-1])
                    new_names.append(first_name)
                    # if ((new_names[i] == full_names[i]) == False):
                    #     print("5b")
                    #     print(new_names[i] + full_names[i])
            else:
                    if (len(second_name) >= 3):
                        if (second_name[-2] in surnames and second_name[-2] not in male_list and second_name[
                            -2] not in female_list and first_name[-1] in (female_list+male_list)):
                            first_name.append(second_name[-2])
                            first_name.append(second_name[-1])
                        elif (second_name[-1] in surnames and first_name[-1] in (female_list+male_list)):
                            if (second_name[-2] in surnames and len(second_name)>=4 and second_name[0] not in prefix):
                                first_name.append(second_name[-2])
                            first_name.append(second_name[-1])
                    new_names.append(first_name)
                    # if ((new_names[i] == full_names[i]) == False):
                    #     print("6  ")
                    #     print(new_names[i] + full_names[i])

        else:
            new_names.append(first_name)
            # if((new_names[i]==full_names[i])==False):
            #     print("7  ")
            #     print(new_names[i]+full_names[i])
        i=i+1



    #Checking accuracy and length of expected names
    accuracy=0
    two_names=0
    three_names=0
    four_names=0
    for i in range(1000):
        if(new_names[i]==full_names[i]):
            accuracy=accuracy+1
        if(len(full_names[i])==2):
            # print(full_names[i])
            two_names=two_names+1
        elif(len(full_names[i])==3):
            three_names=three_names+1
        elif(len(full_names[i])==4):
            # print(full_names[i])
            four_names=four_names+1
        else:
            print(full_names[i])

    print('accuracy')
    print(accuracy)
    print("two names")
    print(two_names)
    print("three names")
    print(three_names)
    print("four names")
    print(four_names)

