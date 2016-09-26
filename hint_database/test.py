# Script to test hint class
# Run this script with the folder that contains all the hint class files,
# it will check if a hint class is valid for the attempts
#
# NOTICE: Name of the hint class has to be the same as the hint class file
#
# Name: Zeng Fan
# Date: Sep 21, 2016
from cluster_functions import make_params, find_matches, get_numerical_answer
import pickle
import sys
from pydoc import locate
import os
from os import listdir
from os.path import isfile, join

def check_final_answer(params,tol = 1+1e-3):
    att_tree = params['att_tree']
    ans_tree = params['ans_tree']
    att_result = get_numerical_answer(att_tree)
    ans_result = get_numerical_answer(ans_tree)
    if ans_result != 0:
        ratio = att_result/ans_result
    else:
        if att_result == 0:
            ratio = 1
        else:
            ratio = 0

    if ratio < tol and ratio > (1/tol):
        return True
    else:
        return False


if __name__ == "__main__":
    import sys
    print 'argv=',sys.argv
    week,problem,part,test_length,file_path=sys.argv[1:]

#    week = raw_input("Week ID:")
#    problem = raw_input("Problem ID:")
#    part = raw_input("Part_ID:")
#    test_length = raw_input("How many samples you want to see:")
#    file_path = raw_input("Type in name of your class:\n")


    '''Read data file'''
    data_file = "2015data/pkl/Week"+week+"_data.pkl"
    print "Reading ",data_file
    weekdata = pickle.load(open(data_file,'rb'))


    '''Read hint class'''
    file_path = "hint_class/Week"+week+"/"+file_path+".py"
    package_name,hint_class_name = os.path.split(file_path)
    hint_class = os.path.splitext(hint_class_name)[0]
    package_name = package_name.replace('/', '.')#"".join(package_name.split('/')[-1])
    class_address = package_name + "." + hint_class + "." + hint_class
    print class_address
    ClassName = locate(class_address)
    #print ClassName,type(ClassName)
    try:
        hint_instance = ClassName()
    except TypeError:
        sys.exit("ERROR: name of the HINT CLASS has to be the same as the name of the FILE !!")

    key = (problem,part)
    problem_data = weekdata[key]
    if test_length > 50:
        test_length = 50
    testdata = problem_data[0:test_length]
    testdata = tuple(testdata)
    i = 1

    for test in testdata:
        print "\nUserID:",i
        i+=1
        attempt = test['attempt']
        answer = test['answer']
        print "attempt:",attempt
        print "answer:",answer

        if not attempt:
            print "Attempt is empty"
        else:
            params = make_params(answer,attempt)
            match = find_matches(params)
            ans_tree = params['ans_tree'][0]
            if match==ans_tree or check_final_answer(params):
                print "Correct answer!"
            else:
                hint, hint_ans = hint_instance.check_attempt(params)
                if not hint:
                    print "Hint does not hit"
                else:
                    print hint, hint_ans


