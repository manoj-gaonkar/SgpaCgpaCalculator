from django.shortcuts import render

def sgpa(request):
    return render(request,'sgpa/sgpa.html')

def sgpaselect(request,sem):
    context = {
        'sem':sem
    }
    
    if sem == 11:
        sem12phy = ['18MAT11/21','18PHY12/22','18ELE13/23','18CIV14/24','18EGDL15/25','18PHYL16/26','18ELEL17/27','18EGH18/28(ENGLISH)']
        gradepoints = [4,4,3,3,3,1,1,1]
        sumgradepoints = sum(gradepoints)
        context['subs'] = sem12phy
        total = 0
        if request.method == "POST":
            submarks = request.POST.getlist('marks')
            for i in range(len(submarks)):
                if int(submarks[i])<=35:
                    gradepoints[i]=0
            for i in range(len(sem12phy)):
                submarks[i] = (int(submarks[i])//10)+1
                total += int(submarks[i])*int(gradepoints[i])
            sgpa = total/sumgradepoints
            context = {
                'sgpa':sgpa,
                'percentage': (sgpa-0.75)*10,
            }
            return render(request,'sgpa/result.html',context)
    elif sem == 12:
        sem12chem = ['18MAT11/21','18CHE12/22','18CPS13/23','18ELN14/24','18ME15/25','18CHEL16/26','18CPL17/27','18EGH18/28(ENGLISH)']
        gradepoints = [4,4,3,3,3,1,1,1]
        context['subs'] = sem12chem
        total = 0
        if request.method == "POST":
            submarks = request.POST.getlist('marks')
            for i in range(len(sem12chem)):
                submarks[i] = (int(submarks[i])//10)+1
                total += int(submarks[i])*int(gradepoints[i])
            sgpa = total/sum(gradepoints)
            context = {
                'sgpa':sgpa,
                'percentage': (sgpa-0.75)*10,
            }
            return render(request,'sgpa/result.html',context)
    elif sem == 3:
        sem3 = ['18MAT31','18XX32','18XX33','18XX34','18XX35','18XX36','18XXL37','18XXL38','18CPC39/49 or Kannada']
        gradepoints = [3,4,3,3,3,3,2,2,1]
        context['subs'] = sem3
        total = 0
        if request.method == "POST":
            submarks = request.POST.getlist('marks')
            for i in range(len(sem3)):
                submarks[i] = (int(submarks[i])//10)+1
                total += int(submarks[i])*int(gradepoints[i])
            sgpa = total/sum(gradepoints)
            context = {
                'sgpa':sgpa,
                'percentage': (sgpa-0.75)*10,
            }
            return render(request,'sgpa/result.html',context)
    elif sem == 4:
        sem4 = ['18MAT41','18XX42','18XX43','18XX44','18XX45','18XX46','18XXL47','18XXL48','18CPC39/49 or Kannada']
        gradepoints = [3,4,3,3,3,3,2,2,1]
        context['subs'] = sem4
        total = 0
        if request.method == "POST":
            submarks = request.POST.getlist('marks')
            for i in range(len(sem4)):
                submarks[i] = (int(submarks[i])//10)+1
                total += int(submarks[i])*int(gradepoints[i])
            sgpa = total/sum(gradepoints)
            context = {
                'sgpa':sgpa,
                'percentage': (sgpa-0.75)*10,
            }
            return render(request,'sgpa/result.html',context)
    elif sem == 5:
        sem5 = ['18XX51','18XX52','18XX53','18XX54','18XX55','18XX56','18XXL57','18XXL58','Enviromental Studies']
        gradepoints = [3,4,4,3,3,3,2,2,1]
        context['subs'] = sem5
        total = 0
        if request.method == "POST":
            submarks = request.POST.getlist('marks')
            for i in range(len(sem5)):
                submarks[i] = (int(submarks[i])//10)+1
                total += int(submarks[i])*int(gradepoints[i])
            sgpa = total/sum(gradepoints)
            context = {
                'sgpa':sgpa,
                'percentage': (sgpa-0.75)*10,
            }
            return render(request,'sgpa/result.html',context)
    elif sem == 6:
        sem6 = ['18XX61','18XX62','18XX63','18XX64X','18XX65X','18XXL66 Lab','18XXL67 Lab','18XXMP68 Mini Project']
        gradepoints = [4,4,4,3,3,2,2,2]
        context['subs'] = sem6
        total = 0
        if request.method == "POST":
            submarks = request.POST.getlist('marks')
            for i in range(len(sem6)):
                submarks[i] = (int(submarks[i])//10)+1
                total += int(submarks[i])*int(gradepoints[i])
            sgpa = total/sum(gradepoints)
            context = {
                'sgpa':sgpa,
                'percentage': (sgpa-0.75)*10,
            }
            return render(request,'sgpa/result.html',context)
    elif sem == 71:
        sem71 = ['18CS71','18CS72','18CS73X','18CS74X','18CS75X','18CSL76 Lab','18CSP77 Project Phase 1']
        gradepoints = [4,4,3,3,3,2,1]
        context['subs'] = sem71
        total = 0
        if request.method == "POST":
            submarks = request.POST.getlist('marks')
            for i in range(len(sem71)):
                submarks[i] = (int(submarks[i])//10)+1
                total += int(submarks[i])*int(gradepoints[i])
            sgpa = total/sum(gradepoints)
            context = {
                'sgpa':sgpa,
                'percentage': (sgpa-0.75)*10,
            }
            return render(request,'sgpa/result.html',context)
    elif sem == 72:
        sem72 = ['18XX71','18XX72','18XX73X','18XX74X','18XX75X','18XXL76 Lab','18XXL77 Lab','18XXP78 Project Phase 1']
        gradepoints = [4,4,4,3,3,2,2,2,2]
        context['subs'] = sem72
        total = 0
        if request.method == "POST":
            submarks = request.POST.getlist('marks')
            for i in range(len(sem72)):
                submarks[i] = (int(submarks[i])//10)+1
                total += int(submarks[i])*int(gradepoints[i])
            sgpa = total/sum(gradepoints)
            context = {
                'sgpa':sgpa,
                'percentage': (sgpa-0.75)*10,
            }
            return render(request,'sgpa/result.html',context)
    elif sem == 8:
        sem8 = ['18XX81','18XX82X','18XXP83','18XXS84','18XX185 Intership']
        gradepoints = [3,3,8,1,3]
        context['subs'] = sem8
        total = 0
        if request.method == "POST":
            submarks = request.POST.getlist('marks')
            for i in range(len(sem8)):
                submarks[i] = (int(submarks[i])//10)+1
                total += int(submarks[i])*int(gradepoints[i])
            sgpa = total/sum(gradepoints)
            context = {
                'sgpa':sgpa,
                'percentage': (sgpa-0.75)*10,
            }
            return render(request,'sgpa/result.html',context)
        


    return render(request,'sgpa/sgpasem.html',context)

def csec(request,sem):
    return render(request,'sgpa/sem7.html')

    
