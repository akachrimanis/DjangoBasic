from django.contrib import admin
from .models import InteractionType, Interaction, InteractionDetails, TaskType, Task
admin.site.register(InteractionType)
admin.site.register(Interaction)
admin.site.register(InteractionDetails)
admin.site.register(TaskType)
admin.site.register(Task)

