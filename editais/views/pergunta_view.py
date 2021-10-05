from django.views.generic import CreateView,UpdateView
from editais.forms.form_pergunta import PerguntaForm, Formset_PergAlter
from django.shortcuts import redirect
from editais.models import Edital,Pergunta


class CriarPerguntaView(CreateView):
    form_class=PerguntaForm
    template_name='pergunta/form_pergunta.html'

    def get_context_data(self, **kwargs):
         context = super(CriarPerguntaView,self).get_context_data(**kwargs)
         context['edital'] = Edital.objects.get(pk=self.kwargs['pk'])
         pergunta=Pergunta()
         pergunta.edital=context['edital']

         if self.request.POST:
            context['formset'] = Formset_PergAlter(self.request.POST , instance=pergunta)
         else:
            context['formset'] = Formset_PergAlter(instance=pergunta)
         return context

    def form_valid(self, form):
        context =self.get_context_data()
        formset=context['formset']

        if formset.is_valid():
            form.instance.edital = context['edital']
            self.object=form.save()
            formset.instance=self.object
            formset.save()
            return redirect('editais:listar_editais')

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form,formset=formset))
    

class EditarPerguntaView(UpdateView):
    model=Pergunta
    form_class=PerguntaForm
    template_name='pergunta/form_pergunta.html'

    def get_context_data(self, **kwargs):
         context = super(EditarPerguntaView,self).get_context_data(**kwargs)
         context['edital']=self.object.edital
         if self.request.POST:
             
            context['formset'] = Formset_PergAlter(self.request.POST or None , instance=self.object)
         else:
            context['formset'] = Formset_PergAlter(instance=self.object)
         return context

    def form_valid(self, form):
        context =self.get_context_data()
        formset=context['formset']

        if formset.is_valid():
            self.object=form.save()
            formset.instance =self.object
            formset.save()
            formset.instance=self.object
            formset.save()
            return redirect('editais:listar_editais')

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form,formset=formset))
    
    




