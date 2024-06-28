"""code maybe working but is very ugly make class and
functions with 2 params input file and amount of turbines /split sections
 and third params measured values or status code

"""
import csv
from os import getcwd


class Split:
    def __int__(self, dir_file: int, no_of_WTGs: int, type_of_data):
        dir_file = self.dir_file

        pass

    def open_big_file(self, dir_file, no_of_WTGs: int, type_of_data):

        pass

    def split_sections_sc(self, ):
        pass

    def split_sections_mv(self, ):
        pass


dir_big_file = input("big file directory")

csvfile = open(dir_big_file, "r", newline="\r\n")
bigfile = csv.reader(csvfile, delimiter=';', quotechar='|')

saved_rows = []

for row in bigfile:
    saved_rows.append(row)

end = int(input("number of turbines/ section to split: ")) + 3

start_Status_codes_for = []

turbines_list = []
for row in saved_rows[3:end]:
    start = [f'Status codes for  {str(row)[2:-2]}']
    start1 = [f'{str(row)[2:-2]}']
    start_Status_codes_for.append(start)
    turbines_list.append(start1)

start_s = saved_rows.index(start_Status_codes_for[0])
end_s = saved_rows.index(start_Status_codes_for[1])
i = 0

for element in turbines_list: #while i <= len(start_Status_codes_for):
    start_s = saved_rows.index(start_Status_codes_for[i])
    try:
        end_s = saved_rows.index(start_Status_codes_for[i + 1])
    except IndexError:
        end_s = len(saved_rows)
    nameOfTurbine = f'sc_WTG{i+1}.csv'
    new1 = open(nameOfTurbine, "w+", newline="\n")
    new = csv.writer(new1, delimiter=";")
    new.writerows(saved_rows[0:3])
    new.writerows(saved_rows[i + 3:i + 4])
    new.writerows(saved_rows[end:end + 2])
    # new.writerows(saved_rows[saved_rows.index(turbines_list[i])])
    new.writerows(saved_rows[start_s:end_s])
    new1.close()
    i += 1

csvfile.close()
