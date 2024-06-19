

#3rd block of fixed lines with additional data such as time period, creator and units"""
if __name__ == "__main__":
    turbine = ["wtg1", "wtg2", "wtg3", "wt4"]

    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for el in turbine:
        print("1")

import csv
from Split_csv_Measured_values import saved_rows, turbines_list


def StatusCode(saved_rows, turbines_list):
    i = 0
    for element in turbines_list:  # while i <= len(start_Status_codes_for):
        start_s = saved_rows.index(start_Status_codes_for[i])
        try:
            end_s = saved_rows.index(start_Status_codes_for[i + 1])
        except IndexError:
            end_s = len(saved_rows)
        nameOfTurbine = f'sc_WTG {str(turbines_list[i])[2:5]}{i + 1}.csv'
        new1 = open(nameOfTurbine, "w+", newline="\n")
        new = csv.writer(new1, delimiter=";")
        new.writerows(saved_rows[0:3])
        new.writerows(saved_rows[i + 3:i + 4])
        new.writerows(saved_rows[end:end + 2])
        # new.writerows(saved_rows[saved_rows.index(turbines_list[i])])
        new.writerows(saved_rows[start_s:end_s])
        new1.close()
        i += 1

    print('function work SC')
    #return Split_csv_Status_Codes

    pass