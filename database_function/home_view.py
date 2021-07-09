from ta_assistant_django.wsgi import *
from classroom.models import Class
from database_function.conversion import convert_member, get_all_class_member

"""
This file contain a function that is mainly to create a view in homepage of each user.
"""


def get_available_class_student(user_id):
    """
    Get user ID of target users and return a list of `Class` objects that user is a member as a student.
    :param user_id: User id of target user.
    :type user_id: int
    :return: A list of `Class` object that target user is a member as a student.
    :rtype: list
    """
    available_class_student = []
    for class_obj in Class.objects.all():
        if int(user_id) in get_all_class_member(convert_member(class_obj.student)):
            available_class_student.append(class_obj)
    return available_class_student


def get_available_class_ta(user_id):
    """
    Get user ID of target users and return a list of `Class` objects that user is a member as a TA.
    :param user_id: User id of target user.
    :type user_id: int
    :return: A list of `Class` object that target user is a member as a TA.
    :rtype: list
    """
    available_class_ta = []
    for class_obj in Class.objects.all():
        if int(user_id) in get_all_class_member(convert_member(class_obj.ta)):
            available_class_ta.append(class_obj)
    return available_class_ta


def get_available_class_teacher(user_id):
    """
    Get user ID of target users and return a list of `Class` objects that user is a member as a teacher.
    :param user_id: User id of target user.
    :type user_id: int
    :return: A list of `Class` object that target user is a member as a teacher.
    :rtype: list
    """
    available_class_teacher = []
    for class_obj in Class.objects.all():
        if int(user_id) in get_all_class_member(convert_member(class_obj.teacher)):
            available_class_teacher.append(class_obj)
    return available_class_teacher


def check_status(user_id):
    """
    Get user ID of target users and return a status that is necessary in template condition of homepage views.

    Return value :

    - 1 = Only student (Only a member in entire class database as student, not as TA or teacher)

    - 2 = No class (Not member in any class in entire Class database)

    :param user_id: User id of target user.
    :type user_id: int
    """
    if (get_available_class_teacher(user_id) == []) and (get_available_class_ta(user_id) == []) and\
            (get_available_class_student(user_id) != []):
        return 1
    elif (get_available_class_teacher(user_id) == []) and (get_available_class_ta(user_id) == []) and\
            (get_available_class_student(user_id) == []):
        return 2
    else:
        return False


if __name__ == '__main__':
    print(get_available_class_student(22))
    print(get_available_class_ta(22))
    print(get_available_class_teacher(22))
    print(check_status(22))
