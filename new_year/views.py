from django.shortcuts import render, redirect
import uuid
from .models import NewYearArticle
from .utils import qr_code_make, delete_qr_image
from django.http import JsonResponse


def home_page(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        receiver = request.POST.get('receiver')
        text = request.POST.get('text')
        qr_hash = uuid.uuid4()
        NewYearArticle.objects.create(sender_name=name, receiver_name=receiver, body=text, qr_code=qr_hash)
        filename = qr_code_make(qr_hash)
        context['qr_image'] = filename

    return render(request, 'home.html', context=context)


def delete_qr_code(request):
    filename = request.GET.get('qr_id').split('/')[-1]
    delete_qr_image(filename)
    return JsonResponse({"status": True})


def congrats(request, qr_hash):
    context = {}
    data = NewYearArticle.objects.get(qr_code=qr_hash)

    context['name'] = data.sender_name
    context['receiver'] = data.receiver_name
    context['text'] = data.body

    return render(request, 'congrats.html', context=context)
