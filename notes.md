Anomaly Detector/
└── backend/
    ├── manage.py
    ├── monitoring/     # Django project folder (settings, urls, etc.)
    └── metrics/        # Django app folder (your code for metrics)




#What is Request
🔍 What does request contain?
It's an instance of django.http.HttpRequest, and it carries all the information about the incoming HTTP request, including:

Attribute	  | What it holds
request.method	'GET', 'POST', etc.
request.GET 	Query parameters like ?search=abc
request.POST	Data from form submissions
request.body	Raw request body (JSON, etc.)
request.headers	HTTP headers
request.user	Authenticated user (if any)🔍 What does request contain?

It is passed automatically in http usecases.
