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

	Dim pctgOffset as Integer
    pctgOffset = 2

    For Each wkSheet In Worksheets
        'Initializations
        totalCounter = 2
        totalTickers = 0
        tickerSwitch = True
        firstRow = 2
        lastRow = wkSheet.Cells(Rows.Count, 1).End(xlUp).Row

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
                        .Font.Color = vbYellow
                    End With
                End If
                tickerSwitch = True
                totalCounter = totalCounter + 1
                
            Else
                totalTickers = totalTickers + wkSheet.Cells(i, 7).Value
                If tickerSwitch = True And wkSheet.Cells(i, 3) <> 0 Then
                   openPrice = wkSheet.Cells(i, 3).Value
                   tickerSwitch = False
                End If
            End If
        
        Next i
        
        lastRow = wkSheet.Cells(Rows.Count, 1).End(xlUp).Row
        
        max = 0
        min = 0
        maxVol = 0
        
            For i = 2 To lastRow
                'loop through values
                If wkSheet.Cells(i, 12).Value <> 0 Then
                        ' Search for highest volume  and save it accordingly to its row value
                        If wkSheet.Cells(i, 12).Value > maxVol And wkSheet.Cells(i, 12).Value <> 0 Then 
                             maxVol = wkSheet.Cells(i, 12).Value ' store it as the new max!
                             maxVolrow = i
                        End If

                        ' Search for highest percentage increase and save it accordingly to its row value
                        If wkSheet.Cells(i, 11).Value > max And wkSheet.Cells(i, 12).Value <> 0 Then 
                             max = wkSheet.Cells(i, 11).Value ' store it as the new max!
                             maxRow = i
                        End If

                        ' Search for highest percentage decrease and save it accordingly to its row value
                        If wkSheet.Cells(i, 11).Value < min And wkSheet.Cells(i, 12).Value <> 0 Then 
                             min = wkSheet.Cells(i, 11).Value ' store it as the new min!
                             minRow = i
                        End If
                End If
            Next i

        ' Update the Percentage high increase values

        wkSheet.Cells(pctgOffset, 17).Value = max
        wkSheet.Cells(pctgOffset, 16).Value = wkSheet.Cells(maxRow, 9).Value
        wkSheet.Cells(pctgOffset, 15).Value = "Greatest % Increase"

        ' Update the Percentage high decrease values
        wkSheet.Cells(pctgOffset + 1, 17).Value = min
        wkSheet.Cells(pctgOffset + 1, 16).Value = wkSheet.Cells(minRow, 9).Value
        wkSheet.Cells(pctgOffset + 1, 15).Value = "Greatest % Decrease"

        ' Update the Percentage high greatest Volume
        wkSheet.Cells(pctgOffset + 2, 17).Value = maxVol
        wkSheet.Cells(pctgOffset + 2, 16).Value = wkSheet.Cells(maxVolrow, 9).Value
        wkSheet.Cells(pctgOffset + 2, 15).Value = "Greatest % Volume"
        
     Next wkSheet
   
End Sub


```

