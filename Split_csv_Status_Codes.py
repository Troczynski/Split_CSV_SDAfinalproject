"""code maybe working but is very ugly make class and
functions with 2 params input file and amount of turbines /split sections
 and third params measured values or status code
aaa

"""

# import csv
# #import Split_csv_Measured_values
#
# #if __name__ == "__main__":
#
# dir_big_file = input("Status code file directory ")
# #OPEN FILE WITH MULTIPLE TURBINES
# csvfile = open(dir_big_file, "r", newline="\r\n")
# bigfile = csv.reader(csvfile, delimiter=';', quotechar='|')
#
# #SAVED ALL LINES OF FILE IN LIST
# saved_rows = []
#
# for row in bigfile:
#     saved_rows.append(row)
#
# csvfile.close()
# #CLOSED FILE WITH MULTIPLE TURBINES WORKING WITH SEPERATE_ROWS LIST
#
#
# end = int(input("number of turbines/ section to split: ")) + 3


def StatusCode(saved_rows, turbines_list):
    time_to_units_block = []  # 3rd block of fixed lines with additional data such as time period, creator and units
    for x in saved_rows[len(turbines_list) + 3:len(turbines_list) + 6]:
        time_to_units_block.append(x)
    start_Status_codes_for = []  # block of data availability and turbines list not in order 3* due to turbines list is iterat 2 times and one time data vailable
    for row in saved_rows[3:len(turbines_list)+3]:
        start = f'Status codes for  {str(row)[:-2]}'
        start_Status_codes_for.append(start)

    print(start_Status_codes_for)
    for element in turbines_list:
        nameOfTurbine = f'SC_for_{element.replace("/", "_")}.csv'  # create name of the file based on wtg
        nextfileWTG = open(nameOfTurbine, "w+")  # create and open file(singular wtg)
        nextfileWTG.writelines(saved_rows[0:3])  # save 1st fixed block of text
        nextfileWTG.writelines(element + '\n')
        nextfileWTG.writelines(time_to_units_block)
        #status code for line
        #units line


        nextfileWTG.close()











#not used in final version variable end(input) was replaced by function from measured values


# start_s = saved_rows.index(start_Status_codes_for[0])
# end_s = saved_rows.index(start_Status_codes_for[1])
#
# # CREATE SEPARATE FILES
# i = 0
# for element in turbines_list: #while i <= len(start_Status_codes_for):
#     start_s = saved_rows.index(start_Status_codes_for[i])
#     try:
#         end_s = saved_rows.index(start_Status_codes_for[i + 1])
#     except IndexError:
#         end_s = len(saved_rows)
#     nameOfTurbine = f'sc_WTG {str(turbines_list[i])[2:5]}{i+1}.csv'
#     new1 = open(nameOfTurbine, "w+", newline="\n")
#     new = csv.writer(new1, delimiter=";")
#     new.writerows(saved_rows[0:3])
#     new.writerows(saved_rows[i + 3:i + 4])
#     new.writerows(saved_rows[end:end + 2])
#     # new.writerows(saved_rows[saved_rows.index(turbines_list[i])])
#     new.writerows(saved_rows[start_s:end_s])
#     new1.close()
#     i += 1


