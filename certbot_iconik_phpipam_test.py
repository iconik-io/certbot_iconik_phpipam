import pynetdot

import certbot_netdot

# I dropped the split_domain code so these tests aren't valid anymore

# def test_split_domain(monkeypatch):
#     def mock_lookup_domain(self, domain):
#         domain_name = "bar.baz"
#         if domain.endswith(domain_name):
#             ret = pynetdot.Zone()
#             ret.name = domain_name
#             return ret
#
#     monkeypatch.setattr(certbot_netdot.NetdotClient, 'lookup_domain', mock_lookup_domain)
#
#     client = certbot_netdot.NetdotClient()
#     test_val = client.split_domain("foo.kaka.bar.baz")
#
#     assert test_val == ('foo.kaka', 'bar.baz')
#
# def test_split_domain_full(monkeypatch):
#     def mock_lookup_domain(self, domain):
#         domain_name = "bar.baz"
#         if domain.endswith(domain_name):
#             ret = pynetdot.Zone()
#             ret.name = domain_name
#             return ret
#
#     monkeypatch.setattr(certbot_netdot.NetdotClient, 'lookup_domain', mock_lookup_domain)
#
#     client = certbot_netdot.NetdotClient()
#     test_val = client.split_domain("bar.baz")
#
#     assert test_val == ('', 'bar.baz')
