c = get_config()  # Get the config object.
c.IPKernelApp.pylab = 'inline'  # in-line figure when using Matplotlib
c.NotebookApp.ip = '*'  # Serve notebooks locally.
c.NotebookApp.open_browser = False  # Do not open a browser window by default when using notebooks.
