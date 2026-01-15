from django import forms
import requests

class ShorterUrlForm(forms.Form):
    url = forms.URLField(required=True)

    # def clean_url(self):
    #     try:
    #         if requests.get(self.cleaned_data['url']).status_code != 200:
    #             raise forms.ValidationError("l'URL n'est pas valide !")
    #     except:
    #         raise forms.ValidationError("l'URL n'est pas valide !")
