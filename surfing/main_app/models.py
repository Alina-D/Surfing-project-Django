from django.db import models

# Create your models here.

# еденица товара
class Products(models.Model):
	name = models.CharField(verbose_name='название', max_length=32, unique=True)
	category = models.ForeignKey('Category' )
	image = models.ImageField(blank=True, upload_to='image_products')
#	image = models.ImageField(upload_to='image_products', blank=True, verbose_name='картинка')
	rating = models.PositiveIntegerField(verbose_name='рейтинг', default=0)
	description = models.TextField(verbose_name='описание', blank=True)

	def __str__(self):
		return self.name

#Fins
#добавить категорию в продукты


# категория товара
class Category(models.Model):
    name = models.CharField(verbose_name='название', max_length=16, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
		
    def __str__(self):
        return self.name

