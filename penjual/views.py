from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.db.models import Sum

from penjual.models import Benih
from . import pub

STATIC_URL = './static'
class SupplyForm(forms.Form):
	wheat = forms.IntegerField(label = "suplai beras")
	corn = forms.IntegerField(label = "suplai jagung")
	pea = forms.IntegerField(label = "suplai kacang")

sub = pub.subscribe('beras')

# Create your views here.
def index(request):
	return render(request, "index.html", {
		"formSuplai": SupplyForm()
	})

def pub_data(request):
	if request.method == 'POST':
		form = SupplyForm(request.POST)
		if form.is_valid():
			jumlah_beras = form.cleaned_data.get("wheat")
			jumlah_jagung = form.cleaned_data.get("corn")
			jumlah_kacang = form.cleaned_data.get("pea")
			dbBenih = Benih(
				jumlah_beras = int(jumlah_beras),
				jumlah_jagung = int(jumlah_jagung),
				jumlah_kacang = int(jumlah_kacang)
			)
			dbBenih.save()
		sum_beras = Benih.objects.aggregate(Sum('jumlah_beras')).get("jumlah_beras__sum")
		sum_jagung = Benih.objects.aggregate(Sum('jumlah_jagung')).get("jumlah_jagung__sum")
		sum_kacang = Benih.objects.aggregate(Sum('jumlah_kacang')).get("jumlah_kacang__sum")
		pub.publish_data_on_redis(sum_beras, "beras")
		pub.publish_data_on_redis(sum_jagung, "jagung")
		pub.publish_data_on_redis(sum_kacang, "kacang")
	return render(request, "published.html", {
		"beras": sum_beras,
		"jagung": sum_jagung,
		"kacang": sum_kacang
	})

def sub_data(request):
	data = pub.get_data(sub, 'beras')
	return render(request, "subscribed.html", {
		"topic": "beras",
		"amount": data
	})

def save_pub_data(beras, jagung, kacang):
	benih = {"beras": beras, "jagung": jagung, "kacang": kacang}
	return Benih