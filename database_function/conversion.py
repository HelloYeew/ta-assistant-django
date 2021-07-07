from ta_assistant_django.wsgi import *
from django.contrib.auth.models import User
from classroom.models import Class


def convert_member(member_str):
    li = list(member_str.split(","))
    li = [int(item) for item in li]
    return li


def get_all_class_member(member_list):
    member_object_list = []
    if member_list is not list:
        return member_list
    else:
        for member_id in member_list:
            member_obj = User.objects.get(id=member_id)
            member_object_list.append(member_obj)
        return member_object_list


def convert_id_to_user(user_id):
    return User.objects.get(id=int(user_id))


def create_member_query(member_list):
    return [convert_id_to_user(item) for item in member_list]


# Convert member list in string from database to a value that can use in member list view
def convert_to_usable_value(class_detail):
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


if __name__ == '__main__':
    print(convert_to_usable_value(Class.objects.get(id=19)))
    print(create_member_query(get_all_class_member(convert_member(Class.objects.get(id=19).student))))
    print(get_all_class_member(convert_member("1,21")))
    print(convert_id_to_user(1))
