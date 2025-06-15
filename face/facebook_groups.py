import csv
import json
import os
import hmac
import hashlib
from facepy import GraphAPI
from facepy.exceptions import FacebookError

# Access token beszerzése:
# App id: 128127535865520
# App secret: 492ce06b91352bf2d9efe2695ed8eb0f
# curl -X GET "https://graph.facebook.com/oauth/access_token
#   ?client_id={your-app-id}
#   &client_secret={your-app-secret}
#   &grant_type=client_credentials"

class FacebookGroupScraper:
    """Facebook csoport adatok legyűjtésére szolgáló osztály"""

    DEFAULT_GROUP_ID = "488606049192077"
    DEFAULT_OUTPUT_FILE = "weores-group-summary.csv"

    def __init__(self, access_token=None, app_secret=None, group_id=None, output_file=None):
        # Ha nincs megadva, próbáljuk környezeti változóból
        if not access_token:
            access_token = os.getenv('FACEBOOK_ACCESS_TOKEN')

        if not app_secret:
            app_secret = os.getenv('FACEBOOK_APP_SECRET')

        # Ha még mindig nincs, kérjük be paraméterként
        if not access_token:
            raise ValueError(
                "Facebook access token szükséges!\n"
                "Opciók:\n"
                "1. Állítsd be a FACEBOOK_ACCESS_TOKEN környezeti változót\n"
                "2. Vagy add meg paraméterként: FacebookGroupScraper(access_token='TOKEN')"
            )

        if not app_secret:
            raise ValueError(
                "Facebook app secret szükséges!\n"
                "Opciók:\n"
                "1. Állítsd be a FACEBOOK_APP_SECRET környezeti változót\n"
                "2. Vagy add meg paraméterként: FacebookGroupScraper(app_secret='SECRET')\n"
                "3. Vagy használd a run_with_credentials() függvényt"
            )

        self.access_token = access_token
        self.app_secret = app_secret
        self.group_id = group_id or self.DEFAULT_GROUP_ID
        self.output_file = output_file or self.DEFAULT_OUTPUT_FILE
        self.processed_posts = []

        # GraphAPI inicializálása - csak az access token pozicionális paraméterként
        self.graph = GraphAPI(self.access_token)

    def generate_app_secret_proof(self):
        """App Secret Proof generálása"""
        return hmac.new(
            self.app_secret.encode('utf-8'),
            self.access_token.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    def validate_token(self):
        """Access token érvényességének ellenőrzése app secret proof-fal"""
        try:
            app_secret_proof = self.generate_app_secret_proof()
            self.graph.get('me', appsecret_proof=app_secret_proof)
            return True
        except FacebookError as e:
            print(f"Token érvényesítési hiba: {e}")
            if e.code == 100:
                print("App Secret Proof szükséges, de automatikusan generálva lesz.")
                return True
            return False

    def fetch_group_feed(self):
        """Facebook csoport feed lekérése hibakezeléssel és app secret proof-fal"""
        try:
            app_secret_proof = self.generate_app_secret_proof()
            return self.graph.get(
                f"{self.group_id}/feed",
                page=False,
                limit=100,
                since="yyyy-mm-dd",
                until="yyyy-mm-dd",
                appsecret_proof=app_secret_proof
            )
        except FacebookError as e:
            if e.code == 190:
                raise ValueError("Érvénytelen access token! Generálj új tokent a Facebook Developer Console-ban.")
            elif e.code == 100:
                raise ValueError("App Secret Proof hiba! Ellenőrizd az App Secret-et.")
            elif e.code == 10:
                raise ValueError("Nem rendelkezel jogosultsággal a csoport eléréséhez!")
            else:
                raise ValueError(f"Facebook API hiba [{e.code}]: {e.message}")

    def extract_post_data(self, post):
        """Egyetlen poszt adatainak kinyerése"""
        post_data = [
            post["created_time"],
            post["from"]["name"]
        ]

        post_data.append(post.get("name", "No Link"))
        post_data.append(post.get("link", "No URL"))

        likes_count = 0
        if "likes" in post and "data" in post["likes"]:
            likes_count = len(post["likes"]["data"])
        post_data.append(likes_count)

        comments_count = "No Comments :("
        if "comments" in post and "data" in post["comments"]:
            comments_count = len(post["comments"]["data"])
        post_data.append(comments_count)

        return post_data

    def process_posts(self, posts_data):
        """Összes poszt adatainak feldolgozása"""
        for post in posts_data:
            processed_post = self.extract_post_data(post)
            self.processed_posts.append(processed_post)

    def print_results(self):
        """Eredmények kiírása a konzolra"""
        for post_data in self.processed_posts:
            try:
                print(", ".join(map(str, post_data)))
            except UnicodeError:
                pass

    def save_to_csv(self):
        """Eredmények mentése CSV fájlba"""
        try:
            with open(self.output_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Header sor
                writer.writerow(['Created Time', 'Author', 'Name', 'Link', 'Likes', 'Comments'])
                # Adatok
                writer.writerows(self.processed_posts)
            print(f"Adatok mentve: {self.output_file}")
        except Exception as e:
            print(f"CSV mentési hiba: {e}")

    def scrape_group_data(self):
        """Fő folyamat: csoport adatok legyűjtése és feldolgozása"""
        print("Token érvényesítése...")
        if not self.validate_token():
            print("Érvénytelen access token!")
            return

        print("Csoport adatok legyűjtése...")
        try:
            feed_data = self.fetch_group_feed()
            posts = feed_data["data"]
            print(f"{len(posts)} poszt találva.")
            self.process_posts(posts)
            self.print_results()
            self.save_to_csv()
        except Exception as e:
            print(f"Hiba történt az adatok legyűjtése során: {e}")


def run_with_credentials():
    """Segédfüggvény a hitelesítő adatok bekérésére"""
    print("Facebook API hitelesítő adatok szükségesek:")
    print("Ezeket a Facebook Developer Console-ból szerezheted be:")
    print("https://developers.facebook.com/")
    print()

    access_token = input("Access Token: ").strip()
    app_secret = input("App Secret: ").strip()

    if not access_token or not app_secret:
        print("Mindkét érték szükséges!")
        return

    try:
        scraper = FacebookGroupScraper(access_token=access_token, app_secret=app_secret)
        scraper.scrape_group_data()
    except Exception as e:
        print(f"Hiba: {e}")


def main():
    """Facebook csoport kommentek legyűjtése"""
    ACCESS_TOKEN = "128127535865520|oXfy5D3qJRh-XlTkX0sUwpQpbfs"
    APP_SECRET = "492ce06b91352bf2d9efe2695ed8eb0f"
    try:
        scraper = FacebookGroupScraper(ACCESS_TOKEN, APP_SECRET)
        scraper.scrape_group_data()
    except ValueError as e:
        print(f"Beállítási hiba: {e}")
        print("\nAlternatíva: Használd a run_with_credentials() függvényt")

        response = input("\nSzeretnéd most megadni a hitelesítő adatokat? (i/n): ").lower()
        if response == 'i':
            run_with_credentials()


if __name__ == "__main__":
    main()
