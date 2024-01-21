from django.shortcuts import render
from django.views import View

class SelectMethodView(View):
    template_name = 'select_method.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

