# profesor/decorators.py

from django.shortcuts import redirect

def profesor_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'profesor_id' not in request.session:
            return redirect('login_p')
        return view_func(request, *args, **kwargs)
    return wrapper