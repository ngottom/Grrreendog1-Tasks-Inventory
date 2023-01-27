from unicodedata import category
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing, Comment, Employee, EmployeeListing, Section, employeeComment, VideoSection, Video,Timestamp

import datetime




def index(request):
    activeEmployees = Employee.objects.filter(isActive=True)
    sections = Section.objects.all()
    return render(request, "auctions/employees.html", {
        "activeEmployees": activeEmployees,
        "sections": sections,
    })


def employees(request):
    activeEmployees = Employee.objects.filter(isActive=True)
    sections = Section.objects.all()
    return render(request, "auctions/employees.html", {
        "activeEmployees": activeEmployees,
        "sections": sections,
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


def createListing(request):
    if request.method == "GET":
        allCategories = Category.objects.all()
        return render(request, "auctions/create.html", {
            "categories": allCategories
        })
    else:
        # Get data from form
        title = request.POST["title"]
        description = request.POST["description"]

        imageURL = request.POST["imageURL"]
        price = request.POST["price"]
        category = request.POST["category"]
        # who is the user
        currentUser = request.user
        # Get all content about particular category
        categoryData = Category.objects.get(categoryName=category)
        # Create new listing
        newListing = Listing(
            title=title,
            description=description,
            imageURL=imageURL,
            price=float(price),
            category=categoryData,
            owner=currentUser
        )
def createTask(request):
    
    #Load Employees, Sections
    if request.method == "GET":
        
        #get current Year
        today = datetime.datetime.now()
        currentYear = today.year
        nextYear = currentYear+1
        currentMonth = today.month
        if currentMonth == 12:
            nextMonth = 1
        else:
            nextMonth = currentMonth + 1
        print(nextMonth)
        #import Employee and Section objects
        allEmployees = Employee.objects.filter(isActive=True)
        allSections = Section.objects.all()
        activeEmployees = Employee.objects.filter(isActive=True)
        return render(request,"auctions/createTask.html",{
            "allEmployees": allEmployees,
            "allSections": allSections,
            "currentYear": currentYear,
            "nextYear": nextYear,
            "currentMonth": currentMonth,
            "nextMonth": nextMonth,
            "rangeDays": range(1,32),
            "rangeHours": range(1,13),
            "rangeMinutes": range(0,31,30),
        })
    else:
        employeeName = request.POST["employeeName"]
        section = request.POST["section"]
        tasks = request.POST["tasks"]
        startYear = request.POST["startYear"]
        startHour = request.POST["startHour"]
        startMonth = request.POST["startMonth"]
        startDay = request.POST["startDay"]
        startMinute = request.POST["startMinute"]
        endHour = request.POST["endHour"]
        endMinute = request.POST["endMinute"]
        extras = request.POST["extras"]
        extrasPrice = request.POST["extrasPrice"]

        newEmployeeListing = EmployeeListing(
            employee = Employee.objects.get(phone=employeeName),
            section=Section.objects.get(sectionName=section),
            tasks = tasks,
            startYear = startYear,
            startMonth = startMonth,
            startDay = startDay,
            startHour = startHour,
            startMinute = startMinute,
            endHour = endHour, 
            endMinute = endMinute,
            extras = extras,
            extrasPrice = extrasPrice
        )
        newEmployeeListing.save()
        # Insert object into database
        # print(newListing)
        # print(f"my listing{newListing.title}")
        # print(f"my listing{newListing.description}")
        # print(f"my listing{newListing.imageURL}")
        # print(f"my listing{newListing.price}")
        # Redirect to index
        return HttpResponseRedirect(reverse("index"))


def activeListings(request):
    activeListings = Listing.objects.all()
    categories = Category.objects.all()

    return render(request, "auctions/active.html", {
        "activeListings": activeListings,
        "categories": categories,
    })


def categories(request):
    categories = Category.objects.all()
    return render(request, "auctions/categories.html", {
        "categories": categories,
    })


def displayCategory(request):
    if request.method == "POST":
        categoryFromForm = request.POST['category']
        category = Category.objects.get(categoryName=categoryFromForm)
        activeListings = Listing.objects.filter(
            isActive=True, category=category)
        allCategories = Category.objects.all()
        allListings = Listing.objects.all()
        # print(category)
        # print(activeListings)
        return render(request, "auctions/index.html", {
            "activeListings": activeListings,
            "categories": allCategories,
            "allListings": allListings,
        })
def displaySection(request):
    if request.method == "POST":
        sectionFromForm = request.POST['section']
        section = Section.objects.get(sectionName=sectionFromForm)
        activeEmployees = Employee.objects.filter(isActive=True, section=section)
        allSections = Section.objects.all()
        allEmployees = Employee.objects.all()
        
        return render(request, "auctions/employees.html", {
            "activeEmployees": activeEmployees,
            "sections": allSections,
            "allEmployees": allEmployees,
        })


def listing(request, id):
    if request.method == "POST":
        number = request.POST['number']
        listingData = Listing.objects.get(pk=id)
        listingData.count = number
        listingData.save()
        currentUser = request.user
        createTimestamp = Timestamp(
            author = currentUser,
            listing = Listing.objects.get(pk=id)
        )
        createTimestamp.save()
        print(listingData.count)
        print(f"{number}")
    listingData = Listing.objects.get(pk=id)
    lastTimestamp = Timestamp.objects.filter(listing=listingData).last()
    print(lastTimestamp)
    print(lastTimestamp)

    isListingInWatchlist = request.user in listingData.watchlist.all()
    comments = Comment.objects.filter(listing=listingData)
    # print(isListingInWatchlist)
    # print(f"listingData, {listingData}")
    # print(f"comments: {comments}")
    print(f"lastTimestamp: {lastTimestamp}")
    return render(request, "auctions/listing.html", {
        "listingData": listingData,
        "isListingInWatchlist": isListingInWatchlist,
        "comments": comments,
        "lastTimestamp": lastTimestamp
    })


def employeePage(request, phone):
    employee = Employee.objects.get(phone=phone)
    employeeData = Employee.objects.get(phone=phone)
    employeeTasks = EmployeeListing.objects.filter(employee=employee)
    print(f"UNORDERED {employeeTasks}")
    # employeeTasks = employeeTasks.order_by('id')[:6][::-1]
    # employeeTasks = reversed(employeeTasks)
    employeeTasks = employeeTasks.order_by('-id')[:7:1]
    # use [:5:1] for the reverse order in our case
    print(f"EMPLOYEETASKS {employeeTasks}")
    # print(f"employee Tasks REVERSED {reverseEmployeeTasks}")
    # sortedEmployeeTasks = employeeTasks.sort(key=lambda y : y.startYear)
    # print(sortedEmployeeTasks)
    comments = employeeComment.objects.filter(employee=employee)
    comments = comments.order_by('-id')[:10:1]

    return render(request, "auctions/employeePage.html", {
        "employeeData": employeeData,
         "employeeTasks": employeeTasks,
         "comments": comments,
    })


def removeWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))
    print(f"watchlist {listingData.watchlist}")


def addWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))
    print(listingData.watchlist)


def watchlist(request):
    currentUser = request.user
    categories = Category.objects.all()
    watchlist = currentUser.listingWatchlist.all()
    return render(request, "auctions/watchlist.html", {
        "watchlist": watchlist,
        "categories": categories
    })


def sortWatchlist(request):
    if request.method == "POST":
        currentUser = request.user
        categoryFromForm = request.POST['category']
        category = Category.objects.get(categoryName=categoryFromForm)
        watchlist = currentUser.listingWatchlist.all()
        sortedWatchlist = watchlist.filter(isActive=True, category=category)

        allCategories = Category.objects.all()
        print(f"sortedwatchlist_is{sortedWatchlist}")
        return render(request, "auctions/sortWatchlist.html", {
            "watchlist": watchlist,
            "categories": allCategories,
            "sortedWatchlist": sortedWatchlist
        })


def addComment(request, id):
    currentUser = request.user
    listingData = Listing.objects.get(pk=id)
    message = request.POST['newComment']
    createComment = Comment(
        author=currentUser,
        listing=listingData,
        message=message,
    )
    createComment.save()

    return HttpResponseRedirect(reverse("listing", args=(id, )))

def addEmployeeComment(request, phone):
    currentUser = request.user
    employee = Employee.objects.get(phone=phone)
    message = request.POST['newComment']
    createComment = employeeComment(
        author = currentUser,
        employee = employee,
        message = message
    )
    createComment.save()

    return HttpResponseRedirect(reverse("employeePage", args=(phone, )))


# def purchases(request):
#     listingData = Listing.objects.get(pk=id)
#     isPurchased = request.user in listingData.purchased.all()
#     ordered = False
#     return render(request, id, {
#         "ordered": ordered
#     })

def videos(request):
    videoSections = VideoSection.objects.all()
    videos = Video.objects.all()
    return render(request, "auctions/videos.html", {
    "videoSections":videoSections,
    "videos":videos,
    })

def displayVideoSection(request):
    videoSections = VideoSection.objects.all()
    if request.method == "POST":
        sections = VideoSection.objects.all()
        sectionFromForm = request.POST['videoSection']
        print(sectionFromForm)
        selectedVideoSection = VideoSection.objects.get(videoSection=sectionFromForm)
        print(selectedVideoSection)
        sortedVideos = Video.objects.filter(videoSection=selectedVideoSection)
        print(sortedVideos)
    return render(request, "auctions/displayVideoSection.html", {
    "videoSections":videoSections,
    "sortedVideos": sortedVideos,
        
    })
def uploadVideo(request):
    sections = VideoSection.objects.all()
    if request.method == "POST":
        sectionFromForm = request.POST['section']
        titleFromForm = request.POST['title']
        embedLink = request.POST['embedLink']

        createVideo = Video(VideoSection=sectionFromForm,
        videoTitle = videoTitle,
        videoLink = embedLink,
        )
        createVideo.save()
    
    return render(request, "auctions/uploadVideo.html", {
    "sections":sections,
        
    })
def dogs(request):
    return render(request, "auctions/dogs.html",{

    })