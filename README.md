# PyGIGO - Garbage In, Garbage Out
_______

## Intro
This project was designed to fit a necessity for easy CSV processing without having to whip up the same code every time.
At its core, it's a wrapper for Python's `csv` library. Only tested on Python 3.

## Usage
Simply override the process_line function. That's it. That function is run for each line in your input file, so when you
have the `out` dictionary ready, just return that! Easy peasy. Check the example#.py files for usage examples or read
below:

_(note: tables have been stylized and do not output this way)_
_______

## Examples
### example1.py

    from PyGIGO import CsvHandler
    
    # By default, PyGIGO will simply mirror the file if process_line() is not overwritten
    
    if __name__ == "__main__":
        handler = CsvHandler("ex1_in.csv", "ex1_out.csv", ["col_one", "col_two", "extra_three", "extra_four"])
        handler.process()

    #   In:                                            
    #   +-----------------+-------------------+        
    #   |     COL_ONE     |      COL_TWO      |        
    #   +-----------------+-------------------+        
    #   | mirror this!    | mirror this too!  |        
    #   | how about this? | can do!           |        
    #   | yay how fun!    | are we there yet? |        
    #   +-----------------+-------------------+        
    #   
    #   Out:
    #   +-----------------+-------------------+-------------+------------+
    #   |     COL_ONE     |      COL_TWO      | EXTRA_THREE | EXTRA_FOUR |
    #   +-----------------+-------------------+-------------+------------+
    #   | mirror this!    | mirror this too!  |             |            |
    #   | how about this? | can do!           |             |            |
    #   | yay how fun!    | are we there yet? |             |            |
    #   +-----------------+-------------------+-------------+------------+
    
### example2.py

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
    
    #   In:
    #   +---------+---------+
    #   | NUM_ONE | NUM_TWO |
    #   +---------+---------+
    #   | 1       | 4       |
    #   | 2       | 7       |
    #   | 5       | 8       |
    #   +---------+---------+
    #   
    #   Out:
    #   +---------+---------+-----+
    #   | NUM_ONE | NUM_TWO | SUM |
    #   +---------+---------+-----+
    #   | 1       | 4       | 5   |
    #   | 2       | 7       | 9   |
    #   | 5       | 8       | 13  |
    #   +---------+---------+-----+

## example3.py
There's an append mode too, in case you need to iterate multiple times for whatever reason and have the outfile longer
than the input. Maybe for statistics or science stuff, I dunno. The following example uses the input and output file as
the same file, and adds an extra instance variable.

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
    
    
    #   In:    
    #   +---------+---------+-----+
    #   | NUM_ONE | NUM_TWO | SUM |
    #   +---------+---------+-----+
    #   | 2       | 3       | 5   |
    #   +---------+---------+-----+
    #   
    #   Out, after three executions:
    #   +---------+---------+-----+
    #   | NUM_ONE | NUM_TWO | SUM |
    #   +---------+---------+-----+
    #   | 2       | 3       | 5   |
    #   | 2       | 3       | 20  |
    #   | 2       | 3       | 20  |
    #   | 2       | 3       | 80  |
    #   | 2       | 3       | 20  |
    #   | 2       | 3       | 80  |
    #   | 2       | 3       | 140 |
    #   | 2       | 3       | 380 |
    #   +---------+---------+-----+