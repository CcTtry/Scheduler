# author:Ctry
# datetime:2021/3/11 20:22
# software: PyCharm


import sys
import datetime
from classFile import Server
from classFile import VisualMachine
from classFile import RequestItem


# -------------------输入输出--------------------------

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def readData(filename):
    servers = []
    visualMachines = []
    reqItemsDays = []
    reqItems = []  # 一天的请求
    state = 0  # 用于表示当前读取的信息是哪个阶段的
    line_num = 0
    nums = []   # 存储 N、M、T （可以采购的服务器数量、售卖的虚拟机类型数量、T天的数列）
    day_num = 0  # 天数
    f = open(filename)
    for line in f:
        if state == 0:
            if is_number(line):  # 是不是数字，判断是否进行插入操作
                nums.append(int(line))
                line_num += 1
                continue
            else:
                line = line[1:-2].split(', ')
                # print("{}   {}  {} {}".format(line_num-1, line, len(line), type(line)))
                sv = Server(line)
                servers.append(sv)
                # print(servers[-1].memory)
            if(line_num == nums[0]):  # 如果该类型数据读完了，状态转为下一个
                state = 1
                # print("nums 11")

        elif state == 1:
            if is_number(line):  # 是不是数字，判断是否进行插入操作
                nums.append(int(line))
                line_num += 1
                continue
            else:
                line = line[1:-2].split(', ')
                # print("{}   {}  {} {}".format(line_num - 1, line, len(line), type(line)))
                vm = VisualMachine(line)
                visualMachines.append(vm)
            if (line_num == nums[0] + nums[1] + 1):
                state = 2
                # print("\n\n\n")


        elif state == 2:

            if is_number(line) and len(nums) < 3:  # 当前数字表示天数
                nums.append(int(line))
                line_num += 1
                continue
            elif is_number(line):  # 每天有多少行请求
                if(day_num > 0):
                    reqItemsDays.append(reqItems)  # 将前一天的请求入栈
                    reqItems.clear()
                day_num += 1
                continue
            else :
                line = line[1:-2].split(', ')  # 插入请求
                # print("{}   {}  {} {}".format(line_num - 1, line, len(line), type(line)))
                if len(line) == 2:
                    line.insert(1, "NULL")
                reqItem = RequestItem(line)
                reqItems.append(reqItem)
                # print("\n")

        line_num += 1
    reqItemsDays.append(reqItems)
    print(servers[0])
    keyMap = {
        'servers': servers,
        'visualMachines': visualMachines,
        'reqItemsDays': reqItemsDays,

    }
    # print(servers)
    return keyMap



# 添加了排序的处理  修改时间 3/12/10:30
if __name__ == "__main__":
    start = datetime.datetime.now()
    # -------------------输入---------------------------
    data = readData('./trainingFile/training-1.txt')
    end = datetime.datetime.now()
    runtime = end - start
    print(f"运行时长：{runtime}")

    servers = data['servers']
    servers.sort(key=lambda i:(-i.cpuKernel, -i.memory))
    #  排序先按照内核数目排序，核心数目相同的，按照内存大小排序
    for i in range(len(servers)):
        print(" {} ".format(i), end="")
        servers[i].myPrint()





