from django.shortcuts import render, redirect
from django.contrib import messages

def cgpa(request):
    sgpa = [0]*8
    assigngradepoints = [20,20,24,24,25,24,20,18]
    gradepoints = [0]*8
    gradetotal = 0
    avg = []
    if request.method == "POST":
        sgpa[0] = float(request.POST['s1'])
        sgpa[1] = float(request.POST['s2'])
        sgpa[2] = float(request.POST['s3'])
        sgpa[3] = float(request.POST['s4'])
        sgpa[4] = float(request.POST['s5'])
        sgpa[5] = float(request.POST['s6'])
        sgpa[6] = float(request.POST['s7'])
        sgpa[7] = float(request.POST['s8'])
        # for i in range(8):
        #     if i%2!=0:

        if sgpa[0]==0:
            return redirect('cgpa')
        for i in range(8):
            if sgpa[i]!=0:
                gradepoints[i]=assigngradepoints[i]
        for i in range(8):
            gradetotal += gradepoints[i]*sgpa[i]
        cgpa = gradetotal/sum(gradepoints)
        print(cgpa)
        percentage = (cgpa-0.75)*10
        context = {
            'cgpa':cgpa,
            'percentage':percentage,
        }
        return render(request,'cgpa/result.html',context)
    else:
        pass

    return render(request,'cgpa/cgpa.html')

def result(request):
    return render(request,'cgpa/result.html')