from django.contrib import admin
from eventex.core.models import Speaker, Contact, Talk

# Register your models here.

class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1

class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug', 'email', 'phone']

    def email(self, obj):
        return obj.contact_set(manager='emails').first()

    email.short_description = 'e-mail'

    def phone(self, obj):
        return Contact.phones.filter(speaker=obj).first()

    phone.short_description = 'telefone'


admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk)

