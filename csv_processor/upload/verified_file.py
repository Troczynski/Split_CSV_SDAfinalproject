
import os
import sys


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import Split_csv_Measured_values
import Split_csv_Status_Codes

sgre_measured_values = '10 Minute Values, detailed\n'
sgre_status_code = 'Status code list\n'

def verify_file(file_path):
    with open(file_path, 'r') as dir_big_file:
        saved_rows1 = []
        for row in dir_big_file:
            saved_rows1.append(row)

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

    if saved_rows1[1] == sgre_measured_values:
        Split_csv_Measured_values.MeasureValues(saved_rows1, turbines_list, data_lines_per_WTG)
        return True
    elif saved_rows1[1] == sgre_status_code:
        Split_csv_Status_Codes.StatusCodesAll(turbines_list, file_path)
        return True
    else:
        return False
