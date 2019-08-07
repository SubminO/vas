from django.urls import path

from purple_admin import views

urlpatterns = [
    path('', views.cabinet, name='admin_panel_cabinet'),
    path('route_list', views.cabinet_list, {'type': 'route'}, name='admin_panel_route_list'),
    path('route_add', views.cabinet_add, {'type': 'route'}, name='admin_panel_route_add'),
    path('route_edit/<int:pk>/', views.cabinet_edit, {'type': 'route'}, name='admin_panel_route_edit'),
    path('route_delete/<int:pk>/', views.cabinet_delete, {'type': 'route'}, name='admin_panel_route_delete'),
    path('route_platform_list', views.cabinet_list, {'type': 'route_platform'}, name='admin_panel_route_platform_list'),
    path('route_platform_add', views.cabinet_add, {'type': 'route_platform'}, name='admin_panel_route_platform_add'),
    path('route_platform_edit/<int:pk>/', views.cabinet_edit, {'type': 'route_platform'}, name='admin_panel_route_platform_edit'),
    path('route_platform_delete/<int:pk>/', views.cabinet_delete, {'type': 'route_platform'},
         name='admin_panel_route_platform_delete'),
    path('route_relation_add_ajax', views.cabinet_add, {'type': 'route_platform_type'}, name='admin_panel_route_platform_type_relation_ajax_add'),
    path('route_add', views.ajax_add, {'type': 'route'}, name='admin_panel_ajax_add'),
]

