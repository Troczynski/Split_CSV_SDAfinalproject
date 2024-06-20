# choose wich splitter
import Split_csv_Measured_values

import Split_csv_Status_Codes_all

a = "All.csv"
path_of_the_file = "ALL_LDK_GRB_SC_30-04.04.23.csv"
c = "SDA_ALL_BUK_MV.csv"
d = "SDA ALL GZK WTG MV.csv"
e = "ALL_LDK_GRB_MV_30-04.04.23.csv"
f = "SDA_LDK01_03_MV18.06_20.06.csv"
dire = "SDA_ALL_GZK_MV14_20.06.csv"
dir_big_file = open(path_of_the_file, "r")

# sprawdzamy rodzaj pliku
saved_rows1 = []
for row in dir_big_file:
    saved_rows1.append(row)

dir_big_file.close()

sgre_measured_values = '10 Minute Values, detailed\n'
sgre_status_code = 'Status code list\n'
def wtg_list(saved_rows):
    turbines_list1 = []
    start_status_codes_for = []

    time_period = "time period:"
    for el in saved_rows[3:]:
        if str(el)[0:12] == time_period:
            break
        turbines_list1.append(el[:-1])
        sc = [f'Status codes for  {el[:-1]}']
        start_status_codes_for.append(sc)
    return turbines_list1

turbines_list = wtg_list(saved_rows1)

data_lines_per_WTG = Split_csv_Measured_values.TimePeriod(saved_rows1, turbines_list)

# app choose type of file SC or MV
if saved_rows1[1] == sgre_measured_values:
    Split_csv_Measured_values.MeasureValues(saved_rows1, turbines_list,data_lines_per_WTG)
elif saved_rows1[1] == sgre_status_code:
    Split_csv_Status_Codes_all.StatusCodesAll(turbines_list,path_of_the_file)


else:
    print("please check if the file contain Status codes or Measured Values")
