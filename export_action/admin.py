import uuid
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _


def export_selected_objects(modeladmin, request, queryset):
    selected = list(queryset.values_list('id', flat=True))
    ct = ContentType.objects.get_for_model(queryset.model)
    url = reverse("export_action:export")

    session_key = "export_action_%s" % uuid.uuid4()
    request.session[session_key] = selected
    return HttpResponseRedirect("%s?ct=%s&session_key=%s" % (url, ct.pk, session_key))


export_selected_objects.short_description = _("Export selected items...")

admin.site.add_action(export_selected_objects)
