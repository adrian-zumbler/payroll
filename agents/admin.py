from django.contrib import admin
from .models import Agent

class AgentAdmin(admin.ModelAdmin):
	pass

admin.site.register(Agent,AgentAdmin)
