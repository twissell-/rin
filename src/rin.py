import plexaniscrobbler
import plextoggltracker
from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix

import config

rin = Flask("Rin")
rin.debug = config.get("debug")


@rin.before_request
def request_logger():
    rin.logger.debug("Data: {}".format(request.data))
    rin.logger.debug("Args: {}".format(dict(request.args)))
    rin.logger.debug("Form: {}".format(dict(request.form)))


plexaniscrobbler.configure(
    anilist_username=config.get("plexaniscrobbler.anilist_username"),
    anilist_access_token=config.get("plexaniscrobbler.anilist_access_token"),
    plex_username=config.get("plexaniscrobbler.plex_username"),
)

rin.register_blueprint(
    plexaniscrobbler.webhook, url_prefix=config.get("plexaniscrobbler.url_prefix")
)

plextoggltracker.configure(
    toggl_api_token=config.get("plextoggltracker.toggl_api_token"),
    plex_username=config.get("plextoggltracker.plex_username"),
    mapping=config.get("plextoggltracker.mapping"),
)

rin.register_blueprint(
    plextoggltracker.webhook, url_prefix=config.get("plextoggltracker.url_prefix")
)

rin.wsgi_app = ProxyFix(rin.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
rin.run(host="0.0.0.0", port=86000)
