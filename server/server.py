import oslo_messaging as om

from config import *

##Invoke "get_transport". This call will set default Configurations required to Create Messaging Transport
transport = om.get_transport(cfg.CONF)

cfg.CONF(['--config-file', 'file.conf'])

##Create Messaging Transport
transport = om.get_transport(cfg.CONF)

##Create Target (Exchange, Topic and Server to listen on)
target = om.Target(topic='testme', server='192.168.122.116')

##Create EndPoint
class TestEndpoint(object):
    def test_method1(self, ctx, arg):
        res = "Result from test_method1 " + str(arg)
        print res
        return res
    def test_method2(self, ctx, arg):
        res = "Result from test_method2 " + str(arg)
        print res
        return res

##Create EndPoint List
endpoints = [TestEndpoint(), ]

##Create RPC Server
access_policy = om.rpc.dispatcher.DefaultRPCAccessPolicy
server = om.get_rpc_server(transport, target, endpoints, executor='eventlet', access_policy=access_policy)
#server = om.get_rpc_server(transport, target, endpoints, executor='blocking', access_policy=access_policy)

##Start RPC Server
server.start()
server.wait()
