import oslo_messaging as om

from config import *

##Invoke "get_transport". This call will set default Configurations required to Create Messaging Transport
transport = om.get_transport(cfg.CONF)

cfg.CONF(['--config-file', 'file.conf'])

##Create Messaging Transport
transport = om.get_transport(cfg.CONF)

##Create Target
target = om.Target(topic='testme')

##Create RPC Client
client = om.RPCClient(transport, target)

##Invoke remote method and wait for a reply.
arg = "Call Method 1"
ctxt = {}
client.call(ctxt, 'test_method1', arg=arg)

##Invoke remote method and return immediately.
arg = "Cast method 1"
ctxt = {}
client.cast(ctxt, 'test_method1', arg=arg)