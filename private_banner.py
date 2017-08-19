import click
from seleniumrequests import PhantomJS

BANNER_APP = 'https://pybites-banners.herokuapp.com/'
HEADERS = {'User-Agent': 'Mozilla/5.0'}
PYTHON_LOGO_IMG = 'assets/python/python-logo.png'
ASSET_PNG = 'assets/pybites/pybites-{}.png'
# to retrieve option list with Selenium - https://stackoverflow.com/a/18516161
PYBITES_PILLARS = 'news challenge special article'.split()


def login(username, password):
    driver = PhantomJS()
    driver.get(BANNER_APP)
    driver.find_element_by_link_text('login').click()

    username_field = driver.find_element_by_name('username')
    username_field.send_keys(username)
    password_field = driver.find_element_by_name('password')
    password_field.send_keys(password)

    # TODO: need html id/name on button
    btn_xpath = "//button[contains(@class, 'pure-button-primary')]"
    login_btn = driver.find_element_by_xpath(btn_xpath)
    login_btn.click()

    return driver


@click.command()
@click.option('-n', '--name', prompt=True)
@click.option('-l', '--logo', type=click.Choice(PYBITES_PILLARS))
@click.option('-i', '--image', prompt=True)
@click.option('-t', '--text', prompt=True)
@click.option('-b/-nb', '--background/--no-background',
              default=False, prompt=True)
@click.option('-o', '--outfile', default='banner.png')
@click.option('-u', '--username', envvar='USERNAME')
@click.option('-p', '--password', envvar='PASSWORD')
def get_banner(name, logo, image, text, background, outfile,
               username, password):
    logo = ASSET_PNG.format(logo)
    data = {
        'name': name,
        'image_url1': logo,
        'image_url2': image,
        'text': text,
        'background': 'y' if background else 'n',
    }

    driver = login(username, password)

    request = driver.request('POST', BANNER_APP, data=data)

    if request.status_code != 200:
        request.raise_for_status()

    with open(outfile, 'wb') as f:
        f.write(request.content)


if __name__ == '__main__':
    get_banner()
