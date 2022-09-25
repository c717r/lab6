import sys
 
if __name__ == '__main__':
    students = []
    count = 0
    while True:
        command = input(">>> ").lower()
 
        if command == 'exit':
            break
 
        elif command == 'add':
            name = input("Фамилия и инициалы? ")
            number = input("Номер группы? ")
            z = str(input("Успеваемость? "))
 
            student = {
                'name': name,
                'number': number,
                'z': z,
            }
 
            students.append(student)
            if len(student) > 1:
                students.sort(key=lambda item: item.get('name', ''))
 
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )