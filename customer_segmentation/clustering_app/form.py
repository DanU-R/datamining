from django import forms

class ClusterForm(forms.forms):
    clusters = forms.IntegerField()