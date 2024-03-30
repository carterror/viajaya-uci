from django import forms
from reservas.models.viajero import Viajero
from django.utils.html import format_html
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe

class CustomCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option_attrs = self.option_attrs(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        if 'id' in option_attrs:
            option_attrs['id'] = option_attrs['id'].replace('_', '-')
        return super().create_option(name, value, label, selected, index, subindex=subindex, attrs=option_attrs)

    def render(self, name, value, attrs=None, renderer=None):
        # Genera el HTML para cada opción del checkbox
        output = []
        for i, choice in enumerate(self.choices):
            choice_value, choice_label = choice
            if isinstance(choice_label, (tuple, list)):
                attrs = choice_label[1]
                choice_label = choice_label[0]
            else:
                attrs = {}

            # Genera el input y el label para cada opción
            input_attrs = self.attrs.copy()
            input_attrs.update(attrs)
            input_attrs['type'] = self.input_type
            input_attrs['name'] = name
            input_attrs['value'] = choice_value
            input_attrs['id'] = f"{name}-{i}"
            input_attrs['class'] = 'btn-check w-100'
            input_attrs['autocomplete'] = 'off'

            if value and choice_value in value:
                input_attrs['checked'] = 'checked'

            input_html = f'<input {flatatt(input_attrs)}>'

            label_attrs = {'class': 'btn btn-outline-primary w-100 mb-3', 'for': input_attrs['id']}
            label_html = f'<label {flatatt(label_attrs)}>{choice_label}</label>'

            output.append(f'{input_html}{label_html}<br>')

        return mark_safe('\n'.join(output))

class ViajerosForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ViajerosForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['viajeros'].queryset = Viajero.objects.filter(user=user)
        else:
            self.fields['viajeros'].queryset = Viajero.objects.none()

    viajeros = forms.ModelMultipleChoiceField(queryset=Viajero.objects.none(),
                                              widget=CustomCheckboxSelectMultiple(
                                                                                    attrs={'class': 'btn-check my-2'}
                                                                                ),
                                              label='')
    
    def clean(self):
        cleaned_data = super().clean()
        viajeros_seleccionados = cleaned_data.get('viajeros')

        if viajeros_seleccionados and len(viajeros_seleccionados) > 4:
            raise ValidationError("No puedes seleccionar más de 4 viajeros.")

        return cleaned_data