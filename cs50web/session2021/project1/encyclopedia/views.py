from django.shortcuts import render

from . import util
import markdown2, random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def retrieve(request, title):
    if util.get_entry(title) == None:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested wiki page could not be retrieved."
        })
    else:
        return render(request, "encyclopedia/display.html", {
            "topic": util.get_entry(title).split('\n')[0][2:],
            "entry": markdown2.markdown(util.get_entry(title))
        })

def search(request):
    title = request.GET["q"]
    if util.get_entry(title) == None:
        return render(request, "encyclopedia/matches.html", {
            "entries": [item for item in util.list_entries() if title in item]
        })
    else:
        return render(request, "encyclopedia/display.html", {
            "topic": util.get_entry(title).split('\n')[0][2:],
            "entry": markdown2.markdown(util.get_entry(title))
        })

def newpage(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        if title in util.list_entries():
            return render(request, "encyclopedia/error.html", {
            "message": "An encyclopedia entry already exists with that title."
        })
        filename = "entries/" + title + ".md"
        fout = open(filename, "w")
        fout.write("# " + title + "\n\n")
        fout.write(content)
        fout.close()
        return render(request, "encyclopedia/display.html", {
            "topic": util.get_entry(title).split('\n')[0][2:],
            "entry": markdown2.markdown(util.get_entry(title))
        })
    
    return render(request, "encyclopedia/newpage.html")

def editpage(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        filename = "entries/" + title + ".md"
        fout = open(filename, "w")
        fout.write("# " + title + "\n\n")
        fout.write(content)
        fout.close()
        return render(request, "encyclopedia/display.html", {
            "topic": util.get_entry(title).split('\n')[0][2:],
            "entry": markdown2.markdown(util.get_entry(title))
        })
    else:
        title = request.GET["q"]
        return render(request, "encyclopedia/editpage.html", {
                "topic": util.get_entry(title).split('\n')[0][2:],
                "entry": util.get_entry(title).split('\n')[2]
            })


def randompage(request):
    title = random.choice(util.list_entries())
    return render(request, "encyclopedia/display.html", {
            "topic": util.get_entry(title).split('\n')[0][2:],
            "entry": markdown2.markdown(util.get_entry(title))
        })




