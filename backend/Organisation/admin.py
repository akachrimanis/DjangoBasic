from django.contrib import admin
from .models import Employee, Individual, Organisation, Manager, Employer
admin.site.register(Employee)
admin.site.register(Individual)
admin.site.register(Organisation)
admin.site.register(Manager)
admin.site.register(Employer)

