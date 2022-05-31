from django import forms
from django.forms import ModelForm
from .models import TaskItem
 
class DateInput(forms.DateInput):
    input_type = 'date'

class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class TaskItemForm(forms.ModelForm):
    class Meta:
        model = TaskItem
        fields = fields = [
            "todo_list",
            "title", 
            "description",
            "title",
            "due_date",
        ]
        widgets = {
            'due_date': DateInput(),
        }