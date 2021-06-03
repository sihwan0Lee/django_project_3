from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch


# @method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'home.html'

    # def get_context_data(self, **kwargs):
    #context = super(HomeView, self).get_context_data(**kwargs)

    #user = self.request.user
