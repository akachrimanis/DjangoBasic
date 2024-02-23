from django.contrib import admin
from .models import Employee, Individual, Organization, Manager, Employer
admin.site.register(Employee)
admin.site.register(Individual)
admin.site.register(Organization)
admin.site.register(Manager)
admin.site.register(Employer)

