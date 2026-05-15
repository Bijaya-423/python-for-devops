# import pdb
from itertools import count
import json

class LogAnalyzer:

    def __init__(self, file_name, output_file):
        self.file_name = file_name
        self.output_file = output_file

    
    def read_logs(self):
        # lines = []
        with open(self.file_name, 'r') as file:
            # lines.append(file.readlines())
            return file.readlines()
        


    def analyzer(self):
        # pdb.set_trace()
        log_count = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0
        }

        lines = self.read_logs()

        for line in lines:
            if "INFO" in line:
                log_count.update({"INFO": log_count["INFO"] + 1})
            elif "WARNING" in line:
                log_count.update({"WARNING": log_count["WARNING"] + 1})
            elif "ERROR" in line:
                log_count.update({"ERROR": log_count["ERROR"] + 1})
            else:
                # continue
                pass

        return log_count

    def write_json(self, data):
        with open(self.output_file, "w+") as json_file:
            json.dump(data, json_file)


# lines = read_logs()
# counts = analyzer(lines)
# print(f'"LOG counts are": {counts}')
# write_json(counts)

log_obj = LogAnalyzer("app2.log", "out_analyzer2.json")
# log_obj = LogAnalyzer("app_analyzer.log", "out_analyzer.json")

log_count = log_obj.analyzer()
log_obj.write_json(log_count)