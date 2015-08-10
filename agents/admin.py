from django.contrib import admin
from .models import Agent

class AgentAdmin(admin.ModelAdmin):
	list_display = ('fullName','id_avaya', 'id_softphone','status')
	search_fields = ('first_name', 'last_name')

admin.site.register(Agent,AgentAdmin)
