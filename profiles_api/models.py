from django.db import models


class DirectoryManager(models.Manager):
    def create_directory(self, name, short_name, description, version, start_date, password=None):
        if not name:
            raise ValueError('Directory must have a name')

        directory = self.model(name=name, short_name=short_name, description=description,
                               version=version, start_date=start_date)
        directory.save(using=self.db)

        return directory


class DirectoryItemManager(models.Manager):
    def create_directory(self, parent, element_code, value):
        if not value:
            raise ValueError('Directory Item must have a value')

        directory_item = self.model(parent=parent, element_code=element_code, value=value)
        directory_item.save(using=self.db)

        return directory_item


class Directory(models.Model):
    # Сущность "Справочник"
    ident = models.CharField('Идентификатор справочника', unique=True, max_length=255)
    name = models.CharField('Наименование', max_length=255)
    short_name = models.CharField('Короткое наименование', max_length=255)
    description = models.TextField('Описание', max_length=255)
    version = models.CharField('Версия', max_length=255, blank=False)
    start_date = models.DateField('Дата начала действия справочника этой версии', auto_now_add=False)
    end_date = models.DateField('Дата окончания действия справочника этой версии', auto_now_add=False)

    objects = DirectoryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Справочник"
        verbose_name_plural = "Справочники"


class DirectoryItem(models.Model):
    # Сущность "Элемент справочника"
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(Directory, on_delete=models.CASCADE)
    element_code = models.CharField('Код элемента', max_length=255, blank=False)
    value = models.CharField('Значение элемента', max_length=255, blank=False)

    objects = DirectoryItemManager()

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Элемент"
        verbose_name_plural = "Элементы"
