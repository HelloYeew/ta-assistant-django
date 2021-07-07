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


if __name__ == '__main__':
    print(get_all_class_member(convert_member(Class.objects.get(id=19).student)))
    print(get_all_class_member(convert_member("1,21")))
