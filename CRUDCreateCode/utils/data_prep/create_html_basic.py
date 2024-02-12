def create_list_html(df, model_name):
    df = df.astype(str)
    # Starting script
   
    html_content = f"""
    {{% extends 'base.html' %}} 
    {{% block content %}}  \n
    <h2>{model_name} List</h2>
<a href="{{%  url '{model_name.lower()}_create' %}} ">Create New {model_name.capitalize()} </a>
<ul>
    {{%  for {model_name.lower()} in {model_name.lower()}s %}} 
    <li>
        {{{{ {model_name.lower()}.name }}}} ({{{{ {model_name.lower()}.email }}}} )
        <a href="{{%  url '{model_name.lower()}_update' {model_name.lower()}.id %}} ">Edit</a>
        <a href="{{% url '{model_name.lower()}_delete' {model_name.lower()}.id %}} ">Delete</a>
    </li>
    {{%  endfor %}} 
</ul>
{{% endblock %}} 

"""
    return html_content

def create_create_html(df, model_name):
    df = df.astype(str)
    # Starting script
    
    html_content = f"""
    {{% extends 'base.html' %}} 
    {{% block content %}}
    <h2>Create {model_name}</h2>
<form method="post">
    {{% csrf_token %}} 
    {{{{ form.as_p }}}}
    <button type="submit">Submit</button>
</form>
<a href="{{% url '{model_name.lower()}_list' %}} ">Back to list</a>
{{% endblock %}} 
"""
    return html_content

def create_update_html(df, model_name):
    df = df.astype(str)
    # Starting script
    html_content = f"""{{% extends 'base.html' %}} 
    {{% block content %}} \n
    <h2>Edit {model_name}</h2>
<form method="post">
    {{% csrf_token %}} 
    {{{{ form.as_p }}}}
    <button type="submit">Submit</button>
</form>
<a href="{{% url '{model_name.lower()}_list' %}} ">Back to list</a>
{{% endblock %}} 
"""
    return html_content


def create_delete_html(df, model_name):
    df = df.astype(str)
    # Starting script
    html_content = f"""
    <h2>Delete {model_name}</h2>
<p>Are you sure you want to delete "{{{{ {model_name.lower()}.name }}}}"?</p>
<form method="post">
    {{% csrf_token %}} 
    <button type="submit">Yes, delete</button>
</form>
<a href="{{% url '{model_name.lower()}_list' %}} ">Cancel</a>
{{% endblock %}} 
"""
    return html_content

"""   


GET /api/1/customers/: List all customers.
POST /api/1/customers/: Create a new customer.
GET /api/1/customers/<id>/: Retrieve a customer by ID.
PUT /api/1/customers/<id>/: Update a customer by ID.
PATCH /api/1/customers/<id>/: Partially update a customer by ID.
DELETE /api/1/customers/<id>/: Delete a customer by ID.
"""
