"""
案例: 使用yield实现多任务切换
"""


def task1(duration):
    time = 0
    while time <= duration:
        print('task1 turn %d' % time)
        time += 1
        yield None
    raise StopIteration()


def task2(duration):
    time = 0
    while time <= duration:
        print('task2 turn %d' % time)
        time += 1
        yield None
    raise StopIteration()


def main():
    my_task1 = task1(10)
    my_task2 = task2(10)
    task1_finished = False
    task2_finished = False
    while True:
        if not task1_finished:
            try:
                next(my_task1)
            except Exception:
                print("task1 is finished")
                task1_finished = True

        if not task2_finished:
            try:
                next(my_task2)
            except Exception:
                print("task2 is finished")
                task2_finished = True

        if task1_finished and task2_finished:
            break


if __name__ == '__main__':
    main()
