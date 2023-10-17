# from django import forms

# class ClusterForm(forms.forms):
#     clusters = forms.IntegerField()

from django import forms

class ClusterForm(forms.Form):
    clusters = forms.IntegerField()