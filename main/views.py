from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users 

# from django.db.models import Sum, Count
# # from custom.models import *	
# # from Ano.models import * 
# from django.db.models import Q

@login_required()
def indexAdmin(request): 
	
	# context = {
		
		
	# 	}
	return render(request, 'home/indexApp.html')

