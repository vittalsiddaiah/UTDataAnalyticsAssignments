## Solution
> **NOTE:** All the common libraries needed for this project would be maintained here in [py_lib](https://github.com/vittalsiddaiah/UTDataAnalyticsAssignments/tree/master/Python/py_lib)
### PyBank
#### Code:
```python
########################################################################################################################
def PyBank(input_file, output_file):
    budgetData = csv_parser(input_file, True)
    budgetData.apply(int, column_name='Profit/Losses')
    report = []
    report.append(line())
    report.append("                      Financial Analysis                      ")
    report.append(line())
    report.append("      Total number of months : " + str(len(budgetData)))
    #report.append("                       Total : $(" + str(budgetData.sum('Profit/Losses')) + ")")
    report.append("                       Total : " + to_usd(budgetData.sum('Profit/Losses')) )

    [diff_list, min_diff, min_offset, max_diff, max_offset, diff_sum] = budgetData.diff(column_name='Profit/Losses')
    report.append("              Average Change :" + to_usd(diff_sum/len(diff_list)))
    report.append("Greatest Increase in Profits : "
                  + budgetData.cell(max_offset, 'Date')
                  + "  " + to_usd(max_diff))
    report.append("Greatest Decrease in Profits : "
                  + budgetData.cell(min_offset, 'Date')
                  + "  " + to_usd(min_diff))
    report.append(line())
    finalReport = "\n".join(report) + "\n"

    with open(output_file, 'w') as fd_results:
        fd_results.write(finalReport)
    print(finalReport + "Log path : ", os.path.abspath(output_file) + "\n" + line(2))
    return
########################################################################################################################
```
#### Output:
```
    ----------------------------------------------------------------------------------
                          Financial Analysis                      
    ----------------------------------------------------------------------------------
          Total number of months : 86
                           Total : $38,382,578.00
                  Average Change :(-$2,315.12)
    Greatest Increase in Profits : Feb-12  $1,926,159.00
    Greatest Decrease in Profits : Sep-13  (-$2,196,167.00)
    ----------------------------------------------------------------------------------
    Log path :  data/dst/RevenueResultFile.txt
    ==================================================================================
    Processed In : [00:00:00:00.0014]  (dd:hh:mm:ss.ssss)

```
******

### PyPoll

#### Code:
```python
########################################################################################################################
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
########################################################################################################################
```

#### Output:
```
    ----------------------------------------------------------------------------------
                           Election Results                       
    ----------------------------------------------------------------------------------
    Total Votes: 3521001
    ----------------------------------------------------------------------------------
          Khan,  63.00%,  2218231
        Correy,  20.00%,   704200
            Li,  14.00%,   492940
      O'Tooley,   3.00%,   105630
    ----------------------------------------------------------------------------------
    Winner: Khan
    ----------------------------------------------------------------------------------
    Log path :  data/dst/ElectionResultFile.txt
    ==================================================================================
    Processed In : [00:00:00:15.8322]  (dd:hh:mm:ss.ssss)
```

#### Support or Contact

For details please contact [email](mailto:vittal.siddaiah@gmail.com) 
