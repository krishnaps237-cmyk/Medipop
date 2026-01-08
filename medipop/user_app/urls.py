from django.urls import path
from.import views
urlpatterns=[
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('login',views.login_user,name="login"),
    path('logout',views.logout_user,name="logout"),
    path('view_user',views.views_user,name="view_user"),
    path('deactivate_user/<int:id>/',views.deactivate_user,name="deactivate_user"),
    path('activate_user/<int:id>/',views.activate_user,name="activate_user"),
    path('profile',views.profile,name="profile"),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('change_password',views.change_password,name="change_password"),
    path('forgot_password',views.forgot_password,name="forgot_password"),
]