from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import Relatoriu
from .forms import RelatoriuForm
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import hashlib
import os
from core.utils import *


def lista_relatoriu(request):
    # Hetan relatoriu hotu
    relatorius = Relatoriu.objects.all().order_by('-data')
    
    # Filter ba tinan
    tinan_filter = request.GET.get('tinan')
    if tinan_filter:
        relatorius = relatorius.filter(data__year=tinan_filter)
    
    # Lista tinan sira ne'ebé iha relatoriu
    tinan_sira = Relatoriu.objects.dates('data', 'year', order='DESC')
    
    context = {
        'relatorius': relatorius,
        'tinan_sira': [tinan.year for tinan in tinan_sira],
        'tinan_filter': tinan_filter
    }
    return render(request, 'lista_relatoriu.html', context)

# @login_required
# def detalhu_relatoriu(request, hashid):
#     """Detalhu relatoriu ida"""
#     relatoriu = get_object_or_404(Relatoriu, hashed=hashid)
    
#     context = {
#         'relatoriu': relatoriu
#     }
#     return render(request, 'detalhu_relatoriu.html', context)

@login_required
def lista_relatoriuAdmin(request):
    # Hetan relatoriu hotu
    relatorius = Relatoriu.objects.all().order_by('-data')
    # Filter ba tinan
    tinan_filter = request.GET.get('tinan')
    if tinan_filter:
        relatorius = relatorius.filter(data__year=tinan_filter)
    # Lista tinan sira ne'ebé iha relatoriu
    tinan_sira = Relatoriu.objects.dates('data', 'year', order='DESC')
    context = {
        'relatorius': relatorius,
        'tinan_sira': [tinan.year for tinan in tinan_sira],
        'tinan_filter': tinan_filter
    }
    return render(request, 'Admin/lista_relatoriuA.html', context)


def lista_relatoriu(request):
    # Hetan relatoriu hotu
    relatorius = Relatoriu.objects.all().order_by('-data')
    # Filter ba tinan
    tinan_filter = request.GET.get('tinan')
    if tinan_filter:
        relatorius = relatorius.filter(data__year=tinan_filter)
    # Lista tinan sira ne'ebé iha relatoriu
    tinan_sira = Relatoriu.objects.dates('data', 'year', order='DESC')
    context = {
        'relatorius': relatorius,
        'tinan_sira': [tinan.year for tinan in tinan_sira],
        'tinan_filter': tinan_filter
    }
    return render(request, 'lista_relatoriu.html', context)

@login_required
def detalhu_relatoriuAdmin(request, relatoriu_id):
    """Detalhu relatoriu ida"""
    relatoriu = get_object_or_404(Relatoriu, id=relatoriu_id)
    
    context = {
        'relatoriu': relatoriu
    }
    return render(request, 'Admin/detalhu_relatoriuA.html', context)


@login_required
def addRelatoriu(request):
    if request.method == 'POST':
        form = RelatoriuForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                
                # Generate hash
                temp_id = Relatoriu.objects.count() + 1
                raw_string = f"{temp_id}{instance.titulu}"
                instance.hashed = hashlib.md5(raw_string.encode('utf-8')).hexdigest()
                
                instance.save()
                
                # Update hash ho PK real
                raw_string = str(instance.pk)
                instance.hashed = hashlib.md5(raw_string.encode('utf-8')).hexdigest()
                instance.save()
                
                messages.success(request, f'Relatóriu "{instance.titulu}" aumenta ho susesu!')
                
                if 'save_and_add_another' in request.POST:
                    return redirect('addRelatoriu')
                return redirect('lista_relatoriuAdmin')
                
            except Exception as e:
                messages.error(request, f'Error: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RelatoriuForm()
    
    context = {
        'form': form,
        'title': 'Aumenta Relatóriu Foun'
    }
    return render(request, 'admin/FormRelatoriu.html', context)


@login_required
def atualiza_relatoriu(request, hashid):
    infoData = get_object_or_404(Relatoriu, hashed=hashid)  # Note: uses 'hashed' field
    if request.method == 'POST':
        form = RelatoriuForm(request.POST, request.FILES, instance=infoData)  # Add request.FILES
        if form.is_valid():
            instance = form.save()
            messages.info(request, f'Relatóriu "{instance.titulu}" atualiza ho susesu!')
            return redirect('lista_relatoriuAdmin')
    else:
        form = RelatoriuForm(instance=infoData)
    
    context = {
        'form': form,
        'title': 'Atualiza Relatóriu'
    }
    return render(request, 'Admin/updaterelatoriu.html', context)

@login_required
def delete_relatoriu(request, hashid):
    relatoriu = get_object_or_404(Relatoriu, hashed=hashid)
    
    if request.method == 'POST':
        titulu_relatoriu = relatoriu.titulu
        relatoriu.delete()
        messages.warning(request, f'Relatóriu "{titulu_relatoriu}" apaga ho susesu!')
        return redirect('lista_relatoriuAdmin')
    
    # Ba GET request, hatudu pájina konfirmasaun
    context = {
        'relatoriu': relatoriu,
        'title': 'Apaga Relatóriu'
    }
    return render(request, 'Admin/delete_relatoriu.html', context)
    


