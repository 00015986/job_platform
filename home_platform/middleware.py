
from django.shortcuts import redirect

class RoleBasedRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if hasattr(request.user, 'profile'):
                if request.user.profile.role == 'recruiter':
                    return redirect('recruiter_dashboard')
                elif request.user.profile.role == 'applicant':
                    return redirect('applicant_dashboard')
        return self.get_response(request)

