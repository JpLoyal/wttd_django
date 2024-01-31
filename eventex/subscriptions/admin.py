from django.contrib import admin, messages
from eventex.subscriptions.models import Subscription
from django.utils.timezone import now
from django.utils.translation import ngettext


## Model Admin ##
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'email', 'phone', 'created_at',
                    'subscribed_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at')
    list_filter = ['paid', 'created_at']

    actions = ["marcar_como_pago"]

    def subscribed_today(self, obj):
        return obj.created_at == now().date()

    subscribed_today.short_description = 'inscrito hoje?'
    subscribed_today.boolean = True

    ## action ##
    def marcar_como_pago(self, request, queryset):
        updated = queryset.update(paid=True)
        self.message_user(
            request,
            ngettext(
                "%d Inscrito foi marcado como pago.",
                "%d Inscritos foram marcados como pago.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )


admin.site.register(Subscription, SubscriptionAdmin)