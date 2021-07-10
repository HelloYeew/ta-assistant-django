from ta_assistant_django.wsgi import *
from django.contrib.auth.models import User
from classroom.models import Class


def convert_member(member_str):
    """
    Convert member data from database to member id list

    :param member_str: Data from Class database
    :type member_str: str
    :return: a list of member id as integer
    :rtype: list

    >>> print(convert_member("1,2,50,69"))
    [1, 2, 50, 69]
    """
    if (member_str == "0") or (member_str == ""):
        return []
    else:
        li = list(member_str.split(","))
        li = [int(item) for item in li]
        return li


def get_all_class_member(member_list, check=False):
    """
    Convert member id list to a list of `user` objects

    :param check: If check is true, this function will use to check that all user ID in list is valid in database.
    :param member_list: List of member id (mainly use an output from convert_member function.
    :type member_list: list
    :return: a list of `User` objects
    :rtype: list
    """
    if not check:
        member_object_list = []
        if member_list is not list:
            return member_list
        else:
            for member_id in member_list:
                member_obj = User.objects.get(id=member_id)
                member_object_list.append(member_obj)
            return member_object_list
    else:
        try:
            member_object_list = []
            for member_id in member_list:
                member_obj = User.objects.get(id=member_id)
                member_object_list.append(member_obj)
            return True
        except:
            return False


def convert_id_to_user(user_id):
    """
    Get user id as parameter and convert it to `User` object.

    :param user_id: User ID
    :type user_id: int
    :return: 'User' object
    :rtype: object
    """
    return User.objects.get(id=int(user_id))


def create_member_query(member_list):
    """
    Get member list and convert it to a list of `User` objects.

    :param member_list: List of member id.
    :type member_list: list
    :return: A list of `User` objects.
    :rtype: list
    """
    return [convert_id_to_user(item) for item in member_list]


def convert_to_usable_value(class_detail):
    """
    Convert member list in string from database to a value that can use in member list view

    This function is target to use in member list view in views.py of Class app.

    :param class_detail: Objects of target class data.
    :return: 3 list of `User` objects in class (student in class, ta in class and teacher in class)
    :rtype: list
    """
    student = []
    ta = []
    teacher = []
    if class_detail.student != "0":
        student = create_member_query(get_all_class_member(convert_member(class_detail.student)))
    if class_detail.ta != "0":
        ta = create_member_query(get_all_class_member(convert_member(class_detail.ta)))
    if class_detail.teacher != "0":
        teacher = create_member_query(get_all_class_member(convert_member(class_detail.teacher)))
    return student, ta, teacher


def remove_duplicate(id_list, class_target_id, return_type, check):
    """
    Check duplication in class member and return a new user id list that is not duplicate in class.

    This function mainly use in add_member_to_class function.

    :param id_list: A user id list as a string.
    :type id_list: str
    :param class_target_id: A class id that user want to check a duplicate in that class.
    :type class_target_id: int
    :param return_type: Type of return value (str or list)
    :type return_type: str
    :param check: If check is True, a program will check in entire class member data (include student, ta and teacher
    that is already in class). But if check is False, a program will check duplication only in id_list parameter.
    :type check: bool
    :return: A new user id list that is not duplicate with designated type from return_type value.
    """
    if check:
        new_list = list(set(convert_member(id_list)))
        class_target = Class.objects.get(id=class_target_id)
        student_in_class = convert_member(class_target.student)
        ta_in_class = convert_member(class_target.ta)
        teacher_in_class = convert_member(class_target.teacher)
        for member in new_list:
            if (member in student_in_class) or (member in ta_in_class) or (member in teacher_in_class):
                new_list.remove(member)
    else:
        new_list = list(set(convert_member(id_list)))
    if return_type == "str":
        return_value = ""
        for member in new_list:
            return_value += f"{member},"
        return return_value[:-1]
    elif return_type == "list":
        return new_list


if __name__ == '__main__':
    # print(convert_to_usable_value(Class.objects.get(id=19)))
    # print(create_member_query(get_all_class_member(convert_member(Class.objects.get(id=19).student))))
    # print(get_all_class_member(convert_member("1,21")))
    print(convert_id_to_user(24))
    print(remove_duplicate("1,1,2,3,5,1", "str"))
    # print(convert_member("1,2,50,69"))
