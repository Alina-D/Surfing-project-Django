from django.conf.urls import url
from django.contrib import admin
from main_app.views import main, product, trainee
from userManagementApp.views import login, logout, registration
from adminApp.views import admin_page, delete_user, get_user_form, create_user, admin_products, admin_products_create, admin_products_delete, admin_products_update, admin_products_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^product/', product, name='product'),
    url(r'^trainee/', trainee, name='trainee'),
]

# userManagementApp"
urlpatterns += [
	url(r'^user/login/$', login, name='login'),
    url(r'^user/logout/$', logout, name='logout'),
    url(r'^user/registration/$', registration, name='registration'),
]

# AdminApp" user
urlpatterns += [    
    url(r'^admin/$', admin_page, name='admin_page'),
	url(r'^admin/delete/user/(\d+)$', delete_user, name='delete_user'),
	url(r'^admin/get_user_form/(\d+)$', get_user_form, name='get_user_form'),
	url(r'^admin/create/user/(\d*)$', create_user, name='create_user'),
]

# AdminApp" products
urlpatterns += [ 
	url(r'^admin/products/', admin_products, name='admin_products'),
	url(r'^admin/create/products$', admin_products_create, name='products_create'),
	url(r'^admin/delete/products/(\d+)$', admin_products_delete, name='products_delete'),
	url(r'^admin/update/products/(\d+)$', admin_products_update, name='products_update'),
	url(r'^admin/detail/products/(\d+)$', admin_products_detail, name='products_detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)