import numpy as np
import sys
def parseInput(file_name):
    # Reading input data and other data files from path specified in command line
    input_names = np.genfromtxt(file_name,delimiter=',',usecols=0,dtype=str)
    data_input = np.genfromtxt(file_name,delimiter=',',usecols=0,dtype=str)
    female_list=np.genfromtxt('dist.female.first.txt',usecols=0,dtype=str)
    male_list = np.genfromtxt('dist.male.first.txt',usecols=0,dtype=str)
    surnames = np.genfromtxt('Names_2010Census.csv', delimiter=',',usecols=0,dtype=str)
    return data_input,input_names,female_list,male_list,surnames


if __name__ == "__main__":

    # Initializing input data
    file_name=str(sys.argv[-1])
    data_input,input_names,female_list,male_list,surnames=parseInput(file_name)
    female_list=female_list.tolist()
    male_list=male_list.tolist()
    prefix=['MAJOR','COLONEL','REVEREND','DOCTOR','PROFESSOR', 'MARSHALL']
    input_names= [[j.replace(',', '') for j in i.split(' AND ')] for i in input_names]
    print(input_names[:10])


    # Calculating new full names
    new_names = []
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

        elif(len(first_name)==len(second_name)):
            current_prefix=''
            if(first_name[0] in prefix):
                current_prefix=first_name[0]
                first_name.remove(current_prefix)
            if(len(first_name)==3):
                new_names.append(first_name)
            elif(second_name[-1] in surnames and first_name[-1] in (female_list+male_list)):
                first_name.append(second_name[-1])
                if(len(current_prefix)!=0):
                    first_name=[current_prefix]+first_name

                new_names.append(first_name)
            else:
                new_names.append(first_name)

        elif(len(first_name)<len(second_name)):
            if(first_name[-1] in surnames and first_name[-1] not in female_list and first_name[-1] not in male_list):
                new_names.append(first_name)
            elif(second_name[-1] in surnames and first_name[-1] not in surnames):
                    if(len(second_name)>3 and second_name[-2] in surnames):
                        first_name.append(second_name[-2])
                    first_name.append(second_name[-1])
                    new_names.append(first_name)
            else:
                    if (len(second_name) >= 3):
                        if (second_name[-2] in surnames and second_name[-2] not in male_list and second_name[
                            -2] not in female_list and first_name[-1] in (female_list+male_list)):
                            first_name.append(second_name[-2])
                            first_name.append(second_name[-1])
                        elif (second_name[-1] in surnames and first_name[-1] in (female_list+male_list)):
                            if (second_name[-2] in surnames and len(second_name) >= 4 and second_name[0] not in prefix):
                                first_name.append(second_name[-2])
                            first_name.append(second_name[-1])
                    new_names.append(first_name)

        else:
            new_names.append(first_name)
        i=i+1


    #Converting predicted names to strings
    name_strs = []
    for i in range(len(new_names)):
        str1 = " "
        str1 = str1.join(new_names[i])
        name_strs.append(str1)


    # Writing input names and predicted names to output file
    import csv
    with open('full-name-output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(zip(data_input,name_strs))

    f.close()
