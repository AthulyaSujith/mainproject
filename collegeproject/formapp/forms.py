from django import forms
from .models import Department, Course

class mform(forms.Form):
    class Meta:
        model = Course
        fields = ['name', 'department']
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    MATERIALS_CHOICES = [
        ('notebook', 'Notebook'),
        ('pen', 'Pen'),
        ('exampaper', 'Exam Paper'),
        ('other', 'Other'),
        ('None', 'None')
    ]
    name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    #department_choices = [(department.id, department.name) for department in Department.objects.all()]
    #department = forms.ChoiceField(choices=department_choices)
    #department= forms.ModelChoiceField(queryset=Department.objects.all())
    #department = forms.ModelChoiceField(queryset=Department.objects.all())
    #name = forms.CharField(max_length=50)
    #course = forms.CharField(max_length=100)
    #course = forms.ModelChoiceField(queryset=Course.objects.none())
    purpose = forms.ChoiceField(choices=[('ENQ', 'Enquiry'), ('ORD', 'Place Order'), ('RET', 'Return'),('AD', 'Admission'),('Tour', 'Campus Tour'),])
    materials_provides = forms.MultipleChoiceField(
        choices=MATERIALS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )
    department_choices = (('N', '---'), ('Li', 'Literature'),('ARTS', 'ARTS'), ('SE', 'Social Science'),('CSE', 'Computer Science'), ('CC', 'Commerce'),('S', 'Science'))
    course_choices = (
        ('IT1', 'Computer Security'), ('IT2', 'Cloud computing'), ('IT3', 'System Administration'),('IT4', 'Cryptograpy'),('IT5', 'Cyber Securiry'),
        ('LI1', 'Modern Literature'),  ('LI2', 'Grammar'),  ('LI3', 'Journalism'),  ('LI4', 'medieval'),  ('LI5', 'Folklore'),
        ('Arts1', 'English'),  ('Arts2', 'Malayalam'),  ('Arts3', 'Hindi'),  ('Arts4', 'Homescience'),  ('Arts5', 'Finearts'),
        ('SE1', 'History'),  ('SE2', 'Geography'),  ('SE3', 'Anthropology'),  ('SE4', 'Political Science'),  ('SE5', 'Psycology'),
        ('CC1', 'Banking'), ('CC2', 'BA'), ('CC3', 'BBA'), ('CC4', 'CA'), ('CC5', 'BCOM'),
        ('S1', 'Physics'), ('S2', 'Chemistry'), ('S3', 'Zoology'), ('S4', 'Botony'), ('S5', 'MicroBiology'),
        ('N1', '---')
                      )
    department = forms.ChoiceField(choices=department_choices, widget=forms.Select(attrs={'id': 'department'}))
    course = forms.ChoiceField(choices=course_choices, widget=forms.Select(attrs={'id': 'course'}))



''' def __init__(self, *args, **kwargs):
        self.instance = kwargs.get('instance', None)  # set instance attribute if it exists in kwargs
        super().__init__(*args, **kwargs)
        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty course queryset
        elif self.instance and self.instance.pk:  # check if instance attribute exists and has a pk value
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')

    def clean(self):
        cleaned_data = super().clean()
        department = cleaned_data.get('department')
        course = cleaned_data.get('course')

        if department and course and course.department != department:
            raise forms.ValidationError("Selected course doesn't belong to the selected department.")

        return cleaned_data'''




