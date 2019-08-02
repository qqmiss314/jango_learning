# 导入
from django import template

# 注册到tempate库里面
register = template.Library()

# 注册在第一种方式
@register.filter
def cut0(value, arg):
    return value.replace(arg, '')

# 注册的第二种方式
def lower0(value):
    return value.lower()
register.filter('lower0', lower0)

"""
{{ project_name | lower0 }}
{{ project_name | cut0:"A" }}
"""