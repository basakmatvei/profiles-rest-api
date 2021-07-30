from django.db import models


class DirectoryManager(models.Manager):
    def create_directory(self,name,short_name,description,version,start_date, password=None):
        if not name:
            raise ValueError('Directory must have a name')

        directory = self.model(name = name, short_name= short_name, description = description,
        version=version, start_date = start_date)
        directory.save(using=self.db)

        return directory


class Directory(models.Model):
    #Сущность "Справочник"
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    version = models.CharField(max_length=255)
    start_date =  models.DateField(auto_now_add=False)

    objects = DirectoryManager()

def get_name(self):
    return self.name

class DirectoryItem(models.Model):
    #Сущность "Элемент справочника"
    id = models.AutoField(primary_key=True)
    parent_id = models.ForeignKey(Directory, on_delete = models.CASCADE)
    element_code = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
