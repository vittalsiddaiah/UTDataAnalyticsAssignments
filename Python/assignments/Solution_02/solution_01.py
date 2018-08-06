import sys
import re
import os

sys.path.insert(1, r'../../py_lib/')
from py_lib.timer import timer
from py_lib.us_state_abbrev import us_state_abbrev
from py_lib.csv_parser import csv_parser
from py_lib.h_line import h_line

########################################################################################################################
def PyBoss(input_file, output_file):
    employeeData = csv_parser(input_file, is_first_row_header=True)
    newEmployeeCSV = ''
    newEmployeeData = []
    newEmployeeHeader = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']
    newEmployeeCSV += ','.join(newEmployeeHeader) + "\n"
    for offset in range(len(employeeData)):
        employee = []
        employee.append(employeeData.cell(offset, column_name='Emp ID'))
        name = re.split('\s+', employeeData.cell(offset, column_name='Name').strip())
        employee.append(name[0])                #First Name
        employee.append(' '.join(name[1:]))     #Last Name, Concatenate if more than one lastName
        dob = re.split('\s*-\s*', employeeData.cell(offset, column_name='DOB'))
        employee.append("%02d/%02d/%02d" %( int(dob[1]), int(dob[2]), int(dob[0])))
        ssn = re.split('\s*-\s*', employeeData.cell(offset, column_name='SSN'))
        employee.append("***-**-%d" % int(ssn[2]))
        employee.append(us_state_abbrev(employeeData.cell(offset, column_name='State')))
        newEmployeeData.append(employee)
        newEmployeeCSV += ','.join(employee) + "\n"

    with open(output_file, 'w') as fd_results:
        fd_results.write(newEmployeeCSV)

    newEmployeeCSV += h_line()
    print("\n" + newEmployeeCSV + "\n" + "Input File  : " + os.path.abspath(input_file))
    print("Output File : " + os.path.abspath(output_file) + "\n" + h_line(2))
    return
########################################################################################################################

########################################################################################################################
def PyParagraph(input_file, output_file):
    letterSum = 0
    words = []
    lines = []
    results = []
    results.append(h_line(num=2))
    with open(input_file) as fd_read:
        for count, line in enumerate(fd_read):
            words.extend(re.split('\s+', line))
            lines.extend(re.split('\.+', line))
            for word in words:
                letterSum += len(word)
    results.append(h_line())
    results.append("Paragraph Analysis")
    results.append(h_line())
    numWords = 0
    numLines = 0

    for word in words:
        if len(word.strip()) == 0: continue
        if (len(word.strip()) == 1) and (not word.strip().isalpha()): continue
        numWords += 1

    for line in lines:
        if len(line.strip()) == 0:  continue    #ignore empty lines
        if (len(line.strip()) == 1) and (not line.isalnum()): continue  #ignore line with single character of non alpha numeric
        numLines += 1   # To Ignore empty lines

    results.append("Approximate Word Count     : %3d" % numWords)
    results.append("Approximate Sentence Count : %3d" % numLines)
    results.append("Average Letter Count       : %6.2f" % (letterSum/numWords))
    results.append("Average Sentence Length    : %6.2f" % (numWords/numLines))
    results.append(h_line())

    finalReport = '\n'.join(results)

    with open(output_file, 'w') as fd_write:
        fd_write.write(finalReport)

    print("\n" + finalReport + "\n" + "Input File  : " + os.path.abspath(input_file))
    print("Output File : " + os.path.abspath(output_file) + "\n" + h_line(2))
    return
########################################################################################################################

########################################################################################################################
if __name__ == '__main__':
    timing = timer('Processed In : ')
    PyBoss("../../data/src/employee_data.csv", "../../data/dst/employee_data_modified.csv")
    print(timing.delta_str())
    timing.reset()
    PyParagraph("../../data/src/paragraph_1.txt", "../../data/dst/paragraph_stats_1.txt")
    print(timing.delta_str())
    timing.reset()
    PyParagraph("../../data/src/paragraph_2.txt", "../../data/dst/paragraph_stats_2.txt")
    print(timing.delta_str())
    timing.reset()
    PyParagraph("../../data/src/test_paragraph.txt", "../../data/dst/test_paragraph_stats.txt")
    print(timing.delta_str())
########################################################################################################################