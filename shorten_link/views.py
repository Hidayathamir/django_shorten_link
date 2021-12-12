from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import LinkForm
from .models import Link


def home(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"Success! Your Shortened Link is 127.0.0.1:8000/shorten-link/{form.cleaned_data['shortened_link']}",
            )
            return redirect(reverse(home))
        else:
            context = {"form": form}
            return render(request, "shorten_link/home.html", context)

    else:
        form = LinkForm()
        context = {"form": form}
        return render(request, "shorten_link/home.html", context)


def redirect_link(request, shortened_link):
    redirect_link = get_object_or_404(Link, pk=shortened_link)
    return redirect(redirect_link.link)
