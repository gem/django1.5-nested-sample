from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from inhermodel.models import TopLevel
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.cache import add_never_cache_headers
from django.views.generic.detail import BaseDetailView
import json


def jsonno(request, pk):
    try:
        tl = TopLevel.objects.get(pk=pk)
    except TopLevel.DoesNotExist:
        raise Http404
    return HttpResponse(serializers.serialize('json', [TopLevel.objects.get(pk=pk)], choices=True,
                                              indent=4, relations={'level_one': 
                                                                   {'relations': 
                                                                    {'level_two' : 
                                                                     {'relations':
                                                                          ('level_three', ) 
                                                                      }
                                                                     }
                                                                    },
                                                                   'level_one_bi': {}
                                                                   }))

    # return render_to_response('polls/detail.html', {'poll': p})
    return HttpResponse('<h1>Page was found</h1>')

class ChainedSelectChoices(BaseDetailView):
    """
    View to handel the ajax request for the field options.
    """

    def get(self, request, *args, **kwargs):
        field = request.GET.get('field')
        parent_value = request.GET.get("parent_value")

        vals_list = []
        for x in range(1,5):
            vals_list.append(x*int(parent_value))

        choices = tuple(zip(vals_list, vals_list))

        response = HttpResponse(
            json.dumps(choices, cls=DjangoJSONEncoder),
            mimetype='application/javascript'
        )
        add_never_cache_headers(response)
        return response

