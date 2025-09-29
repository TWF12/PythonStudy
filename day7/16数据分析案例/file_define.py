import json

from data_define import Record


class FileReader:
    def read_data(self) -> list[Record]:
        pass


class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding='utf-8')
        records = []
        for line in f:
            record_list = line.strip().split(',')
            record = Record(record_list[0], record_list[1], record_list[2], record_list[3])
            records.append(record)
        f.close()
        return records

class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding='utf-8')
        records = []
        for line in f:
            record_dict = json.loads(line)
            record = Record(record_dict["date"], record_dict["order_id"], record_dict["money"], record_dict["province"])
            records.append(record)
        f.close()
        return records

if __name__ == '__main__':
    text_file_reader = TextFileReader("data/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("data/2011年2月销售数据JSON.txt")
    data_txt = text_file_reader.read_data()
    data_json = json_file_reader.read_data()
    for line in data_txt:
        print(line)
print("-----------------------------------------------------------------------------------")
for line in data_json:
    print(line)