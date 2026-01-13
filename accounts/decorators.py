from django.shortcuts import redirect
from django.contrib import messages

def hr_admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if hasattr(request.user, 'userprofile'):
            role = request.user.userprofile.role
            
            if role in ['HR', 'ADMIN']:
                return view_func(request, *args, **kwargs)
            
        messages.error(request, 'You are not authorized to access this page.')
        return redirect('dashboard')
    return wrapper
        