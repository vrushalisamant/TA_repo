# Script to test hint class
# Run this script with the folder that contains all the hint class files,
# it will check if a hint class is valid for the attempts
#
# NOTICE: Name of the hint class has to be the same as the hint class file
#
# Name: Zeng Fan / Zhen Zhai
# Date: Sep 27, 2016
from hint_class_helpers.make_params import make_params
from hint_class_helpers.find_matches import find_matches
from hint_class_helpers.get_numerical_answer import get_numerical_answer
import pickle
import sys
from pydoc import locate
import os
import traceback
from os import listdir
from os.path import isfile, join, expanduser, splitext

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


def get_all_classes(path):
    'Read first universal hint functions'''
    uni_folder_name = 'hint_class/first_Universal'
    first_universal_hint_files = []
    for f in listdir(expanduser(uni_folder_name)):
        if isfile(join(expanduser(uni_folder_name), f)) and \
                f.endswith('.py') and f != '__init__.py':
            first_universal_hint_files.append(splitext(f)[0])

    'Read hint class'''
    folder_name = path
    hint_classes = []
    for f in listdir(expanduser(folder_name)):
        if isfile(join(expanduser(folder_name), f)) and \
                f.endswith('.py') and f != '__init__.py' and f != 'template.py':
            hint_classes.append(splitext(f)[0])

    'Read last universal hint functions'''
    l_uni_folder_name = 'hint_class/last_Universal'
    last_universal_hint_files = []
    for f in listdir(expanduser(l_uni_folder_name)):
        if isfile(join(expanduser(l_uni_folder_name), f)) and \
                f.endswith('.py') and f != '__init__.py':
            last_universal_hint_files.append(splitext(f)[0])


    return first_universal_hint_files, hint_classes, last_universal_hint_files


def single_hint_test(path, new_class_name, testdata):
    first_u_hints, hint_classes, last_u_hints = get_all_classes(path)
    hint_classes.remove(new_class_name)
    
    i = 1

    for test in testdata:
        attempt = test['attempt']
        answer = test['answer']
        if not attempt:
            print "Attempt is empty"
            continue

        params = make_params(answer,attempt)

        if params == {}:
            continue

        match = find_matches(params)
        ans_tree = params['ans_tree'][0]
        if match==ans_tree or check_final_answer(params):
            print "Correct answer!"
            continue

        hint = ""
        # try first universal hints
        package_name = 'hint_class.first_Universal'
        if len(params['att_tree']) > 1:
            for f_name in first_u_hints:
                f_address = package_name + "." + f_name
                try:
                    uni_f = locate(f_address)
                except:
                    #traceback.print_exc()
                    sys.exit("ERROR: syntax error in universal hint function!!")

                try:
                    hint = uni_f.check_attempt(params)
                except:
                    #traceback.print_exc()
                    sys.exit("ERROR: syntax error in universal hint function!!")

                if hint:
                    break
            if hint:
                continue

        # try conditional hints
        folder_name = path
        package_name = folder_name.replace('/', '.')
        for class_name in hint_classes:
            class_address = package_name + "." + class_name + "." + class_name
            try:
                ClassName = locate(class_address)
            except:
                traceback.print_exc()
                sys.exit("ERROR: syntax error in HINT CLASS!!")

            try:
                hint_instance = ClassName()
            except TypeError:
                sys.exit("ERROR: name of the HINT CLASS has to be the same as the name of the FILE !!")

            try:
                hint, hint_ans = hint_instance.check_attempt(params)
            except:
                traceback.print_exc()
                sys.exit("ERROR: syntax error in HINT CLASS!!")

            if hint:
                break
        if hint:
            continue


        print "\nUserID:",i
        i+=1
        print "attempt:",attempt
        print "answer:",answer

        # Try new hint
        class_address = package_name + "." + new_class_name + "." + new_class_name
        try:
            ClassName = locate(class_address)
        except:
            traceback.print_exc()
            sys.exit("ERROR: syntax error in HINT CLASS!!")

        try:
            hint_instance = ClassName()
        except TypeError:
            sys.exit("ERROR: name of the HINT CLASS has to be the same as the name of the FILE !!")

        try:
            hint, hint_ans = hint_instance.check_attempt(params)
        except:
            traceback.print_exc()
            sys.exit("ERROR: syntax error in HINT CLASS!!")

        if hint:
            print "hint:", hint
            print "solution:", hint_ans
            continue

        # Try last universal hint
        package_name = 'hint_class.last_Universal'
        last_universal_hint = ""
        for f_name in last_u_hints:
            f_address = package_name + "." + f_name
            try:
                uni_f = locate(f_address)
            except:
                traceback.print_exc()
                sys.exit("ERROR: syntax error in universal hint function!!")

            try:
                hint = uni_f.check_attempt(params)
            except:
                traceback.print_exc()
                sys.exit("ERROR: syntax error in universal hint function!!")

            if hint:
                print "hint:", hint
                break

        if not hint:
            print "Hint does not hit!"




