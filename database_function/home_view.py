from ta_assistant_django.wsgi import *
from classroom.models import Class
from database_function.conversion import convert_member, get_all_class_member


def get_available_class_student(user_id):
    available_class_student = []
    for class_obj in Class.objects.all():
        if int(user_id) in get_all_class_member(convert_member(class_obj.student)):
            available_class_student.append(class_obj)
    return available_class_student


def get_available_class_ta(user_id):
    available_class_ta = []
    for class_obj in Class.objects.all():
        if int(user_id) in get_all_class_member(convert_member(class_obj.ta)):
            available_class_ta.append(class_obj)
    return available_class_ta


def get_available_class_teacher(user_id):
    available_class_teacher = []
    for class_obj in Class.objects.all():
        if int(user_id) in get_all_class_member(convert_member(class_obj.teacher)):
            available_class_teacher.append(class_obj)
    return available_class_teacher


def check_status(user_id):
    # 1 = Only student (Member on class as student, no as TA or teacher)
    # 2 = No class (Not member in any class in entire database)
    if (get_available_class_teacher(user_id) == []) and (get_available_class_ta(user_id) == []) and (get_available_class_student(user_id) != []):
        return 1
    elif (get_available_class_teacher(user_id) == []) and (get_available_class_ta(user_id) == []) and (get_available_class_student(user_id) == []):
        return 2
    else:
        return False


if __name__ == '__main__':
    print(get_available_class_student(22))
    print(get_available_class_ta(22))
    print(get_available_class_teacher(22))
    print(check_status(22))
