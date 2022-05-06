from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
import datetime

from .models import User, Bid, Comment, Listing


class CreateListingForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(label="Description")
    starting_bid = forms.FloatField(label="Starting Bid")
    url = forms.CharField(label="URL")
    CHOICES = (('Apparel','Apparel'), ('Kitchen','Kitchen'), ('Vehicles','Vehicles'), ('Media','Media'),)
    category = forms.ChoiceField(choices=CHOICES)


class CreateBidForm(forms.Form):
    current_bid = forms.FloatField(label="Current Bid")


class CreateWatchlistForm(forms.Form):
    listing_id = forms.IntegerField(label="Listing ID")


class CreateCloseListingForm(forms.Form):
    listing_id = forms.IntegerField(label="Listing ID")


class CreateReactivateListingForm(forms.Form):
    listing_id = forms.IntegerField(label="Listing ID")


class CreateCommentForm(forms.Form):
    listing_id = forms.IntegerField(label="Listing ID")
    listing_comment = forms.CharField(label="Listing Comment")


# Create a new auction listing
@login_required
def create(request):
    if request.method == "POST":
        form = CreateListingForm(request.POST)
        if form.is_valid():
            current_user = request.user
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            starting_bid = form.cleaned_data["starting_bid"]
            category = form.cleaned_data["category"]
            url = form.cleaned_data["url"]
            
            # Create the relevant database objects and save them
            l = Listing(title=title, description=description, creator=current_user, category=category, timestamp=datetime.datetime.now(), url=url, active=True)
            l.save()
            b = Bid(price=starting_bid, bidder=current_user)
            b.save()
            l.bids.add(b)
            l.save()
            
            # Redirect user to the auction listings
            return HttpResponseRedirect(reverse("index"))
        else:
            # If the form is invalid, re-render the page
            return render(request, "create.html", {
                "form": form
            })

    return render(request, "auctions/create.html", {
        "form": CreateListingForm()
    })


def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.method == "POST":
        form = CreateBidForm(request.POST)
        if form.is_valid():
            current_user = request.user
            current_bid = form.cleaned_data["current_bid"]
            # Create the relevant database objects and save them
            b = Bid(price=current_bid, bidder=current_user)
            b.save()
            listing.bids.add(b)
            listing.save()
            
            # Redirect user to the listing page
            #return HttpResponseRedirect(reverse("listing"))
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "bids": listing.bids.all(),
                "watchlist": listing.watchlist.all(),
                "user": request.user,
                "comments": listing.comments.all()
            })
        else:
            # If the form is invalid, re-render the page
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "bids": listing.bids.all(),
                "watchlist": listing.watchlist.all(),
                "user": request.user,
                "comments": listing.comments.all()
            })
    
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "bids": listing.bids.all(),
        "watchlist": listing.watchlist.all(),
        "user": request.user,
        "comments": listing.comments.all()
    })
    

def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        "listings": listings
    })


@login_required
def categories(request):
    return render(request, "auctions/categories.html")


@login_required
def display(request, category):
    listings = Listing.objects.filter(category=category)
    if not listings:
        content = f"No listings are present in the {category} category."
        return render(request, "auctions/message.html", {
            "content": content
        })
    else:
        return render(request, "auctions/index.html", {
            "listings": listings
        })


@login_required
def message(request):
    pass
    

@login_required
def watchlist(request):
    listings = Listing.objects.filter(watchlist__username=request.user)
    return render(request, "auctions/watchlist.html", {
        "listings": listings
    })


@login_required
def success(request):
    if request.method == "POST":
        form = CreateWatchlistForm(request.POST)
        if form.is_valid():
            listing_id = form.cleaned_data["listing_id"]
            listing = Listing.objects.get(id=listing_id)            

            if request.user not in listing.watchlist.all():
                listing.watchlist.add(request.user)
            else:
                listing.watchlist.remove(request.user)
            listing.save()
            
            # Redirect user to the success page
            return render(request, "auctions/success.html", {
                "listing": listing,
                "watchlist": listing.watchlist.all(),
                "user": request.user
            })
        else:
            # If form is invalid, redirect user to the index page        
            return render(request, "auctions/index.html", {
                "listings": Listing.objects.all()
            })

    # Otherwise, redirect user to the index page        
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


@login_required
def close(request):
    if request.method == "POST":
        form = CreateCloseListingForm(request.POST)
        if form.is_valid():
            listing_id = form.cleaned_data["listing_id"]
            listing = Listing.objects.get(id=listing_id)
            listing.active = False
            listing.save()
            
            # Redirect user to the close page
            return render(request, "auctions/close.html", {
                "listing": listing,
                "bids": listing.bids.all()
            })
        else:
            # If form is invalid, redirect user to the index page        
            return render(request, "auctions/index.html", {
                "listings": Listing.objects.all()
            })

    # Otherwise, redirect user to the index page        
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


@login_required
def reactivate(request):
    if request.method == "POST":
        form = CreateReactivateListingForm(request.POST)
        if form.is_valid():
            listing_id = form.cleaned_data["listing_id"]
            listing = Listing.objects.get(id=listing_id)
            listing.active = True
            listing.save()
            
            # Redirect user to the reactivate page
            return render(request, "auctions/reactivate.html", {
                "listing": listing,
                "bids": listing.bids.all()
            })
        else:
            # If form is invalid, redirect user to the index page        
            return render(request, "auctions/index.html", {
                "listings": Listing.objects.all()
            })

    # Otherwise, redirect user to the index page        
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


@login_required
def comment(request):
    if request.method == "POST":
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            listing_id = form.cleaned_data["listing_id"]
            listing = Listing.objects.get(id=listing_id)
            listing_comment = form.cleaned_data["listing_comment"]
            
            c = Comment(content=listing_comment, author=request.user)
            c.save()
            listing.comments.add(c)
            listing.save()
            
            # Redirect user to the close page
            return render(request, "auctions/comment.html", {
                "listing": listing,
                "comments": listing.comments.all()
            })
        else:
            # If form is invalid, redirect user to the index page        
            return render(request, "auctions/index.html", {
                "listings": Listing.objects.all()
            })

    # Otherwise, redirect user to the index page        
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
