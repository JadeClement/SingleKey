from django.shortcuts import render
 
import json
from django.http import JsonResponse
import os

# Create your views here.

def home(request):
    submissions = load_submissions()
    context = {'submissions': submissions}
    return render(request, 'home.html',context)  

def thanks(request):
    if request.method == 'POST':
        # Load existing submissions from your storage (e.g., JSON file, database, etc.)
        submissions = load_submissions()

        # Add new submission
        submissions.append({
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'status': 'Submitted'
        })

        # Save back to storage
        save_submissions(submissions)

    return render(request, 'thanks.html') 

def login(request):
    return render(request,"login.html")

def call(request):
    return render(request,"call.html")

def start(request):
    return render(request,"start.html")

# Path to the JSON file - this should be an absolute path in production
SUBMISSIONS_FILE = 'submissions.json'

def load_submissions():
    # Load submissions from a JSON file
    if not os.path.isfile(SUBMISSIONS_FILE):
        # If the file does not exist, create it with initial submissions
        initial_submissions = [
            {'name': 'John Doe', 'email': 'john@example.com', 'status': 'Submitted'},
            {'name': 'Jane Smith', 'email': 'jane@example.com', 'status': 'Submitted'}
        ]
        with open(SUBMISSIONS_FILE, 'w') as file:
            json.dump(initial_submissions, file)
        return initial_submissions
    
    # If the file exists, load its content
    with open(SUBMISSIONS_FILE, 'r') as file:
        submissions = json.load(file)
    return submissions

def save_submissions(submissions):
    # Save submissions to a JSON file
    with open('submissions.json', 'w') as file:
        json.dump(submissions, file)



def index(request):
    if request.method == 'POST':
        # Load existing submissions
        submissions = load_submissions()

        # Add new submission
        submissions.append({
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'status': 'Submitted'
        })

        # Save back to file
        save_submissions(submissions)

        # Redirect or respond as necessary
        return JsonResponse({'status': 'success'})

    # Load submissions for display
    context = {'submissions': load_submissions()}
    return render(request, 'index.html', context)

'''
def index(request):
  if request.POST:
    context = {
      'name': request.POST['name'],
      'email': request.POST['email'],
    }
    return render(request, 'thanks.html', context)
  context = {
    'results': [
      {'name': 'Fatima Lopez', 'email': 'f.lopez@email.com'},
      {'name': 'Gary Johnston', 'email': 'g.johnston@email.com'}
    ]
  }
  
  return render(request, 'index.html', context)
'''