from oslo_config import cfg

from opts import *

oslo_messaging_rabbit_group = cfg.OptGroup('oslo_messaging_rabbit')
cfg.CONF.register_group(oslo_messaging_rabbit_group)
cfg.CONF.register_opts(rabbit_opts, group=oslo_messaging_rabbit_group)

