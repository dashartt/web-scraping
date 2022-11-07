from parsel import Selector
import requests


response = requests.get("https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags")
selector = Selector(text=response.text)

images_url = selector.css('.image img::attr(src)').getall()
flags_image = list(map(lambda url: "http://"+url[2:], images_url))

for url in flags_image[:10]:    
    filename = url.split('/')[-1]
    try:
        request = requests.get(url, timeout=0.5)
    
        if request.status_code == 200:
            with open(f'exercises/flags/{filename}', 'wb') as file:
                file.write(request.content)
    except Exception:
        print("\n_______________________________\n")
        print(f"download fail {filename}")