from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from values.models import Value

def index(request):
    values_list = Value.objects.all().order_by('-frequency')
    context = {'values_list': values_list}
    return render(request, 'values/index.html', context)

def detail(request, value_id):
    value = get_object_or_404(Value, pk=value_id)
    return render(request, 'values/detail.html', {'value': value})