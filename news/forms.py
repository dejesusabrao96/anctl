from django import forms
from froala_editor.widgets import FroalaEditor
# from ckeditor.fields import RichTextField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from .models import *


class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['title','excerpt','content','image','category']
        exclude = ['created','updated','hashed']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0'),
                Column('excerpt', css_class='form-group col-md-6 mb-0'),
                Column('content', css_class='form-group col-md-12 mb-0'),

                # Column('published', css_class='form-group col-md-6 mb-0'), 
                # Column('image', css_class='form-group col-md-6 mb-0'), 
                Column('category', css_class='form-group col-md-6 mb-0'), 
                # Column('author', css_class='form-group col-md-6 mb-0'), 
                # Column('tags', css_class='form-group col-md-6 mb-0'), 
                # Column('created', css_class='form-group col-md-6 mb-0'), 
                # Column('updated', css_class='form-group col-md-6 mb-0'), 

                Column('image', css_class='form-group col-md-6 mb-0', onchange="myFunction()"),
                ),
            
            HTML(""" <center> <img id='output' width='200' /> </center> """),
            HTML(
                """ <div class="text-left mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Save"><span class="btn-label"><i class='fa fa-save'></i></span> Save</button>"""),
            HTML(
                """  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
        )