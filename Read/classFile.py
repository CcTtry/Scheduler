# author:Ctry
# datetime:2021/3/11 18:08
# software: PyCharm

#  对属性进行了类型的强制转换 修改时间 3/12/10:30
class Server(object):  # 服务器
    def __init__(self, line):  # model_id, cpu_kernel, memory, product_cost, day_cost
        self.modelId = line[0]
        self.cpuKernel = int(line[1])
        self.memory = int(line[2])
        self.productCost = int(line[3])
        self.dayCost = int(line[4])
    def myPrint(self):
        print("{}  {} {} {} {} ".format(self.modelId, self.cpuKernel, self.memory, self.productCost, self.dayCost))

#  对属性进行了类型的强制转换 修改时间 3/12/10:30
class VisualMachine(object):   # 虚拟机
    def __init__(self, line):  # model_id, cpu_kernel, memory, if_double
        self.modelId = line[0]
        self.cpuKernel = int(line[1])
        self.memory = int(line[2])
        self.ifDouble = int(line[3])


class RequestItem(object):  # 请求类 单个条目
    def __init__(self, line):  # 请求条目初始为空 add|del  model  vmId
        self.reqItem = line[0]
        self.model =  line[1]
        self.vmId =  line[2]


class RequestItemDay(object):  # 请求类
    def __init__(self):  # 请求条目初始为空 add|del  model  vmId
        self.items = []
    def insert(self, reqItem):
        self.items.append(reqItem)





# before = {
# "key1": 5,
# "key2": 6,
# "key3": 4,
# "key4": 3,
# }

# 排序

# after = dict(sorted(before.items(), key=lambda e: e[1]))
#
# print(after)