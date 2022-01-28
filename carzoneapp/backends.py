# from django.conf import settings
# from account.models import MyUser
# from django.contrib.auth.backends import ModelBackend
# from django.db.models import Q
# from django.contrib.auth.backends import BaseBackend

# class CommonAuthBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):

#         try:
#             user = MyUser.objects.get(username=username)
#         except MyUser.DoesNotExist:
#             user = MyUser(email=username)
#         return user

#     def get_user(self, user_id):
#         try:
#             user = MyUser.objects.get(pk=user_id)
#             return user
#         except MyUser.DoesNotExist:
#             return None

            