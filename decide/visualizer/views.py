import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404, HttpResponse
import xlwt
from voting.models import Voting
from base import mods

class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            r = mods.get('voting', params={'id': vid})
            context['voting'] = json.dumps(r[0])
        except:
            raise Http404

        return context

class ContactUs(TemplateView):
    try:
        template_name = 'visualizer/contactUs.html'
    except:
        raise Http404

class AboutUs(TemplateView):
    try:
        template_name = 'visualizer/aboutUs.html'
    except:
        raise Http404

def export_users_xls(request, voting_id):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Votacion.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Votacion')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Votos', 'Opcion', 'Puntuacion']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Voting.objects.all().filter(id = voting_id).values_list('postproc')
    for row in rows:
        for dicc in row[0]:
            row_num += 1
            col_num = 0
            valores = list(dicc.values())
            for aux in range(0,4):
                if aux != 1:
                    ws.write(row_num, col_num, valores[aux], font_style)
                    col_num +=1
    wb.save(response)
    return response