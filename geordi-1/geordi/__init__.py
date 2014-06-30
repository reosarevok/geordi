# geordi
# Copyright (C) 2012 Ian McEwen, MetaBrainz Foundation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import division, absolute_import
from flask import Flask
from flask.ext.login import LoginManager, UserMixin
from geordi.config import *

from pyelasticsearch import ElasticSearch

app = Flask(__name__)
app.config.from_object(__name__)

@app.before_first_request
def setup_logging():
    if not app.debug:
        import logging
        from logging.handlers import RotatingFileHandler
        if app.config['ERROR_LOG']:
            error_fh = RotatingFileHandler(app.config['ERROR_LOG'],
                                           maxBytes=1024 * 1024 * 10,
                                           backupCount=10,
                                           encoding='utf_8')
            error_fh.setLevel(logging.ERROR)
            app.logger.addHandler(error_fh)
        if app.config['WARNING_LOG']:
            warning_fh = RotatingFileHandler(app.config['WARNING_LOG'],
                                             maxBytes=1024 * 1024 * 10,
                                             backupCount=10,
                                             encoding='utf_8')
            warning_fh.setLevel(logging.WARNING)
            app.logger.addHandler(warning_fh)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

login_manager = LoginManager()
login_manager.login_view = "ui.login"

@login_manager.user_loader
def load_user(username):
    return User(username)

login_manager.setup_app(app, add_context_processor=True)

es = ElasticSearch(app.config['ELASTICSEARCH_ENDPOINT'], max_retries=2, timeout=10, revival_delay=0)

import geordi.views
