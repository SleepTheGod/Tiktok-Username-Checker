Tiktok Username Checker
This Python script checks the availability of usernames on TikTok using their API, incorporating rotating proxies to avoid rate limiting. It reads usernames from a words.txt file and utilizes proxies fetched from https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all.

Requirements
To run this script, ensure you have the following installed:

requests: Library for making HTTP requests in Python.
Installation

Clone the repository
git clone https://github.com/SleepTheGod/Tiktok-Username-Checker.git

Navigate into the project directory
cd Tiktok-Username-Checker

Install dependencies using pip
pip install -r requirements.txt

Usage
Place your list of usernames in words.txt, with one username per line.

Run the script
python tiktok_username_checker.py 

Notes
Proxies are automatically rotated to avoid IP bans and rate limits.
Adjust error handling and retry mechanisms in the script based on your requirements.


