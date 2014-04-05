from django.contrib import admin
from nested_inlines.admin import NestedStackedInline, NestedModelAdmin
from inhermodel.models import *

class LevelThreeInline(NestedStackedInline):
    model = LevelThree
    max_num = 1
    extra = 1
    fk_name = 'level'


class LevelTwoInline(NestedStackedInline):
    model = LevelTwo
    max_num = 1
    extra = 1
    fk_name = 'level'
    inlines = [LevelThreeInline]


class LevelOneInline(NestedStackedInline):
    model = LevelOne
    max_num = 1
    extra = 1
    fk_name = 'level'
    inlines = [LevelTwoInline]

class LevelOneBiInline(NestedStackedInline):
    model = LevelOneBi
    max_num = 1
    extra = 1
    fk_name = 'level_bi'


class TopLevelAdmin(NestedModelAdmin):
    model = TopLevel
    inlines = [LevelOneInline, LevelOneBiInline]

    def cross_validate(self, form, formsets):
	print "Cross_validate is here"
        # print dir(formsets)
        # print len(formsets)
	return True


admin.site.register(TopLevel, TopLevelAdmin)
