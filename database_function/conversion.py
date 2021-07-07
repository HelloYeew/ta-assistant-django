from ta_assistant_django.wsgi import *
from django.contrib.auth.models import User

def convert_member(member_str):
    li = list(member_str.split(","))
    li = [int(item) for item in li]
    return li

def get_all_class_member(member_list):
    member_object_list = []
    for member_id in member_list:
        member_obj = User.objects.get(id=member_id)
        member_object_list.append(member_obj)
    return member_object_list

if __name__ == '__main__':
    print(get_all_class_member(convert_member("1,21")))