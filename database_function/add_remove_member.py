from ta_assistant_django.wsgi import *
from django.contrib.auth.models import User
from classroom.models import Class
from database_function.conversion import convert_member, get_all_class_member, remove_duplicate


def add_student_to_db(id_to_add, class_id):
    """
    Get a lit of user id to add as student in a class target and return a status.

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

# TODO: Implement this function to TA and teacher (Duplication must check on all TA and teacher too.)
