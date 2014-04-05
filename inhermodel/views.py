from django.http import Http404
from django.shortcuts import render_to_response
from inhermodel.models import TopLevel
from django.core import serializers

from django.http import HttpResponse

def jsonno(request, pk):
    try:
        tl = TopLevel.objects.get(pk=pk)
    except TopLevel.DoesNotExist:
        raise Http404
    return HttpResponse(serializers.serialize('json', [TopLevel.objects.get(pk=pk)], indent=4, 
                                              relations={'level_one': 
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
