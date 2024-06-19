
import csv
#import Split_csv_Status_Codes
from re import search
#from workfile import StatusCode

#dostajemy csieżkę pliku do dir big file All.csv

a = "All.csv"
b = "ALL_LDK_GRB_SC_30-04.04.23.csv"
c = "SDA_ALL_BUK_MV.csv"
d = "SDA ALL GZK WTG MV.csv"
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
        turbines_list.append(el[:-1])
        sc = [f'Status codes for  {el[:-1]}']
        start_Status_codes_for.append(sc)
    return turbines_list


turbines_list = Wtg_list(saved_rows)
#check end of turbines list
print(turbines_list)

def MeasureValues(saved_rows, turbines_list):

    time_to_units_block = [] #3rd block of fixed lines with additional data such as time period, creator and units
    for x in saved_rows[len(turbines_list)+3:len(turbines_list)+7]:
        time_to_units_block.append(x)
    data_available_wtg_no = [] #block of data availability and turbines list not in order
    for y in saved_rows[len(turbines_list)+7:len(turbines_list)*3+7]:
        data_available_wtg_no.append(y)



    for element in turbines_list:
        nameOfTurbine = f'MV_for_{element.replace("/", "_")}.csv' #create name of the file based on wtg
        nextfileWTG = open(nameOfTurbine, "w+") #create and open file(singular wtg)
        nextfileWTG.writelines(saved_rows[0:3]) #save 1st fixed block of text
        nextfileWTG.writelines(element + '\n')
        nextfileWTG.writelines(time_to_units_block)
        #for element in  #create loop tubine +data available not the same order as turbineslist
        for wtg in data_available_wtg_no:
             if wtg == f'{element}\n':
                print(f'{element}\n')
                print(data_available_wtg_no)
                #nextfileWTG.writelines(data_available_wtg_no)
                nextfileWTG.writelines(wtg)
                nextfileWTG.writelines(data_available_wtg_no[
                                           data_available_wtg_no.index(wtg)+1
                                       ])
                break
        nextfileWTG.writelines('\n')
        nextfileWTG.writelines(saved_rows[len(turbines_list)*3+8]) # timestamp line
        #create loop with data based on wtg number
        # time stam to ";" first line which is an index of line to start in next iteration
        nextfileWTG.writelines(saved_rows[len(turbines_list) * 3 + 9:])
        # for dataline in saved_rows[len(turbines_list)*3+8:100]:

        start_index_data = len(turbines_list) * 3 + 9
        end_index_data = 0
        mv_data = saved_rows[start_index_data:end_index_data]
        for el in saved_rows[start_index_data:]:
            if str(el)[0:1] != ";":
                nextfileWTG.writelines(el)
            else:
                start_index_data = len(el)
            break

        nextfileWTG.close()

    print("function work MV")




def StatusCode(saved_rows, turbines_list):
    print('function work SC')
    #return Split_csv_Status_Codes

    pass



#app choose type of file SC or MV
if saved_rows[1] == sgre_measured_values:
    MeasureValues(saved_rows, turbines_list)
elif saved_rows[1] == sgre_status_code:
    StatusCode(saved_rows, turbines_list)
else:
    print("please check if the file contain Status codes or Measured Values")



new_file_MV = open("TEST_MV.csv", "w+")

# for lines in saved_rows:
#     new_file_MV.writelines(saved_rows)
new_file_MV.writelines(saved_rows[1:33])

new_file_MV.close()

