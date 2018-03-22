from django.shortcuts import render
# from dmc.models import Menu, Sub_menu, Sub_of_sub_menu, Video_slider, Image_slider, Product, Sub_product, About

# Create your views here.

def index(request):
	# mindex = Menu.objects.all()
	# smindex = Sub_menu.objects.all()
	# ssmindex = Sub_of_sub_menu.objects.all()
	# vslindex = Video_slider.objects.all()
	# islindex = Image_slider.objects.all()
	# pindex = Product.objects.all()
	# spindex = Sub_product.objects.all()
	# context = {'mindex' : mindex, 'smindex' : smindex, 'ssmindex' : ssmindex, 'vslindex' : vslindex, 'islindex' : islindex, 'pindex' : pindex, 'spindex' : spindex}
	return render(request, 'index.html')

def contact(request):
	# mindex = Menu.objects.all()
	# smindex = Sub_menu.objects.all()
	# ssmindex = Sub_of_sub_menu.objects.all()
	# context = {'mindex' : mindex, 'smindex' : smindex, 'ssmindex' : ssmindex}
	return render(request, 'contact.html')

def about(request):
	# mindex = Menu.objects.all()
	# smindex = Sub_menu.objects.all()
	# ssmindex = Sub_of_sub_menu.objects.all()
	# abindex = About.objects.all()
	# context = {'mindex' : mindex, 'smindex' : smindex, 'ssmindex' : ssmindex, 'abindex' : abindex}
	return render(request, 'about.html')

def products(request):
	# mindex = Menu.objects.all()
	# smindex = Sub_menu.objects.all()
	# ssmindex = Sub_of_sub_menu.objects.all()
	# pindex = Product.objects.all()
	# spindex = Sub_product.objects.all()
	# context = {'mindex' : mindex, 'smindex' : smindex, 'ssmindex' : ssmindex, 'pindex' : pindex, 'spindex' : spindex }
	return render(request, 'portfolio.html')

def services(request):
	# mindex = Menu.objects.all()
	# smindex = Sub_menu.objects.all()
	# ssmindex = Sub_of_sub_menu.objects.all()
	# context = {'mindex' : mindex, 'smindex' : smindex, 'ssmindex' : ssmindex}
	return render(request, 'services.html')			

def certificate(request):
	# mindex = Menu.objects.all()
	# smindex = Sub_menu.objects.all()
	# ssmindex = Sub_of_sub_menu.objects.all()
	# context = {'mindex' : mindex, 'smindex' : smindex, 'ssmindex' : ssmindex}
	return render(request, 'certificate.html')	

def careers(request):
	# mindex = Menu.objects.all()
	# smindex = Sub_menu.objects.all()
	# ssmindex = Sub_of_sub_menu.objects.all()
	# context = {'mindex' : mindex, 'smindex' : smindex, 'ssmindex' : ssmindex}
	return render(request, 'careers.html')			

