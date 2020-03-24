
import subprocess
import logging
import zope.interface

from certbot import errors
from certbot import interfaces
from certbot.plugins import dns_common


logger = logging.getLogger(__name__)

@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)

class JJIMDNS_Authenticator(dns_common.DNSAuthenticator):
    default_ttl=30

    @classmethod
    def add_parser_arguments(cls, add):  # pylint: disable=arguments-differ
        super(Authenticator, cls).add_parser_arguments(add, default_propagation_seconds=0)
        add('remote_host', help='host to connect to via SSH', default='localhost')
        add('remote_user', help='user to connect as', default='root')
        add('min_ttl', help='minimum record TTL', default=30, type=int)

    def _setup_credentials(self):
        return

    def _perform(self, domain, rname, content):
        subprocess.run([ "ssh", "{}@{}".format(self.conf("remote_user"), self.conf("remote_host")), "replace: {} {} IN TXT {}".format(rname, self.conf("min_ttl"), content )])
    def _cleanup(self, domain, rname, content):
        subprocess.run([ "ssh", "{}@{}".format(self.conf("remote_user"), self.conf("remote_host")), "delete: {} {} IN TXT {}".format(rname, self.conf("min_ttl"), content )])