def all_hints_test(path,testdata):
    first_u_hints, hint_classes, last_u_hints = get_all_classes(path)

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
            continue

        params = make_params(answer,attempt)


        if params == {}:
            continue
            
        match = find_matches(params)
        ans_tree = params['ans_tree'][0]
        if match==ans_tree or check_final_answer(params):
            print "Correct answer!"
            continue

        # try first universal hints
        package_name = 'hint_class.first_Universal'
        universal_hint = ""
        if len(params['att_tree']) > 1:
            for f_name in first_u_hints:
                f_address = package_name + "." + f_name
                try:
                    uni_f = locate(f_address)
                except:
                    traceback.print_exc()
                    sys.exit("ERROR: syntax error in universal hint function!!")

                try:
                    universal_hint = uni_f.check_attempt(params)
                except:
                    traceback.print_exc()
                    sys.exit("ERROR: syntax error in universal hint function!!")

                if universal_hint:
                    print universal_hint
                    break
            if universal_hint:
                continue


        # try conditional hints
        folder_name = path
        package_name = folder_name.replace('/', '.')#"".join(package_name.split('/')[-1])

        hint = ""
        for class_name in hint_classes:
            class_address = package_name + "." + class_name + "." + class_name
            try:
                ClassName = locate(class_address)
            except:
                traceback.print_exc()
                sys.exit("ERROR: syntax error in HINT CLASS!!")

            try:
                hint_instance = ClassName()
            except TypeError:
                sys.exit("ERROR: name of the HINT CLASS has to be the same as the name of the FILE !!")

            try:
                hint, hint_ans = hint_instance.check_attempt(params)
            except:
                traceback.print_exc()
                sys.exit("ERROR: syntax error in HINT CLASS!!")

            if hint:
                print hint, hint_ans
                break


        # Try last universal hint
        package_name = 'hint_class.last_Universal'
        last_universal_hint = ""
        for f_name in last_u_hints:
            f_address = package_name + "." + f_name
            try:
                uni_f = locate(f_address)
            except:
                traceback.print_exc()
                sys.exit("ERROR: syntax error in universal hint function!!")

            try:
                last_universal_hint = uni_f.check_attempt(params)
            except:
                traceback.print_exc()
                sys.exit("ERROR: syntax error in universal hint function!!")

            if last_universal_hint:
                print "hint:", last_universal_hint
                break

        if not hint:
            print "Hint does not hit!"




if __name__ == "__main__":
    # week = raw_input("Week ID:")
    # problem = raw_input("Problem ID:")
    # part = raw_input("Part_ID:")
    # test_length = raw_input("How many samples you want to see:")
    # file_path = raw_input("Type in relative path of class file:\n")

    #print 'argv=',sys.argv
    if sys.argv[1] == "--help":
        print("Please type in parameters as follow:")
        print("<Week ID> <Problem ID> <Part ID> <Sample Numbers> <Hint Class Name(Optional)>")
        print("If you don't want to suppress other hints, please type in the class name.")
        sys.exit()

    try:
        week,problem,part,test_length = sys.argv[1:5]
        class_name = ""
        if len(sys.argv) > 5:
            class_name = sys.argv[5]
            print('Week_ID='+week+', Problem_ID='+problem+', Part_ID='+part+', Sample Numbers='+test_length+', Hint Class='+class_name+
                '. Suppress other hints.')
        else:
            print('Week_ID='+week+', Problem_ID='+problem+', Part_ID='+part+', Sample Numbers='+test_length+'. Don\'t suppress other hints.')
    except:
        sys.exit("Error, see 'python test.py --help' for input requirement")

    '''Read data file'''
    data_file = "2015data/pkl/Week"+week+"_data.pkl"
    print "Reading ",data_file
    weekdata = pickle.load(open(data_file,'rb'))

    key = (problem,part)
    problem_data = weekdata[key]
    testdata = problem_data[0:int(test_length)]
    testdata = tuple(testdata)

    path = 'hint_class/Week{0}'.format(week)
    if class_name:
        single_hint_test(path, class_name, testdata)
    else:
        all_hints_test(path,testdata)



