from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.users.api_views import global_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/search/', global_search, name='global_search'),
    path('', include('apps.users.urls')),
    path('wallets/', include('apps.wallets.urls')),
    path('team/', include('apps.genealogy.urls')),
    path('fund/', include('apps.transactions.urls')),
    path('rank/', include('apps.ranks.urls')),
    path('support/', include('apps.support.urls')),
    path('income/', include('apps.incomes.urls')),
    path('reports/', include('apps.reports.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
