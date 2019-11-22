from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"
      def get_context_data(self):
        data = {
            "message_title" : "Hi", "message_title"  : "Hello!"
            
        }
        return data
