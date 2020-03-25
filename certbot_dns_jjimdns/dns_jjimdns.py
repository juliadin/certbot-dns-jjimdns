
import subprocess
import logging
import time

import zope.interface

from certbot import errors
from certbot import interfaces
from certbot.plugins import dns_common


logger = logging.getLogger(__name__)

@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)

class JJIMDNS_Authenticator(dns_common.DNSAuthenticator):

    description="Authenticate via SSH Cli to a remote DNS Server, running a JJIMDNS compatible command proxy"
    long_description=description

    @classmethod
    def add_parser_arguments(cls, add):  # pylint: disable=arguments-differ
        super(JJIMDNS_Authenticator, cls).add_parser_arguments(add, default_propagation_seconds=10)
        add('remote-host', help='host to connect to via SSH', default='localhost')
        add('remote-user', help='user to connect as', default='root')
        add('min-ttl', help='minimum record TTL', default=30, type=int)

    def more_info(self):
        return("The plugin uses a remote DNS server via SSH to install and cleanup challenges. The remote must support the jjimdns protocol.")

    def _setup_credentials(self):
        return

    def _perform(self, domain, rname, content):
        result = subprocess.run([ "ssh", "{}@{}".format(self.conf("remote-user"), self.conf("remote-host")), "replace: {} {} IN TXT {}".format(rname, self.conf("min-ttl"), content )])
        if result.returncode > 0:
            raise errors.PluginError("There was an error setting up the challenge '{}'. Return code was {}".format(rname, result.returncode))

    def _cleanup(self, domain, rname, content):
        result = subprocess.run([ "ssh", "{}@{}".format(self.conf("remote-user"), self.conf("remote-host")), "delete: {} {} IN TXT {}".format(rname, self.conf("min-ttl"), content )])
        if result.returncode > 0:
            raise errors.PluginError("There was an error cleaning up the challenge '{}'. Return code was {}".format(rname, result.returncode))
