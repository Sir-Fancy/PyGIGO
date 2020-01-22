from PyGIGO import CsvHandler

class Handler(CsvHandler):
    def process_line(self, entry):
        out = {}
        out["num_one"], out["num_two"] = entry["num_one"], entry["num_two"] # define the pass-through columns
        out["sum"] = int(entry["num_one"]) + int(entry["num_two"])          # define the added "sum" column
        return out                                                          # done!

if __name__ == "__main__":
    handler = Handler("ex2_in.csv", "ex2_out.csv", ["num_one", "num_two", "sum"])
    handler.process()
