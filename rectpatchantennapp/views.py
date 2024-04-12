from django.shortcuts import render
from rectpatchantennapp.forms import OptimizerForm
import joblib
# Create your views here.


def RandomForest(request): 
    if request.method == "POST":
        optimizer = OptimizerForm(request.POST)
        if optimizer.is_valid():
            optimizer.save()
            model = joblib.load("./rectangular_patch_antenna.pkl")
            col_names = joblib.load("./rpa_col_names.pkl")
            prediction =model.predict([[optimizer.cleaned_data.get("frequency"),
                                       optimizer.cleaned_data.get("length_of_patch"),
                                       optimizer.cleaned_data.get("width_of_patch"),
                                       optimizer.cleaned_data.get("slot_length"),
                                       optimizer.cleaned_data.get("slot_width")]])
            

            return render(request, "rectpatchantennapp/Optimizer.html", {"form": optimizer, "prediction": round(prediction[0], ndigits=4)})
    else:
        optimizer = OptimizerForm()
        return render(request, "rectpatchantennapp/Optimizer.html", {"form": optimizer})