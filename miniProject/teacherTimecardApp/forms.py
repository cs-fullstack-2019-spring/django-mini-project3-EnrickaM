from django import forms
from .models import TimeCard

class TimeCardForm(forms.ModelForm):
    class Meta:
        model=TimeCard
        fields=['teacherName','school','subject','hours','dateofWork','dateofEntry']