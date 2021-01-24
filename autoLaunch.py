import webbrowser

url = 'https://www.google.com'
webbrowser.register('firefox',
	None,
	webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
webbrowser.get('firefox').open(url)
