from django.apps import apps
from django.http import JsonResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
          
from hitl.models import Epoch, Record

import logging

logger = logging.getLogger(__name__)



class EpochListView(ListView):
    model = Epoch
    template_name = "hitl_table.html"
    ordering = "-date"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['track_type_name'] = "US Import"
        return context


class RecordDetailView(DetailView):
    model = Record

    template_name = 'hitl_record_detail.html'
    slug_field = 'PanjivaRecordID'
    slug_url_kwarg = 'panjivarecordid'

    queryset = Record.objects.using('hitl')

    def get_context_data(self, **kwargs):
        #from VisualComponents_backend.TimeSeries import fetchTimeSeries as TS
        #from VisualComponents_backend.EmbViz_all import main as embTSNE
        from VisualComponents_backend.TimeSeries import fetchTimeSeries as TS
        from VisualComponents_backend.EmbViz_all import main as embTSNE
        from PairwiseComparison.fetchRecord_details import fetchRecord_details
        from VisualComponents_backend.StackedComparison.stackedComparison import get_stackedComparisonPlots

        context = super().get_context_data(**kwargs)

        #app = apps.get_app_config('hitl')
        logger.error("object we are looking for {}".format(self.object.PanjivaRecordID))

        fig1, fig2 = TS.get_TimeSeries(
            self.object.PanjivaRecordID,
            use_cache=True,
            return_type=2
        )

        fig3 = embTSNE.get_record_entityEmbeddings(
            self.object.PanjivaRecordID,
            return_type=2
        )
        entity_pairs = fetchRecord_details(id=self.object.PanjivaRecordID, subDIR="01_2016")
        sorted_pairs = sorted(entity_pairs, key=lambda y: y[2], reverse=True)
        pairs = [[
            list(y[0].keys())[0],
            list(y[1].keys())[0],
            '{0:.3g}'.format(y[2]),
            i
        ] for i, y in enumerate(sorted_pairs)]

        fig_dict = get_stackedComparisonPlots(
            record_id=self.object.PanjivaRecordID, 
            min_count = 500, 
            return_type=1
        )

        context["fig1"] = fig1
        context["fig2"] = fig2
        context["fig3"] = fig3
        context["pairs"] = pairs

        context["carrier_fig"] = fig_dict["Carrier"]
        context["hscode_fig"] = fig_dict["HSCode"]
        context["shipmentorigin_fig"] = fig_dict["ShipmentOrigin"]
        context["shipmentdestination_fig"] = fig_dict["ShipmentDestination"]
        context["portofunlading_fig"] = fig_dict["PortOfUnlading"]
        context["portoflading_fig"] = fig_dict["PortOfLading"]

        # logger.error(entity_pairs)
        return context


show_fields = [
    'ArrivalDate', #'shipmentmonth',
    'ShipmentOrigin', #'consigneecountry',
    'ConsigneePanjivaID',
    'ShipmentOrigin',
    'PlaceOfReceipt', #'countryofsale',
    'ValueOfGoodsUSD',
    'HSCode'
]
hidden_fields = [
    # 'consigneename',
    # 'consigneecity',
    # 'province',
    # 'transportmethod',
    # 'iscontainerized',
    # 'adminregion',
    # 'tradetype',
    # 'hscodekeywords',
    'PanjivaRecordID'
]
pretty_name = {
    'score': 'Score',
    'shipmentmonth': 'Month Shipped',
    'consigneename': 'Consignee Name',
    'consigneecity': 'Consignee City',
    'consigneepanjivaid': 'Consignee',
    'consigneecountry': 'Consignee Country',
    'shipmentorigin': 'Shipment Origin',
    'province': 'Province',
    'countryofsale': 'Country of Sale',
    'transportmethod': 'Transport Method',
    'iscontainerized': 'Containerized',
    'valueofgoodsusd': 'Value',
    'hscode': 'HS Code',
    'hscodekeywords': 'HS Code Keywords',
    'adminregion': 'Admin Region',
    'tradetype': 'Trade Type',
    'panjivarecordid': 'panjivarecordid'
}


def table_format(instance, field):
    value = getattr(instance, field, '')
    if field in ['valueofgoodsusd']:
        return '${:,}'.format(value)
    if field in ['shipmentmonth']:
        return value.strftime('%Y/%m')
    return value


class EpochDetailView(DetailView):
    model = Epoch

    template_name = 'partials/_expanded_row.html'
    slug_field = 'date'
    slug_url_kwarg = 'month'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        app = apps.get_app_config('hitl')
        transactions = app.get_epoch(self.object.path)

        ids = [t[0] for t in transactions]
        records = (
            Record.objects.using("hitl")
                .filter(PanjivaRecordID__in=ids)
                # .only(*Record.CSV_FIELDS)
        )

        scores = dict(transactions)

        fields = ['score'] + show_fields + hidden_fields # + ['comment', 'thumbs']
        id_index = len(fields) - 1#3  # the most magic of numbers

        columns = [{
            'className': "details-control",
            'orderable': False,
            'data': None,
            'defaultContent': ""
        }] + [{
            'title': pretty_name[field] if field in pretty_name else field,
            'data': i
        } for i, field in enumerate(fields)]

        data = []
        for instance in records:
            data.append([
                scores[instance.PanjivaRecordID]
            ] + [
                table_format(instance, field) for field in show_fields
            ] + [
                table_format(instance, field) for field in hidden_fields
            ])


        # columns = [{
        #     'title': field,
        #     'data': i
        # } for i, field in enumerate(Record.CSV_FIELDS + ["Score"])]

        # context = {
        #     "data": [r.to_csv() + [scores[r.PanjivaRecordID] if r.PanjivaRecordID in scores else "???"] for r in records],
        #     "columns": columns

        # }
        table_data = {
            'columns': columns,
            'id_index': id_index,
            'hidden_cols': list(range(len(show_fields) + 1, len(fields) + 1)),
            'data': data,
        }
        import json
        print(json.dumps(table_data))
        return table_data

    def render_to_response(self, context, *args, **kwargs):
        return JsonResponse({
            "data": context,
        })


class HitlExpandRowView(DetailView):
    pass
