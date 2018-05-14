#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import socket
import sys

# from neutron.common import config as common_config
from oslo_config import cfg
from oslo_log import log as logging

from dragonflow.common import profiler as df_profiler
from dragonflow import conf

LOG = logging.getLogger(__name__)

EXTRA_LOG_LEVEL_DEFAULTS = [
    'dragonflow=DEBUG'
]

logging.register_options(cfg.CONF)


def init(args, **kwargs):
    cfg.CONF(args=args, project='dragonflow', **kwargs)
    cfg.CONF.host = socket.gethostname()
    product_name = "dragonflow"
    logging.set_defaults(default_log_levels=logging.get_default_log_levels() +
                         EXTRA_LOG_LEVEL_DEFAULTS)
    logging.setup(cfg.CONF, product_name)
    LOG.info("Logging enabled!")
    LOG.info("%(prog)s", {'prog': sys.argv[0]})
    LOG.debug("command line: %s", " ".join(sys.argv))
    df_profiler.setup(sys.argv[0], conf.CONF.host)

