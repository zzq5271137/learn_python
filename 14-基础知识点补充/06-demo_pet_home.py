"""
案例: 宠物寄养系统(面向对象)
"""


class Pet(object):
    """
    宠物类
    """

    def __init__(self, pet_id, pet_name, pet_type, pet_price):
        self.pet_id = pet_id
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.pet_price = pet_price

    def __str__(self):
        return '宠物id: {}, 宠物名字: {}, 宠物类型: {}, 宠物价格: ${}'.format(self.pet_id, self.pet_name,
                                                                self.pet_type, self.pet_price)

    def get_line(self):
        return "[{pet_id},{pet_name},{pet_type},{pet_price}]\n".format(pet_id=self.pet_id,
                                                                       pet_name=self.pet_name,
                                                                       pet_type=self.pet_type,
                                                                       pet_price=self.pet_price)

    @classmethod
    def get_pet_from_line(cls, line):
        pet_id, pet_name, pet_type, pet_price = line.replace('\n', '').replace('[', '') \
            .replace(']', '').split(',')  # 列表的解组操作
        return Pet(pet_id, pet_name, pet_type, pet_price)


class PetManager(object):
    """
    宠物管理类, 单例
    """

    __instance = None
    __pet_file = 'pet_book.txt'

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def add_pet(self, pet_id, pet_name, pet_type, pet_price):
        pet = Pet(pet_id, pet_name, pet_type, pet_price)
        with open(PetManager.__pet_file, 'a') as fp:
            fp.write(pet.get_line())

    def list_all_pets(self):
        pet_list = []
        with open(PetManager.__pet_file, 'r') as fp:
            for line in fp:
                pet_list.append(Pet.get_pet_from_line(line))
        return pet_list

    def search_pet_by_name(self, pet_name):
        with open(PetManager.__pet_file, 'r') as fp:
            for line in fp:
                pet = Pet.get_pet_from_line(line)
                if pet_name.upper() == pet.pet_name.upper():
                    return pet
        return None


class Application(object):
    """
    程序运行流程控制类, 单例
    """

    __instance = None
    __pet_manager = PetManager()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def run(self):
        print('欢迎来到宠物寄养系统')
        while True:
            print('0.退出程序')
            print('1.添加新宠物')
            print('2.显示所有宠物')
            print('3.查找宠物')
            option = input('请输入操作序号: ')
            if option == '0':
                break
            elif option == '1':
                self.__input_pet_info()
            elif option == '2':
                self.__list_all_pets()
            elif option == '3':
                self.__search_pet_by_name()
            else:
                print('操作序号输入有误, 请重新输入')

    def __input_pet_info(self):
        pet_id = input('请输入宠物id: ')
        pet_name = input('请输入宠物名字: ')
        pet_type = input('请输入宠物类型: ')
        pet_price = input('请输入宠物价格: ')
        Application.__pet_manager.add_pet(pet_id, pet_name, pet_type, pet_price)
        print('宠物信息录入成功！')

    def __list_all_pets(self):
        try:
            pet_list = Application.__pet_manager.list_all_pets()
            for i in range(0, len(pet_list)):
                print('%d---%s' % (i, pet_list[i]))
        except FileNotFoundError:
            print('未有宠物数据, 请先添加！')

    def __search_pet_by_name(self):
        try:
            pet_name = input('请输入要查找的宠物名字: ')
            pet = Application.__pet_manager.search_pet_by_name(pet_name)
            if not pet:
                print('未找到该宠物！')
            else:
                print(pet)
        except FileNotFoundError:
            print('未有宠物数据, 请先添加！')


def main():
    app = Application()
    app.run()


if __name__ == '__main__':
    main()
