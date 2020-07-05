from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import markdown2
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def ran(request):
    ent = util.list_entries()
    name = random.choice(ent)
    return HttpResponseRedirect(reverse("page",args=[name]))

def search(request):
    data = request.POST
    name = data["q"]
    titles = util.list_entries()
    if name in titles:
        return HttpResponseRedirect(reverse("page",args=[name]))
    else:
        pages = []
        for title in titles:
            if name.lower() in title.lower():
                pages.append(title)
        
        return render(request, "encyclopedia/searches.html", {
            "entries": pages
        })

def edit(request,name):
    if request.method == 'POST':
        data = request.POST
        content = data["Content"]
        util.save_entry(name, content)
        return HttpResponseRedirect(reverse("page",args=[name]))

    content = util.get_entry(name)
    return render(request, "encyclopedia/edit.html",{
        "content" : content,
        "name" : name
    })

def new(request):
    if request.method == 'POST':
        data = request.POST
        Title = data["Title"]
        titles = util.list_entries()
        if Title in titles:
            error = "Page Already exists"
            return HttpResponseRedirect(reverse("error",args=[error]))
        
        content = data["Content"]
        util.save_entry(Title, content)
        return HttpResponseRedirect(reverse("page",args=[Title]))
    
    return render(request, "encyclopedia/newFile.html")

def error(request,error):
    return render(request, "encyclopedia/error.html", {
        "error" : error
    })

def page(request ,name):
    page = util.get_entry(name)
    if page == None:
        error = "Page Not Found"
        return HttpResponseRedirect(reverse("error",args=[error]))
        
    text = markdown2.markdown(page)
    return render(request, "encyclopedia/pages.html",{
        "text" : text,
        "name" : name
    })

