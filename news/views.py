import os
from django.shortcuts import render, get_object_or_404, redirect
from datetime import date
from .forms import InformationForm
from .models import Information, Category
from django.utils import timezone
from core.utils import *
from django.contrib import messages
from django.core.paginator import Paginator
import hashlib
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users


# Create your views here.
def blog_detail(request, hashid):
    post = get_object_or_404(Information, hashed=hashid)
    categories = Category.objects.all()
    context = {
        'post': post,
        'categories': categories,
    }
    return render(request, 'blog_details.html', context)


def News(request):
    info_list = Information.objects.all().order_by('-created')

    # Optional: search by keyword
    q = request.GET.get('q')
    if q:
        info_list = info_list.filter(title__icontains=q)

    paginator = Paginator(info_list, 6)  # 3 news items per page
    page_number = request.GET.get('page')
    infos = paginator.get_page(page_number)

    return render(request, 'blog.html', {'infos': infos, 'q': q})


@login_required()
@allowed_users(allowed_roles=['Admin'])
def addInformation(request):
    if request.method == 'POST':
        form = InformationForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            raw_string = str(instance.pk)  
            instance.hashed = hashlib.md5(raw_string.encode('utf-8')).hexdigest()
            instance.save()
            messages.success(request, 'Information is added successfully.')
            if 'save_and_add_another' in request.POST:
                return redirect('addinfo')  
            return redirect('addinfo')  
    else:
        form = InformationForm()
    context = {
        'form': form,
    }
    return render(request, 'infoForm.html', context)

@login_required
def NewsAdmin(request):
    info = Information.objects.all()
    context = {
        'info': info,
    }
    return render(request, 'admin/listaInformasaun.html', context)

@login_required()
def updateInformasaun(request,hashid):
	infoData = get_object_or_404(Information,hashed=hashid)
	if request.method == 'POST':
		form = InformationForm(request.POST,instance=infoData)
		if form.is_valid():
			instance = form.save()
			messages.info(request, f'Informasaun is updated Successfully.')
			return redirect('newsadmin')
	else:
		form = InformationForm(instance=infoData)
	context = {
		# 'sukuActive':"active",
		'page':"form",
		'form': form, 
	}
	return render(request, 'infoForm.html', context)

@login_required
def DeleteInformasaun(request, hashid):
    info = get_object_or_404(Information, hashed=hashid)  # Note: uses 'hashed' field
    naran_info = info.title
    
    if request.method == 'POST':
        info.delete()
        messages.warning(request, f'Information "{naran_info}" has been permanently deleted.')
        return redirect('newsadmin')
    
    # For GET request, show confirmation page
    context = {
        'info': info,
        'title': 'Delete Information'
    }
    return render(request, 'admin/deleteinformasaun.html', context)