import sys
import datetime

def format_time():
    t = datetime.datetime.now().__format__('%a %A %U %W %w')
    print(t)


if __name__=="__main__":
    format_time()
