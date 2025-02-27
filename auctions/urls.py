from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing", views.listing, name="listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("allList", views.allList, name="allList"),
    path("create", views.create, name="create"),
    path("category", views.category, name="category"),
    path("<int:item>", views.item, name="item")
]
