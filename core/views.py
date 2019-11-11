from django.views.generic import TemplateView


class PageOneView(TemplateView):
	template_name = 'page-1.html'


class PageTwoView(TemplateView):
	template_name = 'page-2.html'

