import plotly as pl
import plotly.graph_objects as go


def create_heatmap(similarity_matrix, labels, title):
    """
    Generates and displays a heatmap using Plotly.
    Labels is a list of labels.
    """
    fig = go.Figure(data=go.Heatmap(
        z=similarity_matrix,
        x=labels,
        y=labels,
        colorscale='Viridis', # Choose a color scale
        colorbar=dict(title='Similarity'),
        hoverongaps=False
    ))

    fig.update_layout(
        title_text=title,
        xaxis_title="Files",
        yaxis_title="Files",
        xaxis_nticks=len(labels), # Ensure all labels are shown
        yaxis_nticks=len(labels),
        xaxis_showgrid=False, # Hide grid lines for cleaner look
        yaxis_showgrid=False,
        height=600, # Set a fixed height for better visualization
        width=700, # Set a fixed width
        margin=dict(l=100, r=100, t=100, b=100) # Adjust margins
    )

    # Display the plot
    fig.show()