import click
import requests

BANNER_APP = 'https://pybites-banners.herokuapp.com/'
HEADERS = {'User-Agent': 'Mozilla/5.0'}
PYTHON_LOGO_IMG = 'assets/python/python-logo.png'

fixed_params = {'name': 'some-banner', 'image_url1': PYTHON_LOGO_IMG}


@click.command()
@click.option('--image', prompt=True)
@click.option('--text', prompt=True)
@click.option('--background', default=True, is_flag=True, prompt=True)
@click.option('--outfile', default='banner.png')
def get_banner(image, text, background, outfile):
    user_inputs = {
        'image_url2': image,
        'text': text,
        'background': 'y' if background else 'n',
    }
    payload = {**fixed_params, **user_inputs}

    session = requests.Session()
    request = session.post(BANNER_APP, headers=HEADERS, data=payload)

    if request.status_code != 200:
        request.raise_for_status()

    with open(outfile, 'wb') as f:
        f.write(request.content)


if __name__ == '__main__':
    get_banner()
