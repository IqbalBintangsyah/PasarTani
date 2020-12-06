from django.shortcuts import render
from django.template.defaulttags import register
from django import forms
from django.db.models import Sum

from penjual.models import Benih

from . import sub
# Create your views here.

class ChooseForm(forms.Form):
    CHOICES = [('u', 'unsubscribe'), ('s', 'subscribe')]
    wheat = forms.CharField(label='beras', widget=forms.RadioSelect(choices=CHOICES))
    corn = forms.CharField(label='jagung', widget=forms.RadioSelect(choices=CHOICES))
    pea = forms.CharField(label='kacang', widget=forms.RadioSelect(choices=CHOICES))

STATIC_URL = './static'

subs = sub.subscribe('beras')

def indexp(request):
    jml = sub.get_data(subs, "beras")
    return render(request, "indexp.html", {
        "jumlah" : int(jml['data'])
    })

def pilih(request):
    return render(request, "pilih.html", {
        "form": ChooseForm()
    })

def dashboard(request):
    if "subskripsi" not in request.session:
        request.session["subskripsi"] = {}
    #jumlah_beras = sub.get_data(subs, "beras")
    #jumlah_jagung = sub.get_data(subs, "jagung")
    #jumlah_kacang = sub.get_data(subs, "kacang")
    jumlah_beras = Benih.objects.aggregate(Sum('jumlah_beras')).get("jumlah_beras__sum")
    jumlah_jagung = Benih.objects.aggregate(Sum('jumlah_jagung')).get("jumlah_jagung__sum")
    jumlah_kacang = Benih.objects.aggregate(Sum('jumlah_kacang')).get("jumlah_kacang__sum")
    if request.method == 'POST':
        form = ChooseForm(request.POST)
        if form.is_valid():
            info_beras = form.cleaned_data.get("wheat")
            info_jagung = form.cleaned_data.get("corn")
            info_kacang = form.cleaned_data.get("pea")
        if info_beras == 's':
            request.session["subskripsi"]["beras"] = int(jumlah_beras)
        elif info_beras == 'u' and "beras" in request.session["subskripsi"]:
            request.session["subskripsi"].pop("beras")
        if info_jagung == 's':
            request.session["subskripsi"]["jagung"] = int(jumlah_jagung)
        elif info_jagung == 'u' and "jagung" in request.session["subskripsi"]:
            request.session["subskripsi"].pop("jagung")
        if info_kacang == 's':
            request.session["subskripsi"]["kacang"] = int(jumlah_kacang)
        elif info_kacang == 'u' and "kacang" in request.session["subskripsi"]:
            request.session["subskripsi"].pop("kacang")
    return render(request, "dashboard.html", {
        "subscribe": request.session["subskripsi"]
    })

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)