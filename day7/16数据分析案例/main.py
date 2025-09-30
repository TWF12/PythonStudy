from data_define import Record
from file_define import TextFileReader, JsonFileReader

text_file_reader = TextFileReader("data/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("data/2011年2月销售数据JSON.txt")

jan_data = text_file_reader.read_data()
feb_data = json_file_reader.read_data()

all_data = jan_data + feb_data

sales_dict = {}
for record in all_data:
    date = record.date
    money = record.money
    if date not in sales_dict:
        sales_dict[date] = money
    else:
        sales_dict[date] += money

print(sales_dict)


