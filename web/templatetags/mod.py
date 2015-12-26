from django import template
from django.utils.translation import ugettext_lazy as _, string_concat
from django.utils import timezone
from web.views import findAccount
from django.forms.fields import NullBooleanField, BooleanField, DateTimeField
from dateutil.relativedelta import relativedelta
import random

register = template.Library()

def mod(value, arg):
    if value % arg == 0:
        return True
    else:
        return False

def trans(value):
    return _(value)

def transconcat(value, svalue):
    return string_concat(_(value), _(svalue))

def transconcatspace(value, svalue):
    return string_concat(_(value), ' ', _(svalue))

@register.filter
def is_boolean(field):
    if isinstance(field.field, NullBooleanField):
        return False
    if isinstance(field.field, BooleanField):
        return True
    return False

def isnone(value):
    return value is None

def plusmonths(date, months):
    return date + relativedelta(months=months)

def torfc2822(date):
    return date.strftime("%B %d, %Y %H:%M:%S %z")

def addstr(a, b):
    return unicode(a) + unicode(b)

def findModelId(array, id):
    return next(obj for obj in array if obj.id == id)

positiveAdjectives = [
    _('lovely'),
    _('awesome'),
    _('incredible'),
    _('adorable'),
    _('generous'),
    _('idols-addicted'),
    _('friendly'),
    _('kind'),
    _('warmhearted'),
    _('nice'),
]

@register.simple_tag()
def randomPositiveAdjective():
    return random.choice(positiveAdjectives)

def activity_is_mine(activity, accounts):
    return findAccount(activity.account_id, accounts)

register.filter('mod', mod)
register.filter('trans', trans)
register.filter('transconcat', transconcat)
register.filter('transconcatspace', transconcatspace)
register.filter('plusmonths', plusmonths)
register.filter('isnone', isnone)
register.filter('torfc2822', torfc2822)
register.filter('addstr', addstr)
register.filter('findModelId', findModelId)
register.filter('activity_is_mine', activity_is_mine)
