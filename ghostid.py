import argparse
import requests
import sys
from requests.exceptions import RequestException

class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

BANNER = r"""
 ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗    ██╗██████╗ 
██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝    ██║██╔══██╗
██║  ███╗███████║██║   ██║███████╗   ██║       ██║██║  ██║
██║   ██║██╔══██║██║   ██║╚════██║   ██║       ██║██║  ██║
╚██████╔╝██║  ██║╚██████╔╝███████║   ██║       ██║██████╔╝
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝       ╚═╝╚═════╝ 
"""

PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "Medium": "https://medium.com/@{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "YouTube": "https://www.youtube.com/{}",
    "Xbox": "https://account.xbox.com/en-us/Profile?gamertag={}",
    "Keybase": "https://keybase.io/{}",
    "About.me": "https://about.me/{}",
    "Last.fm": "https://www.last.fm/user/{}",
    "Stack Overflow": "https://stackoverflow.com/users/{}",
    "TryHackMe": "https://tryhackme.com/p/{}",
    "OpenSea": "https://opensea.io/{}",
    "CyberDefenders": "https://cyberdefenders.org/p/{}#/overview",
}

def check_username(username: str) -> None:
    """Verifica si un nombre de usuario existe en varias plataformas."""
    print(BANNER)
    print(f"\n🔍 Buscando usuario: {username}\n")
    headers = {"User-Agent": "Mozilla/5.0"}

    for platform, url_template in PLATFORMS.items():
        url = url_template.format(username)
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                print(f"{Colors.GREEN}[✓] {platform:<15} ENCONTRADO ➜ {url}{Colors.RESET}")
            elif response.status_code == 404:
                print(f"{Colors.RED}[✗] {platform:<15} NO ENCONTRADO{Colors.RESET}")
            else:
                print(f"{Colors.YELLOW}[!] {platform:<15} STATUS {response.status_code}{Colors.RESET}")
        except RequestException as e:
            print(f"{Colors.YELLOW}[!] {platform:<15} ERROR: {e}{Colors.RESET}")

    print("\n✅ Búsqueda terminada.\n")

def main():
    parser = argparse.ArgumentParser(description="Verifica si un nombre de usuario existe en varias plataformas.")
    parser.add_argument("-u", "--username", required=True, help="Nombre de usuario a buscar")
    args = parser.parse_args()

    if not args.username.strip():
        print(f"{Colors.RED}Error: El nombre de usuario no puede estar vacío.{Colors.RESET}")
        sys.exit(1)

    check_username(args.username)

if __name__ == "__main__":
    main()
