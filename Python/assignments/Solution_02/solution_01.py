import sys
import re
import os

sys.path.insert(1, r'../../py_lib/')
from py_lib.timer import timer
from py_lib.us_state_abbrev import us_state_abbrev
from py_lib.csv_parser import csv_parser

########################################################################################################################
def PyBoss(employeeDataFile, modEmployeeDataFile):
    employeeData = csv_parser(employeeDataFile, is_first_row_header=True)
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
        employee.append("%02d/%02d/%02d" %( int(dob[1]), int(dob[2]), int(dob[0])))   #126,Gary Knight,1994-03-08,782-25-1242,Arkansas => MM/DD/YYYY
        ssn = re.split('\s*-\s*', employeeData.cell(offset, column_name='SSN'))
        employee.append("***-**-%d" % int(ssn[2]))
        employee.append(us_state_abbrev(employeeData.cell(offset, column_name='State')))
        newEmployeeData.append(employee)
        newEmployeeCSV += ','.join(employee) + "\n"

    with open(modEmployeeDataFile, 'w') as fd_results:
        fd_results.write(newEmployeeCSV)
    print(newEmployeeCSV)
    print("Log path : ", os.path.abspath(modEmployeeDataFile) + "\n")
########################################################################################################################


def PyParagraph():


########################################################################################################################
if __name__ == '__main__':
    timing = timer('Processed In : ')
    PyBoss("../../data/src/employee_data.csv", "../../data/dst/employee_data_modified.csv")
    print(timing.delta_str())