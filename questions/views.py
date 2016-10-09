from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import Http404, JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST,require_http_methods
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Popper
from .models import Candle
from .models import Balloon
from .models import Knife_Caketag
from .models import Prop_Decoration
from .models import Crown
from .models import Cap
from itertools import chain
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

# Create your views here.
@csrf_exempt
def front(request):
    #context = {'q_list' : Question.objects.all() }
    return render(request, 'questions/mystyle.html');
@csrf_exempt
def about(request):
    #context = {'q_list' : Question.objects.all() }
    return render(request, 'questions/about.html');
@csrf_exempt
def contact(request):
    return render(request, 'questions/contact.html');
@csrf_exempt
def all_Popper(request):
    context = {'q_list' : Popper.objects.all().order_by('-id') }
    return render(request, 'questions/index.html', context);

@csrf_exempt
def all_Candle(request):
    context = {'q_list' : Candle.objects.all().order_by('-id') }
    return render(request, 'questions/index.html', context);

@csrf_exempt
def all_Balloon(request):
    context = {'q_list' : Balloon.objects.all().order_by('-id')}
    return render(request, 'questions/index.html', context);
@csrf_exempt
def all_Cap(request):
    context = {'q_list' : Cap.objects.all().order_by('-id')  }
    return render(request, 'questions/index.html', context);
@csrf_exempt
def all_Knife_Caketag(request):
    context = {'q_list' : Knife_Caketag.objects.all().order_by('-id')  }
    return render(request, 'questions/index.html', context);

@csrf_exempt
def all_Prop_Decoration(request):
    context = {'q_list' : Prop_Decoration.objects.all().order_by('-id')  }
    return render(request, 'questions/index.html', context);

@csrf_exempt
def all_Crown(request):
    context = {'q_list' : Crown.objects.all().order_by('-id')  }
    return render(request, 'questions/index.html', context);
@csrf_exempt
def all_New(request):
    a=Crown.objects.all()
    b=Balloon.objects.all()
    c =[];
    app_models = apps.get_app_config('questions').get_models()
    for model in app_models:    
        c= c + list(model.objects.all().order_by('-id')[:3]);
    context = {'q_list' : c};
    return render(request, 'questions/index.html', context);


