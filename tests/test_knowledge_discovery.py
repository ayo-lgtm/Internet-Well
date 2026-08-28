import json
import unittest
from automation import knowledge_discovery as kd

class KnowledgeDiscoveryTests(unittest.TestCase):
    def test_sources_are_immutable_pinned(self):
        data=kd.registry()
        self.assertEqual(4, len(data['sources']))
        self.assertTrue(all(len(x['pin']) == 40 for x in data['sources']))

    def test_self_hosted_routing(self):
        p=kd.plan('find a self-hosted open source alternative to a SaaS analytics product')
        self.assertEqual('awesome-selfhosted', p['sources'][0]['source'])
        self.assertEqual('not-performed', p['execution'])

    def test_python_routing(self):
        p=kd.plan('find an agent memory library', 'python')
        self.assertEqual('awesome-python', p['sources'][0]['source'])

    def test_go_routing(self):
        p=kd.plan('find a bot framework', 'go')
        self.assertEqual('awesome-go', p['sources'][0]['source'])

    def test_security_reference_is_not_execution(self):
        p=kd.plan('linux security troubleshooting cli reference')
        self.assertEqual('book-of-secret-knowledge', p['sources'][0]['source'])
        self.assertEqual('not-performed', p['execution'])

if __name__ == '__main__': unittest.main()
