import os
import sys
sys.path.insert(1, r'../../py_lib/')
from py_lib.csv_parser import csv_parser
from py_lib.timer import timer
from py_lib.h_line import h_line


def to_usd(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '(-${:,.2f})'.format(-amount)

########################################################################################################################
def PyBank(input_file, output_file):
    budgetData = csv_parser(input_file, True)
    budgetData.apply(int, column_name='Profit/Losses')
    report = []
    report.append(h_line())
    report.append("                      Financial Analysis                      ")
    report.append(h_line())
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
    report.append(h_line())
    finalReport = "\n".join(report) + "\n"

    with open(output_file, 'w') as fd_results:
        fd_results.write(finalReport)

    print("\n" + finalReport + "Input File  : " + os.path.abspath(input_file))
    print("Output File : " + os.path.abspath(output_file) + "\n" + h_line(2))
    return
########################################################################################################################

########################################################################################################################
def PyPoll(input_file, output_file):
    print("\n\nParsing Election Data...")
    electionData = csv_parser(input_file, True)
    candidateCount = electionData.count_unique('Candidate')
    resultArray = csv_parser(candidateCount, False)
    resultArray.columns(['Candidate', 'TotalCount'])
    resultArray.insert_pctg('TotalCount')

    report = []
    report.append(h_line())
    report.append("                       Election Results                       ")
    report.append(h_line())
    report.append("Total Votes: %d" % len(electionData))
    report.append(h_line())
    for offset in range(len(resultArray)):
        report.append("%10s, %6.2f%%, %8d" % (resultArray.cell(offset, column_offset=0),
                                              resultArray.cell(offset, column_offset=2) * 100.0,
                                              resultArray.cell(offset, column_offset=1)))

    report.append(h_line())
    report.append("Winner: " + resultArray.cell(resultArray.max('TotalCount')[1], column_offset=0))
    report.append(h_line())
    finalReport = "\n".join(report) + "\n"

    with open(output_file, 'w') as fd_results:
        fd_results.write(finalReport)
    print("\n" + finalReport + "Input File  : " + os.path.abspath(input_file))
    print("Output File : " + os.path.abspath(output_file) + "\n" + h_line(2))
    return
########################################################################################################################

########################################################################################################################
if __name__ == '__main__':
    timing = timer('Processed In : ')
    PyBank("../../data/src/budget_data.csv", "../../data/dst/RevenueResultFile.txt")
    print(timing.delta_str())
    timing.reset()
    PyPoll("../../data/src/election_data.csv", "../../data/dst/ElectionResultFile.txt")
    print(timing.delta_str())
########################################################################################################################