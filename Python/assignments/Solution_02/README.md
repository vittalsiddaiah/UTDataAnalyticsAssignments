## Solution
> **NOTE:** All the common libraries needed for this project would be maintained here in [py_lib](https://github.com/vittalsiddaiah/UTDataAnalyticsAssignments/tree/master/Python/py_lib)
### Challenge is yet to be posted...
#### Code:
```python

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
```
#### Output:
```
Emp ID,First Name,Last Name,DOB,SSN,State
232,John,Mathews,02/24/1991,***-**-9165,ND
533,Nathan,Moore,11/19/1978,***-**-7469,ME
256,Amanda,Douglas,01/08/1990,***-**-6961,ID
189,Heather,Andrews,08/11/1976,***-**-1797,VT
284,Daniel,Hernandez,07/22/1976,***-**-7473,CO
:
21,Michelle,Brewer,06/10/1988,***-**-6836,OK
362,Hannah,Nolan,09/15/1978,***-**-1332,OK
368,Erica,Johnson,05/27/1978,***-**-9413,LA
323,Jeremy,Obrien,01/13/1982,***-**-7592,OR

Log path :  data/dst/employee_data_modified.csv

Processed In : [00:00:00:00.0117]  (dd:hh:mm:ss.ssss)

```
******

```Python
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
```
#### Output:
```
    ==================================================================================
    ----------------------------------------------------------------------------------
    Paragraph Analysis
    ----------------------------------------------------------------------------------
    Approximate Word Count     : 130
    Approximate Sentence Count :   5
    Average Letter Count       :   6.39
    Average Sentence Length    :  26.00
    ----------------------------------------------------------------------------------
    Input File  : ../paragraph_1.txt
    Output File : /Users/vsiddaia/Vittal/UT/Assignments/UTDataAnalyticsAssignments/Python/data/dst/paragraph_stats_1.txt
    ==================================================================================
    Processed In : [00:00:00:00.0007]  (dd:hh:mm:ss.ssss)
    
    ==================================================================================
    ----------------------------------------------------------------------------------
    Paragraph Analysis
    ----------------------------------------------------------------------------------
    Approximate Word Count     : 285
    Approximate Sentence Count :  11
    Average Letter Count       :  50.05
    Average Sentence Length    :  25.91
    ----------------------------------------------------------------------------------
    Input File  : ../paragraph_2.txt
    Output File : /Users/vsiddaia/Vittal/UT/Assignments/UTDataAnalyticsAssignments/Python/data/dst/paragraph_stats_2.txt
    ==================================================================================
    Processed In : [00:00:00:00.0009]  (dd:hh:mm:ss.ssss)
    
    ==================================================================================
    ----------------------------------------------------------------------------------
    Paragraph Analysis
    ----------------------------------------------------------------------------------
    Approximate Word Count     : 120
    Approximate Sentence Count :   5
    Average Letter Count       :   4.61
    Average Sentence Length    :  24.00
    ----------------------------------------------------------------------------------
    Input File  : ../test_paragraph.txt
    Output File : /Users/vsiddaia/Vittal/UT/Assignments/UTDataAnalyticsAssignments/Python/data/dst/test_paragraph_stats.txt
    ==================================================================================
    Processed In : [00:00:00:00.0004]  (dd:hh:mm:ss.ssss)
```
#### Support or Contact

For details please contact [email](mailto:vittal.siddaiah@gmail.com) 
