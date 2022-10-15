from django.shortcuts import render

def sgpa(request):
    return render(request,'sgpa/sgpa.html')

def sgpaselect(request,sem):
    context = {
        'sem':sem
    }
    if sem == 1:
        sem12phy = ['18MAT11/21','18PHY12/22','18ELE13/23','18CIV14/24','18EGDL15/25','18PHYL16/26','18PHYL16/26','18ELEL17/27','18EGH18/28(ENGLISH)']
        gradepoints = [4,4,3,3,3,1,1,1]
        context ={
            'subs': sem12phy,
        }
    return render(request,'sgpa/sgpasem.html',context)
    
