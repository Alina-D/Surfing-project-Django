from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from userManagementApp.forms import MyRegistrationForm, UserChangeForm
from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test
from main_app.forms import ProductsForm
from main_app.models import Products, Category


# AdminApp" user
@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    users = User.objects.all()
    #user_form = MyRegistrationForm()
    user_form = UserChangeForm()
    return render(request, 'admin/admin_page.html', {'users': users, 'form': user_form})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/admin')


def get_user_form(request, user_id):
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        user_form = UserChangeForm(instance=user)
        context = {'form': user_form, 'id': user_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc_universal_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404


def create_user(request, user_id=None):
    if request.is_ajax():
        print('user_id = ', user_id)
        if not user_id:
            print('Not user_id')
            user = User(request.POST)
            #user_form = MyRegistrationForm(request.POST)
        else:
            user = get_object_or_404(User, id=user_id)
            user_form = UserChangeForm(request.POST or None, instance=user)
            print('Edited' + str(user_id))
        if user_form.is_valid():
            user_form.save()
            users = User.objects.all()
            html = loader.render_to_string('inc-users_list.html', {'users': users}, request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = user_form.errors.as_json()
            return JsonResponse({'errors': errors})
    raise Http404

#
#def delete_user_form(request, user_id):
#	if request.is_ajax():
#		user = get_object_or_404(User, id=user_id)
#		user.delete()
#		users = User.objects.all()
#		context = {'users': users}
#		html = loader.render_to_string('inc-users_list.html', context, request=request)
#		data = {'errors': False, 'html': html}
#		return JsonResponse(data)
#	raise Http404


# AdminApp" products
def admin_products(request):
	products = Products.objects.all()
	return render(request, 'admin/admin_products.html', {'products': products})



def admin_products_create(request):
	if request.method == 'POST':
		form = ProductsForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/admin/products/')
		context = {'form': form}
		return render(request, 'admin/admin_products_create.html', context)
	context = {'form': ProductsForm()}
	return render(request, 'admin/admin_products_create.html', context)


def admin_products_delete(request, id):
	product = get_object_or_404(Products, id=id)
	product.delete()
	return HttpResponseRedirect('/admin/products')


def admin_products_update(request, id):
	product = get_object_or_404(Products, id=id)
	if request.method == 'POST':
		form = ProductsForm(request.POST, request.FILES, instance=product)
		if form.is_valid():
			product.save()
			return HttpResponseRedirect('/admin/products/')
		context = {'form': form}
		return render(request, 'admin/admin_products_update.html' ,context)
	context = {'form': ProductsForm(instance=product)}
	return render(request, 'admin/admin_products_update.html' ,context)


def admin_products_detail(request,id):
	products = get_object_or_404(Products, id=id)
	return render(request, 'admin/admin_products_detail.html', {'product': products})
		