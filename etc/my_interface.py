from supervisor.rpcinterface import SupervisorNamespaceRPCInterface


class CustomRPCInterface:
    def __init__(self, supervisord):
        self.supervisord = supervisord
        self.retries = 3

    def startProcessOrRetry(self, name, wait=True):
        interface = SupervisorNamespaceRPCInterface(self.supervisord)
        retry = 0

        while not interface.startProcess(name) or retry < self.retries:
            retry = retry + 1


# this is not used in code but referenced via an entry point in the conf file
def make_custom_rpcinterface(supervisord):
    return CustomRPCInterface(supervisord)
