from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse, JsonResponse
import json
from pathlib import Path
# from .models import 

class MomentListView(TemplateView):
    # model = Moment
    # context_object_name = 'object_list'
    template_name = 'moments/moment_list.html'

class MomentTitlelView(TemplateView):
    template_name = "moments/community.html"

class MomentTemplatelView(TemplateView):
    template_name = "moments/community_scroll.html"

class MomentModelTemplatelView(TemplateView):
    template_name = "moments/community_scroll_model.html"

class MorePoplView(TemplateView):
    # model = SourceEntry 
    # template_name = 'sources/entry_detail.html'
    template_name = 'moments/more_pop.html'

def FrameJsonView(request):
    CURR_DIR = Path(__file__).resolve().parent
    # print(f"path:{CURR_DIR / 'frames.json'}" )

    with open(CURR_DIR / 'frames.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())

    # print(data)

    return JsonResponse(data, safe=False)