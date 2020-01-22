from PyGIGO import CsvHandler

class Handler(CsvHandler):
    def __init__(self, infile, outfile, fields, append=False):
        super().__init__(infile, outfile, fields, append)
        self.num = 1

    def process_line(self, entry):
        self.num += int(entry["sum"])
        out = {}
        out["num_one"], out["num_two"] = entry["num_one"], entry["num_two"]
        out["sum"] = int(entry["num_one"]) + int(entry["num_two"]) * self.num
        return out


if __name__ == "__main__":
    handler = Handler("ex3_in-out.csv", "ex3_in-out.csv", ["num_one", "num_two", "sum"], append=True)
    handler.process()
