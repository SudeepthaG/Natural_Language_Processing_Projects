import numpy as np

def parseInput():
    # Reading and counting input data
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
    # print(female_list[:10])

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
    # female_list = [[j.replace(',', '') for j in i.split(' ')] for i in female_list]
    # male_list = [[j.replace(',', '') for j in i.split(' ')] for i in male_list]
    input_names= [[j.replace(',', '') for j in i.split(' AND ')] for i in input_names]
    print(input_names[:10])

    # Analying input
    same = 0
    smaller = 0
    single=0
    bigger=0
    for name in input_names:
        first_name=name[0].split(' ')
        second_name=name[1].split(' ')
        # print("First name:")
        # print(first_name)
        # print("Second name:")
        # print(second_name)
        if(len(first_name)==1):
            single=single+1
        elif(len(first_name)==len(second_name)):
            # print("same")
            same=same+1
        elif(len(first_name)<len(second_name)):
            # print('smaller')
            smaller=smaller+1
        else:
            bigger=bigger+1
            # print(name)
    print(same)
    print(smaller)
    print(single)
    print(bigger)
    print(same+smaller+single)
    print(bigger)


    # Calculating new full names
    new_names = []
    full_names = [[j.replace(',', '') for j in i.split(' ')] for i in full_names]
    i=0
    for name in input_names:
        first_name=name[0].split(' ')
        second_name=name[1].split(' ')
        # print("First name:")
        # print(first_name)
        # print("Second name:")
        # print(second_name)

        if(len(first_name)==1):
            # if(second_name[-2] in surnames):
            #     first_name.append(second_name.append[-2])
            # print("enter")
            if(len(second_name)>=3):
                if(len(second_name)==3):
                    # print("enter2")
                    # print("First name:")
                    # print(first_name)
                    # print("Second name:")
                    # print(second_name)
                    # print(first_name[0] in female_list and second_name[-2] not in female_list and second_name[-2] not in male_list and second_name[-2] in surnames)
                    if(first_name[0] in female_list and second_name[-2] not in female_list and second_name[-2] not in male_list and second_name[-2] in surnames):
                        first_name.append(second_name[-2])

                    # print(first_name in male_list and second_name[-2] not in female_list and second_name[-2] in male_list and second_name[-2] in surnames)
                    elif(first_name[0] in male_list and second_name[-2] not in female_list and second_name[-2] not in male_list and second_name[-2] in surnames):
                        first_name.append(second_name[-2])
                else:
                        first_name.append(second_name[-2])
            first_name.append(second_name[-1])
            new_names.append(first_name)
            # if((new_names[i]==full_names[i])==False):
            #     print("1 false")
            #     print(new_names[i]+full_names[i])
            # else:
            #     print('true')
            #     print(new_names[i]+full_names[i])


        elif(len(first_name)==len(second_name)):
            if(len(first_name)==3):
                new_names.append(first_name)
                # if((new_names[i]==full_names[i])==False):
                #     print("2 ")
                #     print(new_names[i]+full_names[i])
            elif(second_name[-1] in surnames):
                first_name.append(second_name[-1])
                new_names.append(first_name)
                # if((new_names[i]==full_names[i])==False):
                #     print("3  ")
                #     print(new_names[i]+full_names[i])
                # else:
                #     print("3 true")
                #     print(new_names[i]+full_names[i])
            else:
                new_names.append(first_name)
                # if ((new_names[i] == full_names[i]) == False):
                #     print("4 ")
                #     print(new_names[i] + full_names[i])

        elif(len(first_name)<len(second_name)):
            if(first_name[-1] in surnames and first_name[-1] not in female_list and first_name[-1] not in male_list):
                new_names.append(first_name)
                print('sfdfd')
                if ((new_names[i] == full_names[i]) == False):
                    print("5a")
                    print(new_names[i] + full_names[i])
            elif(second_name[-1] in surnames and first_name[-1] not in surnames):
                    first_name.append(second_name[-1])
                    new_names.append(first_name)
                    if ((new_names[i] == full_names[i]) == False):
                        print("5b")
                        print(second_name)
                        print(new_names[i] + full_names[i])
                # else:
                #     new_names.append(first_name)
                #     print('dfxgfbd')
                #     if ((new_names[i] == full_names[i]) == False):
                #         print("5b")
                #         print(new_names[i] + full_names[i])
            else:
                first_name.append(second_name[-1])
                new_names.append(first_name)
                if ((new_names[i] == full_names[i]) == False):
                    # print(second_name)
                    print("6 ")
                    print(second_name)
                    print(new_names[i] + full_names[i])

        else:
            new_names.append(first_name)
            if((new_names[i]==full_names[i])==False):
                print("7 ")
                print(new_names[i]+full_names[i])
        i=i+1
    # print(new_names[:10])


    #Checking accuracy
    accuracy=0
    two_names=0
    three_names=0
    four_names=0
    # full_names = [[j.replace(',', '') for j in i.split(' ')] for i in full_names]
    # print(full_names[:10])
    for i in range(1000):
        if(new_names[i]==full_names[i]):
            accuracy=accuracy+1
        # else:
            # print(new_names[i]+full_names[i])
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

    print(accuracy)
    print("two names")
    print(two_names)
    print("three names")
    print(three_names)
    print("four names")
    print(four_names)
