from django.contrib import admin
from django.db import models

from easy_select2.widgets import Select2

from .models import Person, Competition, Match


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    pass


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.ForeignKey: {'widget': Select2()}
    }

    def get_form(self, request, obj=None, **kwargs):
        form = super(MatchAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['winner'].widget.can_add_related = False
        form.base_fields['winner'].widget.can_change_related = False
        form.base_fields['loser'].widget.can_add_related = False
        form.base_fields['loser'].widget.can_change_related = False
        form.base_fields['competition'].widget.can_add_related = False
        form.base_fields['competition'].widget.can_change_related = False
        return form
