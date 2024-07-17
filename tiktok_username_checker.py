import requests
from itertools import cycle

# Function to read usernames from file
def read_usernames(filename):
    with open(filename, 'r') as file:
        usernames = file.readlines()
    return [username.strip() for username in usernames]

# Function to get proxy list
def get_proxies():
    url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.splitlines()
    else:
        print(f"Failed to fetch proxies. Status code: {response.status_code}")
        return []

# Function to check username availability
def check_username(username, proxies):
    proxy = next(proxies)
    proxy_dict = {
        "http": proxy,
        "https": proxy
    }
    url = f'https://api.tiktok.com/username/check/?username={username}'
    try:
        response = requests.post(url, proxies=proxy_dict)
        if response.status_code == 200:
            result = response.json()
            if result.get('available'):
                print(f"Username '{username}' is available!")
            else:
                print(f"Username '{username}' is taken.")
        else:
            print(f"Failed to check username '{username}'. Status code: {response.status_code}")
    except Exception as e:
        print(f"Exception occurred: {str(e)}")

# Main function
def main():
    usernames = read_usernames('words.txt')
    proxies = cycle(get_proxies())
    
    for username in usernames:
        check_username(username, proxies)

# Entry point
if __name__ == "__main__":
    main()
