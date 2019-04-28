from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request,"layout/home.html")

@login_required
def resume(request):
    """Display Applicant Resume"""
    resume = request.user.applicant.resume
    return render(request, 'accounts/resume.html', {
        'resume': resume
    })


@login_required
def edit_resume(request):
    user = request.user
    resume = get_object_or_404(models.Resume, user=user)
    form = forms.ProfileForm(instance=profile)

    if request.method == 'POST':
        form = forms.RseumeForm(instance=resume, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated the Resume Successfully!")
            return HttpResponseRedirect(reverse('accounts:resume'))

    return render(request, 'accounts/edit_resume.html', {
        'form': form
    })
