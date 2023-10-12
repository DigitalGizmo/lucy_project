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

def FrameJsonView(request):
    CURR_DIR = Path(__file__).resolve().parent
    print(f"path:{CURR_DIR / 'frames.json'}" )
    # with open(CURR_DIR / 'frames.json') as f:
    #     data = json.loads(f.read())
    data = {
        "cars": ["ford", "BMW", "Fiat"],
        "community":          
        [
            {
                "imageName": "02-dawn-house-color",
                "storyText": "To be used later, in a loop",
                "moreWhoLinks": [
                    {"title": "Jenny Cole", 
                        "type": "internal", "url": "/people"},
                    {"title": "Cesar", 
                        "type": "external", "url": "https://digitalgizmo.com/"}
                ],
                "moreTopicLinks": [
                    {"title": "Sleeping Arrangements", 
                        "type": "external", "url": "https://digitalgizmo.com/"},            
                ]
            },
            {
                "imageName": "03-candle-color",
                "storyText": "Frame index 1 -- To be used later, in a loop",
                "moreWhoLinks": [
                    {"title": "Phillis Wheatley", 
                        "type": "internal", "url": "/people"},
                    {"title": "Cesar", 
                        "type": "external", "url": "https://digitalgizmo.com/"}
                ],
                "moreTopicLinks": [
                    {"title": "Women's work", 
                        "type": "external", "url": "https://digitalgizmo.com/"}            
                ]
            }
        ]
    }

    return JsonResponse(data, safe=False)