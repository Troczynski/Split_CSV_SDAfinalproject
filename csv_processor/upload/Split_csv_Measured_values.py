import csv
from datetime import datetime, timedelta

# import Split_csv_Status_Codes

# from workfile import StatusCode

# dostajemy csieżkę pliku do dir big file All.csv

# a = "All.csv"
# b = "ALL_LDK_GRB_SC_30-04.04.23.csv"
# c = "SDA_ALL_BUK_MV.csv"
# d = "SDA ALL GZK WTG MV.csv"
# e = "ALL_LDK_GRB_MV_30-04.04.23.csv"
# f = "SDA_LDK01_03_MV18.06_20.06.csv"
# final_test = "SDA_ALL_GZK_MV14_20.06.csv"
# dir_big_file = open(final_test, "r")

# sprawdzamy rodzaj pliku
# saved_rows = []
# for row in dir_big_file:
#     saved_rows.append(row)
#
# dir_big_file.close()
#
# sgre_measured_values = '10 Minute Values, detailed\n'
# sgre_status_code = 'Status code list\n'


# def wtg_list(saved_rows):
#     turbines_list = []
#     start_status_codes_for = []
#
#     time_period = "time period:"
#     for el in saved_rows[3:]:
#         if str(el)[0:12] == time_period:
#             break
#         turbines_list.append(el[:-1])
#         sc = [f'Status codes for  {el[:-1]}']
#         start_status_codes_for.append(sc)
#     return turbines_list


def TimePeriod(saved_rows, turbines_list):
    str_start_date = str(saved_rows[len(turbines_list) + 3])[13:23]
    str_end_date = str(saved_rows[len(turbines_list) + 3])[26:36]
    start_date = datetime.strptime(str_start_date, "%d/%m/%Y").date()
    end_date = datetime.strptime(str_end_date, "%d/%m/%Y").date()
    timedelta = (end_date - start_date).days
    data_lines_number = 144 + 144 * timedelta

    return data_lines_number


#turbines_list = wtg_list(saved_rows)



def MeasureValues(saved_rows, turbines_list, number_of_lines):
#    below 2 variables with blocks of lines - app more efficient
    time_to_units_block = []  # 3rd block of fixed lines with additional data such as time period, creator and units
    for x in saved_rows[len(turbines_list) + 3:len(turbines_list) + 7]:
        time_to_units_block.append(x)
    data_available_wtg_no = []  # block of data availability and turbines list not in order 3* due to turbines list is iterat 2 times and one time data vailable
    for y in saved_rows[len(turbines_list) + 7:len(turbines_list) * 3 + 7]:
        data_available_wtg_no.append(y)


    start_index_data = len(turbines_list) * 3 + 9
    end_index_data = len(
        turbines_list) * 3 + 9 + number_of_lines

    for element in turbines_list:
        nameOfTurbine = f'MV_for_{element.replace("/", "_")}.csv'  # create name of the file based on wtg
        nextfileWTG = open(nameOfTurbine, "w+")  # create and open file(singular wtg)
        nextfileWTG.writelines(saved_rows[0:3])  # save 1st fixed block of text
        nextfileWTG.writelines(element + '\n')
        nextfileWTG.writelines(time_to_units_block)
        # for element in  #create loop tubine +data available not the same order as turbineslist
        for wtg in data_available_wtg_no:
            if wtg == f'{element}\n':
                nextfileWTG.writelines(wtg)
                nextfileWTG.writelines(data_available_wtg_no[
                                           data_available_wtg_no.index(wtg) + 1
                                           ])
                break
        nextfileWTG.writelines('\n')
        nextfileWTG.writelines(saved_rows[len(turbines_list) * 3 + 8])  # timestamp line
        # data copy based on index of lines in saved_rows. Every 24 hours has 144 lines of data (number of lines)

        nextfileWTG.writelines(saved_rows[start_index_data:end_index_data])
        start_index_data += number_of_lines
        start_index_data += 1  # lineseparator
        end_index_data += number_of_lines
        end_index_data += 1  # lineseparator


        nextfileWTG.close()


def StatusCode(saved_rows, turbines_list):
    print('function work SC')
    # return Split_csv_Status_Codes

    pass


# app choose type of file SC or MV
# if saved_rows[1] == sgre_measured_values:
#     MeasureValues(saved_rows, turbines_list,data_lines_per_WTG)
# elif saved_rows[1] == sgre_status_code:
#     StatusCode(saved_rows, turbines_list)
# else:
#     print("please check if the file contain Status codes or Measured Values")