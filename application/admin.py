from django.contrib import admin
from django.apps import apps


# Register models for applications
app_models = apps.get_app_config("application").get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

acct_models = apps.get_app_config("account").get_models()
for model in acct_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

chat_models = apps.get_app_config("chat").get_models()
for model in chat_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass


# to get models for all applications, use below
# all_models = apps.get_models()
#
# for model in all_models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass
