from rectpatchantennapp.models import OptimizerModel
from django import forms

class OptimizerForm(forms.ModelForm):

    class Meta:
        model = OptimizerModel
        fields = "__all__"
        #fields = ("frequency", "length_of_patch", "width_of_patch",
        #           "slot_length", "slot_width")


