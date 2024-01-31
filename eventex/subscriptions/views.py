from django.shortcuts import render, resolve_url as r
from eventex.subscriptions.forms import SubscriptionForm
from django.template.loader import render_to_string
from django.core import mail
from django.http import HttpResponseRedirect, Http404


from eventex.subscriptions.models import Subscription


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def create(request):
        form = SubscriptionForm(request.POST)

        if not form.is_valid():
            return render(request, 'subscriptions/subscription_form.html',
                          {'form': form})

        # Armazena os dados do usuário no banco de dados
        subscription = Subscription.objects.create(**form.cleaned_data)
        """
        !!! Pode ser utilizado caso seja Model Form !!!
        subscription = form.save()
        """

        return HttpResponseRedirect(r('subscriptions:detail', subscription.pk))


def empty_form(request):
        return render(request, 'subscriptions/subscription_form.html',
                      {'form': SubscriptionForm()})


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404


    return render(request, 'subscriptions/subscription_detail.html',
                  {'subscription': subscription})
