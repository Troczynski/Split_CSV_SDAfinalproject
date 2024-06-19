
import csv
#import Split_csv_Status_Codes
from re import search



#dostajemy csieżkę pliku do dir big file All.csv
a = "All.csv"
b = "ALL_LDK_GRB_SC_30-04.04.23.csv"
c ="SDA_ALL_BUK_MV.csv"
dir_big_file = open(c, "r")

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
#check end of turbines list


def MeasureValues(saved_rows, turbines_list):

    time_to_units_block = [] #3rd block of fixed lines with additional data such as time period, creator and units
    for x in saved_rows[len(turbines_list)+3:len(turbines_list)+7]:
        time_to_units_block.append(x)
    data_available_wtg_no = [] #block of data availability and turbines list not in order
    for x in saved_rows[len(turbines_list)+8:len(turbines_list)+17]:
        data_available_wtg_no.append(x)


    for element in turbines_list:
        nameOfTurbine = f'MV_for_{element.replace("/", "_")}'
        nextfileWTG = open(nameOfTurbine, "w+")

        nextfileWTG.writelines(saved_rows[0:3])
        nextfileWTG.writelines(element + '\n')
        nextfileWTG.writelines(time_to_units_block)
        #for element in  #create loop tubine +data available not the same order as turbineslist
        nextfileWTG.writelines(data_available_wtg_no)






        nextfileWTG.close()


    print("function work MV")




def StatusCode(self):
    print('function work SC')
    #return Split_csv_Status_Codes

    pass



#app choose type of file SC or MV
if saved_rows[1] == sgre_measured_values:
    MeasureValues(saved_rows, turbines_list)
elif saved_rows[1] == sgre_status_code:
    StatusCode(saved_rows)
else:
    print("please check if the file contain Status codes or Measured Values")



new_file_MV = open("TEST_MV.csv", "w+")

# for lines in saved_rows:
#     new_file_MV.writelines(saved_rows)
new_file_MV.writelines(saved_rows[1:33])

new_file_MV.close()

