from django.shortcuts import render

# Create your views here.
import os
import joblib




def predict_insurance(request):
    if request.method=="POST":
        
        age = float(request.POST["age"])
        bmi= float(request.POST["bmi"])
        sex= float(request.POST["sex"])
        children= float(request.POST["children"])
        smoker= float(request.POST["smoker"])
        region= float(request.POST["region"])
        file_path=os.path.join(os.path.dirname(__file__),"insurance_model.pkl")
        model=joblib.load(file_path)
        predicted_insurance= model.predict([[age,bmi,sex,children,smoker,region]])
        context={"predicted_insurance": predicted_insurance[0]}

        return render(request,'result.html',context)
    
    return render(request,'index.html')