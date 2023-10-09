from django import template
from home.models import FileInfo

register = template.Library()

@register.filter
def info_value(path):
    file_info = FileInfo.objects.filter(path=path)
    if file_info.exists():
        return file_info.first().info
    else:
        return ""
