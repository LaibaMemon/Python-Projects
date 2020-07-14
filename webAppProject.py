import webbrowser as wb

def webauto():
	chrome_path='C:/Program Files (x86)/Google/Application/chrome.exe %s'#Add the path of the chrome here
	URLS=( 
		   "gmail.com",
		   "google.com"
		   "facebook.com"
		   "youtube.com"
		   "github.com"
		)
	for url in URLS:
		print("opening:"+url)
		wb.get(chrome_path).open(url)

webauto()