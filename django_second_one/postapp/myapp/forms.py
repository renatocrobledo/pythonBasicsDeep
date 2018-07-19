from django import forms

class EntryForm(forms.Form):
  title = forms.CharField(max_length=100)
  date = forms.DateTimeField(widget=forms.DateInput(attrs= {'type': 'date'} ))
  content = forms.CharField(widget=forms.Textarea)