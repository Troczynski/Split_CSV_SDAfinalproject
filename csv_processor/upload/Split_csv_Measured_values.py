from datetime import datetime


def TimePeriod(saved_rows, turbines_list):
    str_start_date = str(saved_rows[len(turbines_list) + 3])[13:23]
    str_end_date = str(saved_rows[len(turbines_list) + 3])[26:36]
    start_date = datetime.strptime(str_start_date, "%d/%m/%Y").date()
    end_date = datetime.strptime(str_end_date, "%d/%m/%Y").date()
    timedelta = (end_date - start_date).days
    data_lines_number = 144 + 144 * timedelta

    return data_lines_number


def MeasureValues(saved_rows, turbines_list, number_of_lines):
    #    below 2 variables with blocks of lines - app more efficient
    time_to_units_block = []  # 3rd block of fixed lines with additional data such as time period, creator and units
    for x in saved_rows[len(turbines_list) + 3:len(turbines_list) + 7]:
        time_to_units_block.append(x)
    data_available_wtg_no = []  # block of data availability and turbines list not in order
    for y in saved_rows[len(turbines_list) + 7:len(turbines_list) * 3 + 7]:
        data_available_wtg_no.append(y)

    start_index_data = len(turbines_list) * 3 + 9
    end_index_data = len(
        turbines_list) * 3 + 9 + number_of_lines

    for element in turbines_list:
        name_of_turbine = f'MV_for_{element.replace("/", "_")}.csv'  # create name of the file based on wtg
        nextfile_wtg = open(name_of_turbine, "w+")  # create and open file(singular wtg)
        nextfile_wtg.writelines(saved_rows[0:3])  # save 1st fixed block of text
        nextfile_wtg.writelines(element + '\n')
        nextfile_wtg.writelines(time_to_units_block)
        # for element in  #create loop turbine +data available not the same order as turbineslist
        for wtg in data_available_wtg_no:
            if wtg == f'{element}\n':
                nextfile_wtg.writelines(wtg)
                nextfile_wtg.writelines(data_available_wtg_no[
                                           data_available_wtg_no.index(wtg) + 1
                                           ])
                break
        nextfile_wtg.writelines('\n')
        nextfile_wtg.writelines(saved_rows[len(turbines_list) * 3 + 8])  # timestamp line
        # data copy based on index of lines in saved_rows. Every 24 hours has 144 lines of data (number of lines)

        nextfile_wtg.writelines(saved_rows[start_index_data:end_index_data])
        start_index_data += number_of_lines
        start_index_data += 1  # lineseparator
        end_index_data += number_of_lines
        end_index_data += 1  # line-separator

        nextfile_wtg.close()
