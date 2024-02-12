def create_urls(df, model_name):
    df = df.astype(str)

    # Starting script
    urls_content = f"""from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import {model_name.capitalize()}ViewSet\n

router = DefaultRouter()
router.register(r'{model_name.lower()}s', {model_name.capitalize()}ViewSet)

urlpatterns = [
    path('api/1/', include(router.urls)),
]


# GET /api/1/customers/: List all customers.
# POST /api/1/customers/: Create a new customer.
# GET /api/1/customers/<id>/: Retrieve a customer by ID.
# PUT /api/1/customers/<id>/: Update a customer by ID.
# PATCH /api/1/customers/<id>/: Partially update a customer by ID.
# DELETE /api/1/customers/<id>/: Delete a customer by ID.
"""
    return urls_content