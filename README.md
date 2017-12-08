## InstaBot

[Original README.md](https://github.com/instabot-py/instabot.py/blob/master/README.md)

## Heroku How-To

1) [Download and install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
2) Create `.env` file with environment variables (see `.env.example` for reference) - **don't forget to set the proxy server!**
3) run `./init_heroku.sh`
4) run `heroku ps:scale worker=1`

And you're gramming 24/7!

## Useful Heroku Commands

You can see the logs either in the web interface or by running:

`heroku logs --tail`

To stop the worker, either go to the web interface or run:

`heroku ps:scale worker=0`
