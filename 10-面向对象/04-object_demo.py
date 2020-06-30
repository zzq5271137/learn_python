"""
案例: 组装电脑
"""


class CPU(object):
    def __init__(self, brand, core, interface):
        self.brand = brand
        self.core = core
        self.interface = interface

    def __str__(self):
        return "({},{}核)".format(self.brand, self.core)


class RAM(object):
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def __str__(self):
        return "({},{})".format(self.brand, self.size)


class Disk(object):
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def __str__(self):
        return "({},{})".format(self.brand, self.size)


class Computer(object):
    def __init__(self, cpu_interface, ram_num, disk_num):
        self.cpu_interface = cpu_interface
        self.ram_num = ram_num
        self.disk_num = disk_num
        self.__cpu = None
        self.__rams = []
        self.__disks = []

    def add_cpu(self, cpu):
        if self.cpu_interface == cpu.interface:
            self.__cpu = cpu
        else:
            print("cpu接口型号不对, 不能安装...")

    def add_ram(self, ram):
        if len(self.__rams) == self.ram_num:
            print("内存条已插满, 无法再安装...")
        else:
            self.__rams.append(ram)

    def add_disk(self, disk):
        if len(self.__disks) == self.disk_num:
            print("硬盘已插满, 无法再安装...")
        else:
            self.__disks.append(disk)

    def run(self):
        if not self.__cpu:
            print("没有cpu, 无法运行...")
            return
        elif len(self.__rams) == 0 or len(self.__rams) > self.ram_num:
            print("内存条安装失败, 无法运行...")
            return
        elif len(self.__disks) == 0 or len(self.__disks) > self.disk_num:
            print("硬盘安装失败, 无法运行...")
            return
        else:
            print("电脑正在运行, 参数: cpu={}".format(self.__cpu))
            print("内存信息: ")
            for ram in self.__rams:
                print(ram)
            print("硬盘信息: ")
            for disk in self.__disks:
                print(disk)


def main():
    computer = Computer(cpu_interface='1234', ram_num=2, disk_num=4)
    cpu = CPU(brand='AMD', core=8, interface='1234')
    ram1 = RAM(brand='玩家国度', size='16g')
    ram2 = RAM(brand='金士顿', size='32g')
    disk1 = Disk(brand='金士顿固态', size='1T')
    disk2 = Disk(brand='西部数据黑盘', size='2T')
    computer.add_cpu(cpu)
    computer.add_ram(ram1)
    computer.add_ram(ram2)
    computer.add_disk(disk1)
    computer.add_disk(disk2)
    computer.run()


if __name__ == '__main__':
    main()
