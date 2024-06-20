"""code maybe working but is very ugly make class and
functions with 2 params input file and amount of turbines /split sections
 and third params measured values or status code
aaa

"""

import csv

def StatusCodesAll(turbines_list, file_directory):

    #if __name__ == "__main__":

    dir_big_file = file_directory
    #OPEN FILE WITH MULTIPLE TURBINES
    csvfile = open(dir_big_file, "r", newline="\r\n")
    bigfile = csv.reader(csvfile, delimiter=';', quotechar='|')

    #SAVED ALL LINES OF FILE IN LIST
    saved_rows = []

    for row in bigfile:
        saved_rows.append(row)

    csvfile.close()
    #CLOSED FILE WITH MULTIPLE TURBINES WORKING WITH SEPERATE_ROWS LIST

    end = len(turbines_list)+3

    start_Status_codes_for = []

    turbines_list = []



    #not used in final version variable end(input) was replaced by function from measured values
    for row in saved_rows[3:end]:
        start = [f'Status codes for  {str(row)[2:-2]}']
        start1 = [f'{str(row)[2:-2]}']
        start_Status_codes_for.append(start)
        turbines_list.append(start1)


    start_s = saved_rows.index(start_Status_codes_for[0])
    end_s = saved_rows.index(start_Status_codes_for[1])

    # CREATE SEPARATE FILES
    i = 0
    for element in turbines_list: #while i <= len(start_Status_codes_for):
        start_s = saved_rows.index(start_Status_codes_for[i])
        try:
            end_s = saved_rows.index(start_Status_codes_for[i + 1])
        except IndexError:
            end_s = len(saved_rows)
        nameOfTurbine = f'sc_WTG {str(turbines_list[i])[2:5]}{i+1}.csv'
        new1 = open(nameOfTurbine, "w+", newline="\n")
        new = csv.writer(new1, delimiter=";")
        new.writerows(saved_rows[0:3])
        new.writerows(saved_rows[i + 3:i + 4])
        new.writerows(saved_rows[end:end + 2])
        # new.writerows(saved_rows[saved_rows.index(turbines_list[i])])
        new.writerows(saved_rows[start_s:end_s])
        new1.close()
        i += 1


