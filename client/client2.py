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

##RPC Call
ctxt = {}
for x in range(10):
    a = client.call(ctxt, 'test_method1', arg=x)
    print a

##RPC Cast
ctxt ={}
for x in range(10):
    a = client.cast(ctxt, 'test_method1', arg=x)
    print a
