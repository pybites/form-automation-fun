## PyBites Banner Generator Automation

After writing [Making a Banner Generator With Pillow and Flask](https://pybit.es/pillow-banner-flask.html) I felt like automating the process even more.

So I wrote two scripts to use Requests and Selenium to automate [PyBites Banner Generator](https://pybites-banners.herokuapp.com/) app login and banner form submission/ creation.

Install requirements (might need to OS install PhantomJS) and run:

1. Public version: 

		$ python public_banner.py
	
	This is an interactive script

2. Private version (PyBites only for now - but feel free to clone the repo and deploy it to Heroku with your own logos):

	Using `click`:

		$ python private_banner.py  --help
		Usage: private_banner.py [OPTIONS]

		Options:
		-n, --name TEXT
		-l, --logo [news|challenge|special|article]
		-i, --image TEXT
		-t, --text TEXT
		-b, --background / -nb, --no-background
		-o, --outfile TEXT
		-u, --username TEXT
		-p, --password TEXT
		--help                          Show this message and exit.

	For example:

		$ python private_banner.py  -n mybanner -l special -i http://images.indianexpress.com/2015/05/python.jpg -t 'PyBites Banner Generator Automation' -b
