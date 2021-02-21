"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from . import views
from trade.views import get_results, AnomalyView, AnomalyApiView, SubmitThumbsView, SubmitCommentView, ChinaImportExpandRowView, ChinaExportExpandRowView, PeruExportExpandRowView, UsImportExpandRowView, DefaultExpandRowView
# from hitl.views import us_import

urlpatterns = [
    path('home', views.home, name='data_home'),
    path('', views.home, name='data_home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('invitations/', include('invitations.urls', namespace='invitations')),
    # path('track/us_import', us_import, name="us_import"),
    path('track/v1/<slug:track_name>', views.data_home, name='track'),
    path('anomaly/<slug:track_name>/<slug:panjivarecordid>', AnomalyView.as_view(), name='anomaly'),
    path('api/anomaly/<slug:track_name>/<slug:panjivarecordid>', AnomalyApiView.as_view(), name='anomaly_api'),
    path('api/<slug:track_name>', get_results, name='results'),
    path('api/comment/<slug:track_name>', SubmitCommentView.as_view(), name='submit_comment'),
    path('api/thumbs/<slug:track_name>', SubmitThumbsView.as_view(), name='submit_thumbs'),
    path('api/expand_row/china_import/<slug:panjivarecordid>', ChinaImportExpandRowView.as_view()),
    path('api/expand_row/china_export/<slug:panjivarecordid>', ChinaExportExpandRowView.as_view()),
    path('api/expand_row/peru_export/<slug:panjivarecordid>', PeruExportExpandRowView.as_view()),
    path('api/expand_row/us_import/<slug:panjivarecordid>', UsImportExpandRowView.as_view()),
    path('api/expand_row/<slug:track_name>', DefaultExpandRowView.as_view(), name='expand_row'),
]

urlpatterns += [
    path('viz_attr_selection', views.viz_attr_selection, name='viz_attr_selection'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
