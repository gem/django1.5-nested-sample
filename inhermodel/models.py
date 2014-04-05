from django.db import models

class TopLevel(models.Model):
    name = models.CharField(max_length=200)

    def clean(self):
        pass
        for name in dir(self.__class__):
            print name, type(getattr(self.__class__, name))
            # print name
        print "CLEAN_FIELDS: ", self.clean_fields()

class LevelOne(models.Model):
    name = models.CharField(max_length=200)
    level = models.OneToOneField('TopLevel', related_name = "level_one")
#    level = models.ForeignKey('TopLevel', related_name = "level_one")

class LevelOneBi(models.Model):
    name_bi = models.CharField(max_length=200)
    level_bi = models.ForeignKey('TopLevel', related_name = "level_one_bi")

class LevelTwo(models.Model):
    name = models.CharField(max_length=200)
    level = models.OneToOneField('LevelOne', related_name = "level_two")

class LevelThree(models.Model):
    name = models.CharField(max_length=200)
    # level = models.ForeignKey('LevelTwo')
    # , primary_key=True
    level = models.OneToOneField(LevelTwo, related_name = "level_three")

