from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from django.contrib import messages


class IndexView(TemplateView):
    # queryset = CommandExecution.objects.all()
    template_name = "index.html"
    print("HHII")
    pass

class AboutView(TemplateView):
    # queryset = CommandExecution.objects.all()
    template_name = "about.html"
    print("about")
    pass

class ContactView(FormView):
    # queryset = CommandExecution.objects.all()
    template_name = "email.html"
    form_class = ContactForm
    success_url = '/thanks/'
    # success_message = "Thank You"
    print("about in email.html")

    def post(self,request):
        print("HELLO")
        if request.method == 'POST':
            print("1111")
            form = ContactForm(request.POST)
            if form.is_valid():
                print("3333")
                subject = form.cleaned_data['subject']
                from_email = form.cleaned_data['from_email']
                message = form.cleaned_data['message']
                try:
                    # send_mail(subject, message, from_email, ['madhurprem1@gmail.com'])
                    # return HttpResponse('/thanks/')
                    messages.success(request, 'Email Sent Successfully', extra_tags='alert')
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
        else:        
            form = ContactForm()
        context_data = {'form': form} 
        print("222222")           
                # return redirect('success')

        return render(request, "success.html", context_data)

    # def success(request):
    #     return HttpResponse('Success! Thank you for your message.')

    # def signup(request):
    #     if request.method == 'POST':
    #         form = SignUpForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             username = form.cleaned_data.get('username')
    #             raw_password = form.cleaned_data.get('password1')
    #             user = authenticate(username=username, password=raw_password)
    #             login(request, user)
    #             return redirect('login')
    #     else:
    #         form = SignUpForm()
    #     return render(request, 'sign_up.html', {'form': form})

    # def password_reset_done(request):
    #     return render(request, 'password_reset_done.html')
    # pass
