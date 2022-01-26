from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day.",
    "march": "Walk for at least 30 minutes every day.",
    "april": "Walk for at least 40 minutes every day.",
    "may": "Walk for at least 50 minutes every day.",
    "june": "Walk for at least 60 minutes every day.",
    "july": "Walk for at least 70 minutes every day.",
    "august": "Walk for at least 80 minutes every day.",
    "september": "Walk for at least 90 minutes every day.",
    "october": "Walk for at least 100 minutes every day.",
    "november": "Walk for at least 110 minutes every day.",
    "december": None
}


# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])  # /challenges/january

        return HttpResponseRedirect(redirect_path)
    except IndexError:
        return HttpResponseNotFound("Invalid Month!")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]

        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except KeyError:
        raise Http404()
