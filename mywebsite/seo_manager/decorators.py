from django.http import request
from seo_manager.models import ActionModel,SEOModel


def register_page(func):
    def echo_func(*func_args, **func_kwargs):
        action,created = ActionModel.objects.get_or_create(action_name = func.__name__)
        return func(*func_args, **func_kwargs)
    return echo_func
    


