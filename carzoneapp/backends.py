# from account.models import MyUser
# from django.contrib.auth.backends import ModelBackend
# from django.db.models import Q

# class CommonAuthBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):

#         try:
#             user = MyUser.objects.get(username=username)
#         except MyUser.DoesNotExist:
#             user = MyUser(email=username)
#         return user

#     def get_user(self, user_id):
#         try:
#             return MyUser.objects.get(pk=user_id)
#         except MyUser.DoesNotExist:
#             return None

            