from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve
from django.utils.translation import ugettext_lazy as _

from rest_framework import routers

from .views import (
    ProfileViewSet, PlaceViewSet, UserViewSet,
    profile_create, profile_redirect, profile_detail,
    profile_edit, profile_update, profile_delete,
    profile_settings,
    profile_email_update,
    place_detail, place_detail_verbose,
    place_create, place_update, place_delete, place_block, authorize_user,
    country_place_list,
    family_member_create, family_member_update,
    family_member_remove, family_member_delete,
    phone_create, phone_update, phone_delete,
    confirm_hosting_info, place_check,
    search,
)

router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(_(r'^profile/create/$'), profile_create, name='profile_create'),
    url(_(r'^profile(?:/(?P<pk>\d+))?/$'), profile_redirect, name='profile_redirect'),
    url(_(r'^profile/(?P<pk>\d+)(?:/(?P<slug>[\w-]+))?/$'), profile_detail, name='profile_detail'),
    url(_(r'^profile/(?P<pk>\d+)(?:/(?P<slug>[\w-]+))?/edit/$'), profile_edit, name='profile_edit'),
    url(_(r'^profile/(?P<pk>\d+)(?:/(?P<slug>[\w-]+))?/update/$'), profile_update, name='profile_update'),
    url(_(r'^profile/(?P<pk>\d+)(?:/(?P<slug>[\w-]+))?/email/$'), profile_email_update, name='profile_email_update'),
    url(_(r'^profile/(?P<pk>\d+)(?:/(?P<slug>[\w-]+))?/delete/$'), profile_delete, name='profile_delete'),
    url(_(r'^profile/(?P<pk>\d+)(?:/(?P<slug>[\w-]+))?/settings/$'), profile_settings, name='profile_settings'),

    url(_(r'^place/(?P<pk>\d+)/$'), place_detail, name='place_detail'),
    url(_(r'^place/(?P<pk>\d+)/detailed/$'), place_detail_verbose, name='place_detail_verbose'),
    url(_(r'^profile/(?P<pk>\d+)(?:/(?P<slug>[\w-]+))?/place/create/$'), place_create, name='place_create'),
    url(_(r'^place/(?P<pk>\d+)/update/$'), place_update, name='place_update'),
    url(_(r'^place/(?P<pk>\d+)/delete/$'), place_delete, name='place_delete'),
    url(_(r'^place/(?P<pk>\d+)/block/$'), place_block, name='place_block'),

    url(_(r'^place/(?P<pk>\d+)/authorize/$'), authorize_user, name='authorize_user'),

    url(_(r'^place/(?P<place_pk>\d+)/family-member/create/$'), family_member_create, name='family_member_create'),
    url(_(r'^place/(?P<place_pk>\d+)/family-member/(?P<pk>\d+)/update/$'), family_member_update, name='family_member_update'),
    url(_(r'^place/(?P<place_pk>\d+)/family-member/(?P<pk>\d+)/remove/$'), family_member_remove, name='family_member_remove'),
    url(_(r'^place/(?P<place_pk>\d+)/family-member/(?P<pk>\d+)/delete/$'), family_member_delete, name='family_member_delete'),

    url(_(r'^lo/(?P<country_code>[A-Z]{2})(?:/book\:(?P<in_book>(0|1)))?(?:/(?P<email>email))?/$'),
        country_place_list,
        name='country_place_list'),

    url(_(r'^profile/(?P<pk>\d+)(?:/(?P<slug>[\w-]+))?/phone/create/$'), phone_create, name='phone_create'),
    url(_(r'^profile/(?P<profile_pk>\d+)/phone/(?P<pk>\d+)/update/$'), phone_update, name='phone_update'),
    url(_(r'^profile/(?P<profile_pk>\d+)/phone/(?P<pk>\d+)/delete/$'), phone_delete, name='phone_delete'),

    url(_(r'^current/confirm/$'), confirm_hosting_info, name='confirm_hosting_info'),
    url(_(r'^place/(?P<pk>\d+)/check/$'), place_check, name='place_check'),

    url(_(r'^search(?:/(?P<query>.+))?/$'), search, name='search'),
]

urlpatterns += [
    url(r'^api/', include(router.urls)),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += [
        url(r'media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
