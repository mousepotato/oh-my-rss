
from django import template
from django.utils.timezone import localtime
from django.conf import settings

register = template.Library()


@register.filter
def to_stars(num):
    """
    转换成星星评级（1，2，3）
    :param num:
    :return:
    """
    return '★' * int(num / 10)


@register.filter
def to_date_fmt(dt):
    """
    转换成 "YYYY-MM-DD hh:mm:ss" 格式的时间
    :param dt:
    :return:
    """
    dt = localtime(dt)
    return dt.strftime("%Y-%m-%d %H:%M:%S")


@register.filter
def to_view_uv(uv_dict, uindex):
    """
    转换成UV数据
    :param uv_dict:
    :param uindex:
    :return:
    """
    uv = uv_dict.get(settings.REDIS_VIEW_KEY % uindex)
    if uv is not None:
        return uv
    return 0


@register.filter
def to_like_uv(uv_dict, uindex):
    uv = uv_dict.get(settings.REDIS_LIKE_KEY % uindex)
    if uv is not None:
        return uv
    return 0


@register.filter
def to_open_uv(uv_dict, uindex):
    uv = uv_dict.get(settings.REDIS_OPEN_KEY % uindex)
    if uv is not None:
        return uv
    return 0