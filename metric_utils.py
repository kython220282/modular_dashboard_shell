def display_metric(label, value, delta=None, delta_color="normal"):
    st.metric(label=label, value=value, delta=delta, delta_color=delta_color, border= True)
