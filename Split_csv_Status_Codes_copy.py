"""code maybe working but is very ugly make class and
functions with 2 params input file and amount of turbines /split sections
 and third params measured values or status code
aaa

"""


import csv
#import Split_csv_Measured_values

#if __name__ == "__main__":

dir_big_file = input("Status code file directory ")
#OPEN FILE WITH MULTIPLE TURBINES
csvfile = open(dir_big_file, "r", newline="\r\n")
bigfile = csv.reader(csvfile, delimiter=';', quotechar='|')

#SAVED ALL LINES OF FILE IN LIST
saved_rows3 = []

for row in bigfile:
    saved_rows3.append(row)

csvfile.close()
#CLOSED FILE WITH MULTIPLE TURBINES WORKING WITH SEPERATE_ROWS LIST
print(print(f'saved rows from Split SC COPY: {repr(saved_rows3[1:3])}'))







def StatusCode(saved_rows2, turbines_list):
    end = int(input("number of turbines/ section to split: ")) + 3
    print(f' to jest wpisane z łay:{end}')
    print(f' a to jest z listy: {len(turbines_list)+3}')
    turbines_list1 = []
    start_Status_codes_for = []
#not used in final version variable end(input) was replaced by function from measured values
    for row in saved_rows2[3:end]:
        start = [f'Status codes for  {str(row)[2:-2]}']
        start1 = [f'{str(row)[2:-2]}'] #dopasować strin z SC do string Vfiled \n
        start_Status_codes_for.append(start)
        turbines_list1.append(start1)

    print(repr(turbines_list))

    print(repr(start_Status_codes_for[0]))
    print(repr(turbines_list[0]))

    start_s = saved_rows2.index(start_Status_codes_for[0])
    end_s = saved_rows2.index(start_Status_codes_for[1])

    # CREATE SEPARATE FILES
    i = 0
    for element in turbines_list: #while i <= len(start_Status_codes_for):
        start_s = saved_rows2.index(start_Status_codes_for[i])
        try:
            end_s = saved_rows2.index(start_Status_codes_for[i + 1])
        except IndexError:
            end_s = len(saved_rows2)
        nameOfTurbine = f'sc_WTG {str(turbines_list[i])[2:5]}{i+1}.csv'
        new1 = open(nameOfTurbine, "w+", newline="\n")
        new = csv.writer(new1, delimiter=";")
        new.writerows(saved_rows2[0:3])
        new.writerows(saved_rows2[i + 3:i + 4])
        new.writerows(saved_rows2[end:end + 2])
        # new.writerows(saved_rows[saved_rows.index(turbines_list[i])])
        new.writerows(saved_rows2[start_s:end_s])
        new1.close()
        i += 1

StatusCode(saved_rows3,turbines_list1)
