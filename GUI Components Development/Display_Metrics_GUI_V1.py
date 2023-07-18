def display_metrics():
    metric_display = tk.Toplevel(window)
    metric_display.title("Tracked Metrics")

    # Create and pack the header labels
    header_frame = tk.Frame(metric_display)
    header_frame.pack(padx=20, pady=20)

    metric_label = tk.Label(header_frame, text="Metric")
    metric_label.pack(side=tk.LEFT, padx=10)

    calories_label = tk.Label(header_frame, text="Calories")
    calories_label.pack(side=tk.LEFT, padx=10)

    hours_label = tk.Label(header_frame, text="Hours")
    hours_label.pack(side=tk.LEFT, padx=10)

    # Create and pack the metric entries
    for metric, data in metrics.items():
        metric_frame = tk.Frame(metric_display)
        metric_frame.pack(padx=20, pady=10)

        metric_name_label = tk.Label(metric_frame, text=metric)
        metric_name_label.pack(side=tk.LEFT, padx=10)

        calories_label = tk.Label(metric_frame, text=data.get("calories", "-"))
        calories_label.pack(side=tk.LEFT, padx=10)

        hours_label = tk.Label(metric_frame, text=data.get("hours", "-"))
        hours_label.pack(side=tk.LEFT, padx=10)