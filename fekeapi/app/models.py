from django.db import models

# Create your models here.
class TodosTitle(models.Model):
    my_list = models.TextField()

    def set_my_list(self,value):        # сохранить в переменную данные через '-'
        self.my_list = '-'.join(value)

    def get_my_list(self):
        return self.my_list.split('-') # вернуть список с данными
    
    def __str__(self):
        return str(self.pk)