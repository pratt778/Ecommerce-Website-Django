from django.shortcuts import redirect


def redirect_authenticated_users(views):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return views(request,*args,**kwargs)
    return wrapper_func