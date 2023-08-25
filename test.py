import json
import time
def open_json_file(filename):
    try:
        with open(filename, "r") as f:
            content=f.read()
            if content=="":
                 return json.loads("[]")
            return json.loads(f.read())
    except IOError:
        assert False, "Could not read file {}".format(filename)

def format_json_file(file):
        f=open(file,"r+")
        content=f.read()
        if len(content) == 0 or content[0] == '[':
            print(" {} doesn't need formatting".format(file))
            f.close()
            return
        time.sleep(1)
        print("test")

format_json_file("./out.json")
open_json_file("./out.json")