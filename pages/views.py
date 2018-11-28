from django.shortcuts import render
from .models import WikiPages

# Create your views here.
def wiki_list(request):
	context = {
	"pages":WikiPages.objects.all()
	}
	return render(request, 'list.html', context)

def wiki_detail(request, page_id):
    context = {"page":WikiPages.objects.get(id=page_id)

    }	

    return render(request, 'detail.html', context)
