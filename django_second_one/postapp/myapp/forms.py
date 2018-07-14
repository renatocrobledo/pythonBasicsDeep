from django import forms

class EntryForm(forms.Form):
  title = forms.CharField(max_length=100)
  date = forms.DateTimeField()
  content = forms.CharField(widget=forms.Textarea)