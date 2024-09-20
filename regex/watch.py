import re

def main():
    html_input = input("HTML: ")
    quick_url = parse(html_input)
    if quick_url:
        print(quick_url)
    else:
        print("None")

def parse(s):
    # Regular expression to find the src attribute in the iframe tag
    match_vid = re.search(r'<iframe[^>]+src="([^"]+)"', s)
    if match_vid:
        vid_url = match_vid.group(1)
        match_id = re.search(r"(?:https?:)?(?:\/\/)?(?:[0-9A-Z-]+\.)?(?:youtu\.be\/|youtube(?:-nocookie)?\.com\S*?[^\w\s-])([\w-]{11})(?=[^\w-]|$)(?![?=&+%\w.-]*(?:['\"][^<>]*>|<\/a>))[?=&+%\w.-]*", vid_url)
        if match_id:
            vid_id = match_id.group(1)
            if vid_id:
                short_url = f"https://youtu.be/{vid_id}"
                return short_url
            return None
        return None
    return None
    
    
# def convert_to_short_url(url):
#     short_url = f"https://youtu.be/{url}"
#     return short_url

if __name__ == "__main__":
    main()