import requests
import json
import time

def fetch_fortnite_posts():
    url = 'https://www.fortnite.com/api/blog/getPosts?category=&postsPerPage=0&offset=0&locale=en-US&rootPageSlug=blog'
    headers = {
        'Cache-Control': 'no-cache',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US',
        'Referer': 'https://www.fortnite.com/news',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }

    print("Attempting to fetch", url)
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Fetch successful")
        return response.json()
    else:
        print(f"Failed to fetch Fortnite API: {response.status_code}")
        print("Response content:", response.content)
        return None

if __name__ == "__main__":
    fortnite_posts = fetch_fortnite_posts()
    if fortnite_posts:
        with open("posts/blog_posts.json", "w") as file:
            json.dump(fortnite_posts, file, indent=4)
            print("Data saved to file")
        with open("posts/timestamp.json", "w") as file:
            file.write('{"timestamp": ' + str(time.time()) + '}')
            print("Timestamp saved to file")
