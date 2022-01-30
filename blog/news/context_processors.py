from .models import *

def get_navbar(request):
    return {'navbar_list': Navbar.objects.filter(posted=True).order_by('position')}