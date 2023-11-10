
# По условию задачи реализованы класс Stack с методом добавления и получения элемента
# и класс TaskManager, основанный на классе Stack, с возможностью создания и удаления задачи.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


class TaskManager:
    def __init__(self):
        self.tasks = Stack()

    def new_task(self, task, priority):
        """Добавление новой задачи.
        Если стек пустой, сразу добавляем в него задачу,
        в случае наличия элементов в стеке при добавлении нового
        реализована проверка на дубли - старая задача удаляется
        и добавляется актуальная новая с возможно другим приоритетом.
        Таким образом можно поменять приоритет у задачи."""

        if self.tasks.is_empty():
            self.tasks.push([task, priority])
        else:
            temp_stack = Stack()

            while not self.tasks.is_empty():
                current_task = self.tasks.pop()
                if current_task[0] != task:
                    temp_stack.push(current_task)

            while not temp_stack.is_empty():
                self.tasks.push(temp_stack.pop())

            self.tasks.push([task, priority])

    def remove_task(self, task):
        """Удаление задачи по названию"""

        temp_stack = Stack()
        while not self.tasks.is_empty():
            current_task = self.tasks.pop()
            if current_task[0] != task:
                temp_stack.push(current_task)
        # Возвращаем задачи обратно в основной стек
        while not temp_stack.is_empty():
            self.tasks.push(temp_stack.pop())

    def __str__(self):
        my_list = []
        result = ""

        while not self.tasks.is_empty():
            my_list.append(self.tasks.pop())

        # Данный цикл необходим, чтобы после принта у нас сохранился наш стек задач
        # reversed() необходимо, чтобы задачи с одним приоритетом не менялись местами при каждом принте
        for y in reversed(range(len(my_list))):
            self.tasks.push(my_list[y])

        # Анонимная функция добавлена для сортировки по приоритету
        my_list.sort(key=lambda x: x[1])

        for y in range(len(my_list) - 1):
            # Данным условием объединяем задачи с одинаковым приоритетом
            # [-1] - последняя позиция, так как приоритет у нас по условию идет после задач
            if my_list[y][-1] == my_list[y + 1][-1]:
                result += str(my_list[y][-1]) + ' ' + my_list[y][0] + '; ' + my_list[y + 1][0] + '\n'
            # Данное условия исключает повторное добавление задач с одинаковым приоритетом
            elif my_list[y][-1] != my_list[y - 1][-1]:
                result += str(my_list[y][1]) + ' ' + my_list[y][0] + '\n'
        return result


if __name__ == '__main__':
    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("поесть", 2)
    manager.new_task("сдать дз", 2)

    print("Выводим отсортированный и объединенный по приоритету список задач без дубликатов:")
    print(manager)

    print('Повторно выводим тот же список задач для демонстрации сохранения этого списка после первого вывода:')
    print(manager)

    manager.remove_task("поесть")
    print('Вывод списка после удаления элемента по названию задачи:')
    print(manager)

