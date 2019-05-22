from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView
from django.template.loader import get_template
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


# Create your views here.
#class HomePageView(TemplateView):
    #def get(self, request, **kwargs):
        #return render(request, 'index.html', context=None)

class Home(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'base.html', context=None)

class About(TemplateView):
    template_name = "about.html"

class Gallery(TemplateView):
    template_name = "gallery.html"

class Contact(CreateView):

    def get(self,request):
        print("get")
        template_name = "contact.html"
        form=ContactForm()
        context={
            'form':form,
            }
        return render(request,template_name,context)
    def post(self,request):
        template_name = get_template("contact.html")
        form=ContactForm(request.POST)

        if form.is_valid():
            print("valid")
            first_name = request.POST.get(
                'first_name', '')
            last_name = request.POST.get(
                    'last_name', '')
            email = request.POST.get(
                        'email', '')
            phone_no = request.POST.get(
                    'phone_no', '')

            body = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone_no':phone_no

                }
            content = {"%s: %s" % (key, value) for (key, value) in body.items()}
            content = "\n".join(content)
            # content = template_name.render(context)

            send_mail(
                "New contact form submission",
                content,
                settings.DEFAULT_FROM_EMAIL,
                ['pmshettar@gmail.com'],fail_silently=False)

            return redirect('/')
        else:
            print("invalid")
            context={
                'form':form,
                }
            return render(request,template_name,context)
