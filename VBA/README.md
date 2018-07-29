## Assignment on VBA


```vba
Sub TotalTicker()

    ' --------------------------------------------
    ' TotalTicker is a generic script that can utitlized over ticker tables
    ' Contact: vittal.siddaiah@gmail.com
    ' --------------------------------------------
    Dim openPrice As Double
    Dim closePrice As Double

    Dim firstRow As Long
    Dim lastRow As Long

    Dim yearlyChange As Double
    Dim percentChange As Double
    
    Dim max As Double
    Dim min As Double
    Dim minRow As Long
    Dim maxRow As Long
    Dim maxVolrow As Long
    Dim maxVol As Double

    Dim totalCounter As Long
    Dim totalTickers As Double
    Dim tickerSwitch As Boolean
    
    Dim startTime As Double
    Dim timeSpentInMins As String
    Dim condColIndex As Integer
    Dim headColIndex As Integer

    startTime = Timer
    For Each wkSheet In Worksheets
        'Initializations
        totalCounter = 2
        totalTickers = 0
        tickerSwitch = True
        firstRow = 2
        max = 0
        min = 0
        maxVol = 0

        resultRow = 2
        headColIndex = 27
        lastRow = wkSheet.Cells(Rows.Count, 1).End(xlUp).Row

            ''Formatting the cells
        wkSheet.Cells(resultRow - 1, 9).Value = "Ticker"
        wkSheet.Cells(resultRow - 1, 10).Value = "Yearly Change"
        wkSheet.Cells(resultRow - 1, 11).Value = "Percent Change"
        wkSheet.Cells(resultRow - 1, 12).Value = "Total Stock Volume"
        wkSheet.Cells(resultRow - 1, 9).Interior.ColorIndex = headColIndex
        wkSheet.Cells(resultRow - 1, 10).Interior.ColorIndex = headColIndex
        wkSheet.Cells(resultRow - 1, 11).Interior.ColorIndex = headColIndex
        wkSheet.Cells(resultRow - 1, 12).Interior.ColorIndex = headColIndex
        wkSheet.Cells(resultRow - 1, 9).ColumnWidth = 12
        wkSheet.Cells(resultRow - 1, 10).ColumnWidth = 12
        wkSheet.Cells(resultRow - 1, 11).ColumnWidth = 14
        wkSheet.Cells(resultRow - 1, 12).ColumnWidth = 16
        
        wkSheet.Cells(resultRow - 1, 16).Value = "Ticker"
        wkSheet.Cells(resultRow - 1, 17).Value = "Value"
        wkSheet.Cells(resultRow - 1, 16).Interior.ColorIndex = headColIndex
        wkSheet.Cells(resultRow - 1, 17).Interior.ColorIndex = headColIndex
        wkSheet.Cells(resultRow - 1, 15).ColumnWidth = 20


        
        ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

        For Row = firstRow To lastRow    ''row iterator start
            ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            If wkSheet.Cells(Row, 1).Value <> wkSheet.Cells(Row + 1, 1).Value Then
                totalTickers = totalTickers + wkSheet.Cells(Row, 7).Value
                wkSheet.Cells(totalCounter, 9).Value = wkSheet.Cells(Row, 1).Value
                wkSheet.Cells(totalCounter, 12).Value = totalTickers
                totalTickers = 0
                
                closePrice = wkSheet.Cells(Row, 6).Value
                yearlyChange = closePrice - openPrice
                wkSheet.Cells(totalCounter, 10).Value = yearlyChange
                wkSheet.Cells(totalCounter, 11).Value = (closePrice - openPrice) / (openPrice) ''Percentage Change Calculation...
                wkSheet.Cells(totalCounter, 11).NumberFormat = "0.00%"
                ''Conditional format of cells
                condColIndex = 0
                If yearlyChange > 0 Then
                    condColIndex = 4
                Else
                    condColIndex = 3
                End If
                wkSheet.Cells(totalCounter, 9).Interior.ColorIndex = condColIndex
                wkSheet.Cells(totalCounter, 10).Interior.ColorIndex = condColIndex
                wkSheet.Cells(totalCounter, 11).Interior.ColorIndex = condColIndex
                wkSheet.Cells(totalCounter, 12).Interior.ColorIndex = condColIndex
                    
                tickerSwitch = True
                totalCounter = totalCounter + 1
                
            Else
                totalTickers = totalTickers + wkSheet.Cells(Row, 7).Value
                If tickerSwitch = True And wkSheet.Cells(Row, 3) <> 0 Then
                   openPrice = wkSheet.Cells(Row, 3).Value
                   tickerSwitch = False
                End If
            End If
        
            ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            If wkSheet.Cells(Row, 12).Value <> 0 Then
                If wkSheet.Cells(Row, 12).Value > maxVol Then
                     maxVol = wkSheet.Cells(Row, 12).Value
                     maxVolrow = Row
                End If
                If wkSheet.Cells(Row, 11).Value > max Then
                     max = wkSheet.Cells(Row, 11).Value
                     maxRow = Row
                ElseIf wkSheet.Cells(Row, 11).Value < min Then
                     min = wkSheet.Cells(Row, 11).Value
                     minRow = Row
                End If
            End If
            ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        Next Row ''row iterator end
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    ' Update the Percentage high increase values
    wkSheet.Cells(resultRow, 17).Value = max
    wkSheet.Cells(resultRow, 16).Value = wkSheet.Cells(maxRow, 9).Value
    wkSheet.Cells(resultRow, 15).Value = "Greatest % Increase"

    ' Update the Percentage high decrease values
    wkSheet.Cells(resultRow + 1, 17).Value = min
    wkSheet.Cells(resultRow + 1, 16).Value = wkSheet.Cells(minRow, 9).Value
    wkSheet.Cells(resultRow + 1, 15).Value = "Greatest % Decrease"

    ' Update the Percentage high greatest Volume
    wkSheet.Cells(resultRow + 2, 17).Value = maxVol
    wkSheet.Cells(resultRow + 2, 16).Value = wkSheet.Cells(maxVolrow, 9).Value
    wkSheet.Cells(resultRow + 2, 15).Value = "Greatest % Volume"
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


    Next wkSheet  ''Sheet iterator end
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    timeSpentInMins = Format((Timer - startTime) / 86400, "hh:mm:ss")
    MsgBox "Update Completed in hh::mm::ss  " & timeSpentInMins, vbInformation
End Sub
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
```

