from django.db import models


class FizProperties(models.Model):
    title = models.IntegerField('title', max_length=50)
    field1 = models.CharField('Молекулярная масса', max_length=50)
    field2 = models.CharField('Норм. темп. плавления (К)', max_length=50)
    field3 = models.CharField('Норм. темп. кипения (К)', max_length=50)
    field4 = models.CharField('Критическая темп (К)', max_length=50)
    field5 = models.CharField('Критическое давление (Па)', max_length=50)
    field6 = models.CharField('Критический обьем (M^3/Кмоль)', max_length=50)
    field7 = models.CharField('Крит к-ент сжимаемости', max_length=50)
    field8 = models.CharField('Фактор ацентричн. Питцера', max_length=50)
    field9 = models.CharField('Плотность жидк. при опорн. темп. (Кг/М^3)', max_length=50)
    field10 = models.CharField('Опорная температура (К)', max_length=50)
    field11 = models.CharField('Дипольный момент (Н*М^4)^0.5', max_length=50)
    field12 = models.CharField('Стан. тепл. образ. при 298К (Дж/Кмоль)', max_length=50)
    field13 = models.CharField('Тепл. парообр. при Т кип.нор. (Дж/Кмоль)', max_length=50)
    field14 = models.CharField('Изобарн. потенц. (при н.у.) (Дж/Кмоль)', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "физ хар-ка"
        verbose_name_plural = "физ хар-ки"
