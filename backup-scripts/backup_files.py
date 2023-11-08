from array_files import files
from decouple import config

FROM_DIR = config("GZE_TO_DIR")

TO_DIR = config("GZE_TO_DIR")

for i in files:
    print(i)
    print("scp command")
