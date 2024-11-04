import json
import sys

# add specific path to the file name, so that it can be accessed through different folder
def loadTable(path: str):
    with open("./configs/" + path, "r") as file:
        return json.load(file)


sys.modules[__name__] = loadTable