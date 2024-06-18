import pandas as pd



bare_file = pd.read_csv('All.csv', sep=';',
                        date_format="%d/%m/%y %H:%M:%S.%f",
                        parse_dates=True,
                        keep_default_na=False,
                        names=['date and time [GMT+01:00]', 'Status code number',
                               'Status code name', 'Status code type', 'incoming/phasing out'],
                        header=None,
                        )
print(type(bare_file))
zozo = pd.DataFrame(bare_file)

sample = zozo[["date and time [GMT+01:00]", "Status code number", "Status code name", "Status code type", "incoming/phasing out"]]
sample = zozo[["Status code number", "Status code name", "Status code type", "incoming/phasing out"]]

find_what = "Bukowsko WEC  1/MM92/90920"
find_where = "todo"
sample = zozo.iloc[0:35,0:3]
value = zozo.iloc[0:4, 2:3]

print(value)
print(sample)
# print(find_where)
end_line = "zaz"

sample.to_csv("out1.csv", index=False, mode="w", sep=";", na_rep=None, lineterminator="\n")