from PyGIGO import CsvHandler

# By default, PyGIGO will simply mirror the file if process_line() is not overwritten

if __name__ == "__main__":
    handler = CsvHandler("ex1_in.csv", "ex1_out.csv", ["col_one", "col_two", "extra_three", "extra_four"])
    handler.process()
