import os

from config import BASE_PATH


# 清空report目录
# report_path = BASE_PATH + os.sep + "report" + os.sep
def clear_report(path=BASE_PATH + os.sep + "report" + os.sep):
    i = input("clear report (Y/N)? ")
    if i == "Y" or i == "y":
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            if os.path.isdir(c_path):
                clear_report(c_path)
            else:
                os.remove(c_path)
        print("report cleared")
    else:
        exit()


clear_report()



