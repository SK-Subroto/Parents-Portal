from django import forms
from .models import Behaviour_assess

CLASS_ATTENTION_CHOICES = (
    (-1,'Below Average'),
    (-2, 'Average'),
    (0, 'Good'),
    (1, 'Very Good'),
    (2, 'Execellet'),
)

BEHAVE_TEACHER_CHOICES = (
    (-1,'Below Average'),
    (-2, 'Average'),
    (0, 'Good'),
    (1, 'Very Good'),
    (2, 'Execellet'),
)

BEHAVE_STUDENT_CHOICES = (
    (-1,'Below Average'),
    (-2, 'Average'),
    (0, 'Good'),
    (1, 'Very Good'),
    (2, 'Execellet'),
)

CLASS_ATTEND_CHOICES = (
    (-1,'Below Average'),
    (-2, 'Average'),
    (0, 'Good'),
    (1, 'Very Good'),
    (2, 'Execellet'),
)

CLASS_PERFORMANCE_CHOICES = (
    (-1,'Below Average'),
    (-2, 'Average'),
    (0, 'Good'),
    (1, 'Very Good'),
    (2, 'Execellet'),
)

class RawBehaveAssessForm(forms.ModelForm):
    classAttention = forms.ChoiceField(choices=CLASS_ATTENTION_CHOICES, widget=forms.RadioSelect(), label="Class Attention")
    behaveTeacher = forms.ChoiceField(choices=BEHAVE_TEACHER_CHOICES, widget=forms.RadioSelect(), label="Behave with Teacher")
    behaveStudent = forms.ChoiceField(choices=BEHAVE_STUDENT_CHOICES, widget=forms.RadioSelect(), label="Behave with Classmate")
    attenClass = forms.ChoiceField(choices=CLASS_ATTEND_CHOICES, widget=forms.RadioSelect(), label="Class Attendent")
    performance = forms.ChoiceField(choices=CLASS_PERFORMANCE_CHOICES, widget=forms.RadioSelect(), label="Class Performance")

    class Meta:
        model = Behaviour_assess
        fields = ['classAttention', 'behaveTeacher', 'behaveStudent', 'attenClass', 'performance',]