from django.shortcuts import render,redirect,HttpResponse

def image(request,id_):
    return HttpResponse("{% load static %}:"+f"<img src='/static/{id_}.jpg'>")

def video(request):
    return HttpResponse(
        f"<video controls><source src='/static/blog/Intimissimi.mp4' type='video/mp4'></source></video>")
0.04
