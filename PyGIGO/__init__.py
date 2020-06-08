import csv
import os

class CsvHandler:
    def __init__(self, infile, outfile, fields, append=False):
        self._infile = open(infile, "r")
        self.append = append
        self.existed = os.path.isfile(outfile)
        self._outfile = open(outfile, "a" if self.append else "w", newline="")
        self.reader = csv.DictReader(self._infile)
        self.writer = csv.DictWriter(self._outfile, fieldnames=fields)

    def process(self):
        if self.existed and self.append:
            pass
        else:
            self.writer.writeheader()
        for garbageIn in self.reader:
            garbageOut = self.process_line(garbageIn)
            if garbageOut is not None:
                self.writer.writerow(garbageOut)
        self._infile.close()
        self._outfile.close()

    def process_line(self, entry: dict) -> dict:
        out = {}
        for k, v in entry.items():
           out[k] = v
        return out
