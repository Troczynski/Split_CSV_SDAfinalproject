import pandas as pd
import csv
#import Split_csv_Status_Codes
from re import search



#dostajemy csieżkę pliku do dir big file All.csv
a = "All.csv"
b = "ALL_LDK_GRB_SC_30-04.04.23.csv"
dir_big_file = open(b, "r")

#sprawdzamy rodzaj pliku
saved_rows = []
for row in dir_big_file:
    saved_rows.append(row)

dir_big_file.close()

sgre_measured_values = '10 Minute Values, detailed\n'
sgre_status_code = 'Status code list\n'

def Wtg_list(saved_rows):
    turbines_list = []
    start_Status_codes_for = []
    time_period = "time period:"
    for el in saved_rows[3:]:
        if str(el)[0:12] == time_period:
            break
        turbines_list.append(el[:-2])
        sc = [f'Status codes for  {el[:-2]}']
        start_Status_codes_for.append(sc)
    return turbines_list

turbines_list = Wtg_list(saved_rows)



time_period = "time period:"

print(repr(str(saved_rows[12])[0:12]))

def MeasureValues(self):
    print("function work MV")



def StatusCode(self):
    print('function work SC')
    #return Split_csv_Status_Codes

    pass




if saved_rows[1] == sgre_measured_values:
    MeasureValues(saved_rows)
elif saved_rows[1] == sgre_status_code:
    StatusCode(saved_rows)
else:
    print("please check if the file contain Status codes or Measured Values")



new_file_MV = open("TEST_MV.csv", "w+")

# for lines in saved_rows:
#     new_file_MV.writelines(saved_rows)
new_file_MV.writelines(saved_rows[1:33])

new_file_MV.close()

