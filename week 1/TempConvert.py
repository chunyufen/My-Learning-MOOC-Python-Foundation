#TempConvert.py
TempStr = input("請輸入帶有符號的溫度值：") # The output is a string
if TempStr[-1] in ['F', 'f']: # ['F', 'f'] is a list
    C = ((float(TempStr[0:-1]) - 32)/1.8) # change string to float for calculation
    print("轉換後的溫度是{:.2f}C".format(C)) # {:} is fill in the blank, with what? with C, in what format? with 2 decimal places (.2f) 
elif TempStr[-1] in ['C', 'c']:
    F = 1.8*float(TempStr[0:-1]) + 32
    print("轉換後的溫度是{:.2f}F".format(F))
else:
    print("輸入格式錯誤。")
