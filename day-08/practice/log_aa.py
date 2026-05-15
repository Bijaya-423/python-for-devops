# import pdb
from itertools import count
import json

def read_logs():

    # lines = []
    with open("app.log", 'r') as file:
        # lines.append(file.readlines())
        return file.readlines()
     


def analyzer(lines):
    # pdb.set_trace()
    log_count = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }
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

def write_json(data):
    with open("out.json", "w+") as json_file:
        json.dump(data, json_file)


lines = read_logs()

counts = analyzer(lines)

print(f'"LOG counts are": {counts}')
write_json(counts)