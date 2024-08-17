from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from owner import views as owner
from user import views as user

urlpatterns = [
    # Administrator
    path('admin/', admin.site.urls),
    path('owner/', owner.index, name='owner_index'),
    path('owner/register/', owner.register, name='owner_register'),
    path('owner/login/', owner.login, name='owner_login'),
    path('owner/logout/', owner.logout, name='owner_logout'),
    path('owner/profile/', owner.profile, name='owner_profile'),
    path('owner/profilephoto/', owner.ProfilePhoto, name='owner_profilephoto'),
    path('owner/addpg/', owner.addpg, name='owner_addpg'),
    path('owner/delete/<int:id>/', owner.deletepg, name='owner_deletepg'),
    path('owner/update/<int:id>/', owner.updatepg, name='owner_updatepg'),
    path('owner/pgs/', owner.pglist, name='owner_pglist'),
    path('owner/notifications/', owner.Notifications, name='owner_notifications'),

    # User
    path('', user.index, name='user_index'),
    path('search/', user.search, name='user_search'),
    path('search/<int:page>/', user.search, name='user_search_page'),
    path('pg/details/<int:pgid>/', user.PGDetail, name='user_pgdetail'),
    path('pg/contact/<int:pgid>', user.Contact, name='user_contact'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)