from datetime import date
from django.core.exceptions import ValidationError

from django import forms
from .models import Feedback, Connection


class feedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields=('name','email','feedback')


class flightsearchform(forms.Form):
    flights = Connection.objects.order_by('date')
    origins = set()
    destinition = set()
    for flight in flights:
        origins.add(flight.place_of_origin)
        destinition.add(flight.place_of_destination)
    flight_from_choice = [(c, c)for c in origins]
    flight_to_choice = [(c, c) for c in destinition]
    numbers_choice = [(n, n) for n in range(21)]
    origins = forms.ChoiceField(label='From:',choices=flight_from_choice,widget=forms.Select(attrs={'onchange':'updateDestinitions();'}))
    destinition = forms .ChoiceField(label='To:',choices=flight_to_choice)
    one_way = forms.BooleanField(required=False,label='OneWay',widget=forms.CheckboxInput(attrs={'onclick':'validate();'}))
    depart_date = forms.DateField(label='Date of departure',initial=date.today(), widget=forms.SelectDateWidget())
    return_date = forms.DateField(required=False,label="date of return",initial=date.today(),widget=forms.SelectDateWidget())
    adult_ticket = forms.ChoiceField(label='Adult',choices=numbers_choice[1:])
    child_ticket = forms.ChoiceField(label='Children[2-16years]',choices=numbers_choice)
    infant_ticket = forms.ChoiceField(label='Infant[0-2years]',choices=numbers_choice)

    def clean(self):
        flights = Connection.objects.order_by('date')
        cleaned_data = self.cleaned_data
        if not cleaned_data['one_way']and cleaned_data['return_date']<cleaned_data['depart_date']:
            raise Validationerror("Return date cannot be before selected flight.")