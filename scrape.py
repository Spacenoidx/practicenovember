import pandas as pd

url = "https://www.precisebits.com/reference/relative_hardness_table.htm"

table = pd.read_html(url, match="Janka")
first_table = table[0]

print(table)
print(table[0]["Janka Hardness - lbf"])

print(first_table)
second_table = first_table[["Common name", "Janka Hardness - lbf"]]
print(second_table.to_string())

third_table = second_table.sort_values(by="Janka Hardness - lbf")
fourth_table = third_table.drop(0, axis=0)
print(fourth_table.to_string())