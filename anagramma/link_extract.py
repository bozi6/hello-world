import requests
from bs4 import BeautifulSoup

"""
Linkből képek listájával tér vissza
"""


def main():
    """
    Főprogram
    :return: linkek listája
    """
    # Making get request
    r = requests.get(
        "https://www.google.com/search?q=imse+vimse&sxsrf=ALiCzsZ1a395vz7srBcjbJNDgiHaqW2vwQ:1669560820383&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiCvYTdzs77AhVf_rsIHbgbC_sQ_AUoAnoECAEQBA&biw=1596&bih=905&dpr=2/"
    )

    # show connection info
    print(r)

    # parsing HTML
    soup = BeautifulSoup(r.content, "html.parser")

    # find all the anchor tags with "href"
    # for link in soup.find_all('a'):
    #    print(link.get('href'))

    # extract images
    images_list = []

    images = soup.select("img")
    for image in images:
        src = image.get("src")
        alt = image.get("alt")
        images_list.append({"src": src, "alt": alt})

    for image in images_list:
        print(image)


if __name__ == "__main__":
    main()
