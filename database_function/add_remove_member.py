from ta_assistant_django.wsgi import *
from django.contrib.auth.models import User
from classroom.models import Class
from database_function.conversion import convert_member, get_all_class_member, remove_duplicate


def add_student_to_class(id_to_add, class_id):
    """
    Get a list of user id to add as student in a class target and return a status.

    :param id_to_add: A string from add_student form.
    :type id_to_add: str
    :param class_id: Class ID that user want to add student there.
    :type class_id: int
    :return: Status on adding student. (True = success, False = failed)
    """
    target_class = Class.objects.get(id=class_id)
    if target_class.student == "0":
        target_class.student = id_to_add
        target_class.save()
        return True
    else:
        clean_list = remove_duplicate(f"{target_class.student},{id_to_add}", "str")
        checked_user = get_all_class_member(convert_member(clean_list), check=True)
        if checked_user:
            target_class.student = clean_list
            target_class.save()
            return True
        else:
            return False


def add_member_to_class(id_to_add, class_id, target_group):
    """
    Get a list of user id to add as student in a class target and return a status.

    :param target_group: Target of group that user want to add member. (student, ta or teacher)
    :type target_group: str
    :param id_to_add: A string from add_student, add_ta or add_teacher form.
    :type id_to_add: str
    :param class_id: Class ID that user want to add student there.
    :type class_id: int
    :return: Status on adding student. (True = success, False = failed)
    """
    target_class = Class.objects.get(id=class_id)
    in_database = ""
    if target_group == "student":
        in_database = target_class.student
    elif target_group == "ta":
        in_database = target_class.ta
    elif target_group == "teacher":
        in_database = target_class.teacher
    if in_database == "0":
        clean_list = remove_duplicate(id_to_add, class_id, "str", False)
        checked_user = get_all_class_member(convert_member(clean_list), check=True)
        if checked_user:
            if target_group == "student":
                target_class.student = clean_list
            elif target_group == "ta":
                target_class.ta = clean_list
            elif target_group == "teacher":
                target_class.teacher = clean_list
            target_class.save()
            return True
        else:
            return False
    else:
        clean_list = remove_duplicate(id_to_add, class_id, "str", True)
        checked_user = get_all_class_member(convert_member(clean_list), check=True)
        if checked_user and (clean_list != ""):
            if target_group == "student":
                target_class.student = f"{target_class.student},{clean_list}"
            elif target_group == "ta":
                target_class.ta = f"{target_class.ta},{clean_list}"
            elif target_group == "teacher":
                target_class.teacher = f"{target_class.teacher},{clean_list}"
            target_class.save()
            return True
        elif checked_user and (clean_list == ""):
            return True
        else:
            return False
