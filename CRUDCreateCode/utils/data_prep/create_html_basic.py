def create_list_html(df, model_name):
    df = df.astype(str)
    # Starting script
    
    def show_variables_in_form(df):
        form_fields = df[df['forms']==1]['Variable'].tolist()

        txt = ""
        for field in form_fields:
            txt += f"{{{{ {model_name.lower()}.{field} }}}} "
            
        return txt
    
    
    txt = show_variables_in_form(df)    

    html_content = f"""
    {{% extends 'base.html' %}} 
    {{% block content %}}  \n
    <h2>{model_name} List</h2>
<a href="{{%  url '{model_name.lower()}-create' %}} ">Create New {model_name.capitalize()} </a>
<ul>
{txt}
    <li>
        {{{{ {model_name.lower()}.date }}}} {{{{ {model_name.lower()}.price }}}}
        <a href="{{%  url '{model_name.lower()}-update' {model_name.lower()}.id %}} ">Edit</a>
        <a href="{{% url '{model_name.lower()}-delete' {model_name.lower()}.id %}} ">Delete</a>
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
<a href="{{% url '{model_name.lower()}-list' %}} ">Back to list</a>
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
<a href="{{% url '{model_name.lower()}-list' %}} ">Back to list</a>
{{% endblock %}} 
"""
    return html_content


def create_delete_html(df, model_name):
    df = df.astype(str)
    # Starting script
    html_content = f"""
    {{% extends 'base.html' %}} 
    {{% block content %}} \n
    <h2>Delete {model_name}</h2>
<p>Are you sure you want to delete "{{{{ {model_name.lower()}.name }}}}"?</p>
<form method="post">
    {{% csrf_token %}} 
    <button type="submit">Yes, delete</button>
</form>
<a href="{{% url '{model_name.lower()}-list' %}} ">Cancel</a>
{{% endblock %}} 
"""
    return html_content



def create_form_html(df, model_name, model_fields):
    df = df.astype(str)
    # Starting script
    html_content = f"""
   {{% extends 'base.html' %}} 
   {{% block content %}} \n
<div class="container mt-5">
    <h1>{{% if {model_name.lower()} %}}Edit {model_name}{{% else %}}Create {model_name}{{% endif %}}</h1>
    <form method="post">
        {{% csrf_token %}}
        {{{{ form.as_p }}}}
        <button type="submit" class="btn btn-primary">Submit</button>
        <a href="{{% url '{model_name.lower()}-list' %}}" class="btn btn-secondary">Cancel</a>
    </form>
    <a href="{{% url '{model_name.lower()}-create' %}}">Add {model_name}</a>  {{# Assuming you have a URL named '{model_name.lower()}-create' #}}
</div>
{{% endblock %}} 
"""
    return html_content




def create_confirm_delete_html(df, model_name):
    df = df.astype(str)
    
    html_content = f"""
     <!-- {model_name.lower()}-confirm-delete.html -->
   {{% extends 'base.html' %}} 
   {{% block content %}} \n
<div class="container mt-5">
    <h1>Confirm Deletion</h1>
    <p>Are you sure you want to delete the {model_name.lower()} with ID {{ {model_name.lower()}.id }}?</p>
    <form method="post">
        {{% csrf_token %}}
        <button type="submit" class="btn btn-danger">Delete</button>
        <a href="{{% url '{model_name.lower()}-list' %}}" class="btn btn-primary">Cancel</a>
    </form>
</div>
{{% endblock %}} 
"""
    return html_content
 
 

def create_detail_html(df, model_name, model_fields):
    def create_fields_list(model_fields):
        txt = ""
        for i in model_fields:
            i_name = i.upper().replace("_", " ")
            txt += """
            <tr>
                <th>{model_name} {i_name}</th>
                <td>{{{{ {model_name.lower()}.{i} }}}}</td>
            </tr>
            """
        return txt
    
    df = df.astype(str)
    fields_form = create_fields_list(model_fields)
    html_content = f"""
    
{{% extends 'base.html' %}} 
{{% block content %}} \n
<div class="container mt-5">
    <h1>{model_name} Details</h1>
    <table class="table table-bordered">
        <tbody>
        {fields_form}
        </tbody>
    </table>

    <!-- Update and Delete Buttons -->
    <div class="mt-3">
        <a href="{{% url '{model_name.lower()}-update' {model_name.lower()}.pk %}}" class="btn btn-primary">Edit {model_name}</a>
        <a href="{{% url '{model_name.lower()}-delete' {model_name.lower()}.pk %}}" class="btn btn-danger">Delete {model_name}</a>
    </div>
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
