from upload import split_csv_measured_values
from upload import split_csv_status_codes

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
    data_lines_per_wtg = split_csv_measured_values.time_period(saved_rows1, turbines_list)

    if saved_rows1[1] == sgre_measured_values:
        split_csv_measured_values.measure_values(saved_rows1, turbines_list, data_lines_per_wtg)
        return True
    elif saved_rows1[1] == sgre_status_code:
        split_csv_status_codes.status_codes(turbines_list, file_path)
        return True
    else:
        return False
