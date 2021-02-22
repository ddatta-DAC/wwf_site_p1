from django.apps import apps
from django.http import JsonResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from hitl.models import Epoch, Record


class EpochListView(ListView):
    model = Epoch
    template_name = "hitl_table.html"
    ordering = "-date"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['track_type_name'] = "US Import"
        return context


class EpochDetailView(DetailView):
    model = Epoch

    template_name = 'partials/_expanded_row.html'
    slug_field = 'date'
    slug_url_kwarg = 'month'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        app = apps.get_app_config('hitl')
        transactions = app.get_epoch(self.object.path)

        records = (
            Record.objects.using("hitl")
                .filter(PanjivaRecordID__in=[t[0] for t in transactions])
                .only(*Record.CSV_FIELDS)
        )

        scores = dict(transactions)

        columns = [{
            'title': field,
            'data': i
        } for i, field in enumerate(Record.CSV_FIELDS + ["Score"])]

        context = {
            "data": [r.to_csv() + [scores[r.PanjivaRecordID] if r.PanjivaRecordID in scores else "???"] for r in records],
            "columns": columns

        }
        return context

    def render_to_response(self, context, *args, **kwargs):
        return JsonResponse({
            "data": context,
        })
