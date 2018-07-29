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
    Dim maxvolrow As Long
    Dim maxvol As Double

    Dim totalCounter As Long
    Dim totalTickers As Double
    Dim tickerSwitch As bool



    For Each wkSheet In Worksheets
        'Initializations
        totalCounter = 2
        totalTickers = 0
        tickerSwitch = true
        firstRow = 2
        lastRow = wkSheet.Cells(RowkSheet.Count, 1).End(xlUp).Row

        wkSheet.Cells(totalCounter - 1, 9).Value = "Ticker"
        wkSheet.Cells(totalCounter - 1, 10).Value = "Yearly Change"
        wkSheet.Cells(totalCounter - 1, 11).Value = "Percent Change"
        wkSheet.Cells(totalCounter - 1, 12).Value = "Total Stock Volume"

        wkSheet.Cells(totalCounter - 1, 16).Value = "Ticker"
        wkSheet.Cells(totalCounter - 1, 17).Value = "Value"  
        
        For i = firstRow To lastRow
            If wkSheet.Cells(i, 1).Value <> wkSheet.Cells(i + 1, 1).Value Then
                totalTickers = totalTickers + wkSheet.Cells(i, 7).Value
                wkSheet.Cells(totalCounter, 9).Value = wkSheet.Cells(i, 1).Value
                wkSheet.Cells(totalCounter, 12).Value = totalTickers
                totalTickers = 0
                
                closePrice = wkSheet.Cells(i, 6).Value
                yearlyChange = closePrice - openPrice
                wkSheet.Cells(totalCounter, 10).Value = yearlyChange
                percentChange = (closePrice - openPrice) * 100 / (openPrice)
                wkSheet.Cells(totalCounter, 11).Value = percentChange

                If yearlyChange > 0 Then
                    With wkSheet.Cells(totalCounter, 10)
                 .Interior.Color = vbGreen
                 .Font.Color = vbBlack
                 End With
                Else
                    With wkSheet.Cells(totalCounter, 10)
                        .Interior.Color = vbRed
                        .Font.Color = vbBlack
                    End With
                End If
                tickerSwitch = true
                totalCounter = totalCounter + 1
                
            Else
                totalTickers = totalTickers + wkSheet.Cells(i, 7).Value
                If tickerSwitch = true And wkSheet.Cells(i, 3) <> 0 Then
                   openPrice = wkSheet.Cells(i, 3).Value
                   tickerSwitch = false
                End If
            End If
        
        Next i
        
        lastRow = wkSheet.Cells(RowkSheet.Count, 11).End(xlUp).Row
        
        max = 0 
        min = 0 
        maxvol = 0 
        
            For i = 2 To lastRow
                'loop through values
                If wkSheet.Cells(i, 12).Value <> 0 Then
                        ' locate the highest volume and save the corresonding row values
                        If wkSheet.Cells(i, 12).Value > maxvol And wkSheet.Cells(i, 12).Value <> 0 Then 'if a value is larger than the old max,
                             maxvol = wkSheet.Cells(i, 12).Value ' store it as the new max!
                             maxvolrow = i
                        End If
        
                        ' locate the highest % increase and save the corresonding row values
                        If wkSheet.Cells(i, 11).Value > max And wkSheet.Cells(i, 12).Value <> 0 Then 'if a value is larger than the old max,
                             max = wkSheet.Cells(i, 11).Value ' store it as the new max!
                             maxRow = i
                        End If
        
                        ' locate the highest % decrease and save the corresonding row values
                        If wkSheet.Cells(i, 11).Value < min And wkSheet.Cells(i, 12).Value <> 0 Then 'if a value is less than the old min ,
                             min = wkSheet.Cells(i, 11).Value ' store it as the new min!
                             minRow = i
                        End If
            End If
            Next i

            ' Move the % high increase values
        wkSheet.Cells(2, 17).Value = max
        wkSheet.Cells(2, 16).Value = wkSheet.Cells(maxRow, 9).Value
        wkSheet.Cells(2, 15).Value = "Greatest % Increase"

        ' Move the % high decrease values
        wkSheet.Cells(3, 17).Value = min
        wkSheet.Cells(3, 16).Value = wkSheet.Cells(minRow, 9).Value
        wkSheet.Cells(3, 15).Value = "Greatest % Decrease"

        ' Move the Max Volume values
        wkSheet.Cells(4, 17).Value = maxvol
        wkSheet.Cells(4, 16).Value = wkSheet.Cells(maxvolrow, 9).Value
        wkSheet.Cells(4, 15).Value = "Greatest % Volume"
 
        ' MsgBox (wkSheet.Name)
        'Exit For
        
     Next wkSheet
   
End Sub
```

