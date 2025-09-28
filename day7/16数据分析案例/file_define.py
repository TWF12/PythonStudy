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
            record_list = line.split(",")
            record = Record(record[0], record[1], record[2], record[3])
            records.append(record)
            f.close()
        return records


if __name__ == '__main__':
    text_file_reader = TextFileReader("data/2011年1月销售数据.txt")
    data = text_file_reader.read_data()