from django.shortcuts import render

# Create your views here.
def main(requrest):
	page = 'main'
	title = 'Главная'
	context = {'page': page,
				'title': title
		}
	return render(requrest, 'index.html', context)


def product(requrest):
	page = 'product'
	title = 'Продукция'
	context = {'page': page,
				'title': title
		}
	return render(requrest, 'product.html')


def trainee(requrest):
	page = 'trainee'
	title = 'Обучение'
	context = {'page': page,
				'title': title
		}
	return render(requrest, 'trainee.html')

