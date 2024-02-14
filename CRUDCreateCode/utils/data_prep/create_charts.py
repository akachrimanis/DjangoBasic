def create_chart(df, model_name, chart_type):
    df = df.astype(str)
    # Starting script
    
    html_script = f"""
    {{% block scripts %}}
    <div>
    <canvas id="{{chart_type.upper()}}"></canvas>
    </div>
  
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  
    <script>
        const ctx = document.getElementById('myChart');
    
        new Chart(ctx, {{
        type: '{{chart_type}}',
        data: {{
            labels: [{{% for item in qs %}}'{{{{item.date}}}}',{{% endfor %}}],
            datasets: [{{
            label: '# of Votes',
            data: [{{% for item in qs %}}{{item.price}},{{% endfor %}}],
            borderWidth: 1
            }}]
        }},
        options: {{
            scales: {{
            y: {{
                beginAtZero: true
            }}
            }}
        }}
        }});
  </script>
  

{{% endblock scripts %}}
{{% block content %}}

{{% endblock %}} 

    """
   
