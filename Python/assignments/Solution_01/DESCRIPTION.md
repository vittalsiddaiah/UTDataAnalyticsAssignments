## Solution
### PyBank
#### Code:
```python
def PyBank(input_file, output_file):
    budgetData = csv_parser(input_file, True)
    budgetData.apply('Revenue', int)
    report = []
    report.append(line())
    report.append("                      Financial Analysis                      ")
    report.append(line())
    report.append("      Total number of months : " + str(len(budgetData)))
    report.append("                       Total : $(" + str(budgetData.sum('Revenue')) + ")")
    [maxValue, maxOffset] = budgetData.max(column_name='Revenue')
    [minValue, minOffset] = budgetData.min(column_name='Revenue')
    report.append("Greatest Increase in Profits : " + budgetData.cell(maxOffset, 'Date') + "  $(" + str(
        maxValue) + ")")
    report.append("Greatest Decrease in Profits : " + budgetData.cell(minOffset, 'Date') + "  $(" + str(
        minValue) + ")")
    report.append(line())

    finalReport = "\n".join(report) + "\n"

    with open(output_file, 'w') as fd_results:
        fd_results.write(finalReport)
    print(finalReport + "Log path : ", os.path.abspath(output_file) + "\n" + line(2))
    return
```
#### Output:



### PyPoll
#### Code:
```python
def PyPoll(input_file, output_file):
    print("\n\nParsing Election Data...")
    electionData = csv_parser(input_file, True)
    candidateCount = electionData.count_unique('Candidate')
    resultArray = csv_parser(candidateCount, False)
    resultArray.columns(['Candidate', 'TotalCount'])
    resultArray.insert_pctg('TotalCount')

    report = []
    report.append(line())
    report.append("                       Election Results                       ")
    report.append(line())
    report.append("Total Votes: %d" % len(electionData))
    report.append(line())
    for offset in range(len(resultArray)):
        report.append("%10s, %6.2f%%, %8d" % (resultArray.cell(offset, column_offset=0),
                                              resultArray.cell(offset, column_offset=2) * 100.0,
                                              resultArray.cell(offset, column_offset=1)))

    report.append(line())
    report.append("Winner: " + resultArray.cell(resultArray.max('TotalCount')[1], column_offset=0))
    report.append(line())
    finalReport = "\n".join(report) + "\n"

    with open(output_file, 'w') as fd_results:
        fd_results.write(finalReport)
    print(finalReport + "Log path : ", os.path.abspath(output_file) + "\n" + line(2))
    return
```
#### Output:

#### Support or Contact

For details please contact [email](vittal.siddaiah@gmail.com).
