from django.shortcuts import render
from django.utils import timezone
from .models import Log
from django.http import HttpResponseRedirect
from login_reg_app.models import User

def tally(request):
    if "user_id" not in request.session:
        return redirect('/')
    else:
        context={
             'all_tasks':Log.objects.all(),
             'this_user':User.objects.get(id=request.session["user_id"])
        }
    return render(request, 'tasks/checklist.html',context)

def create_tally(request):
    user = User.objects.get(id=request.session["user_id"])
    current_date= timezone.now()
    new_item=Log.objects.create(title=request.POST["title"], 
    creator=user, complete=False, created_at=current_date)
    new_item.save()
    return HttpResponseRedirect('/tally')
def delete_tally(request, tally_id ):
    item = Log.objects.get(id=tally_id)
    item.delete()

    return HttpResponseRedirect('/tally')
