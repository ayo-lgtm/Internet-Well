import json
import tempfile
import unittest
from pathlib import Path
from automation import knowledge_discovery as kd

SELFHOSTED = '''## Analytics\n- [Plausible](https://plausible.io/) - Privacy-friendly analytics. ([Source Code](https://github.com/plausible/analytics)) `AGPL-3.0` `Elixir/Docker`\n'''
PYTHON = '''## Artificial Intelligence\n- [mem0](https://github.com/mem0ai/mem0) - Intelligent memory layer for AI agents.\n'''
GO = '''## Bot Building\n- [teleflow](https://github.com/kslamph/teleflow) - Type-safe Telegram bot framework.\n'''
SECRET = '''## Security\n- [Example scanner](https://example.com/scanner) - Network security scanner reference.\n- [Dangerous example](https://example.com/exploit) - Reverse shell exploit payload reference.\n'''

class KnowledgeDiscoveryTests(unittest.TestCase):
    def test_sources_are_immutable_pinned(self):
        data = kd.registry()
        self.assertEqual(10, len(data['sources']))
        self.assertTrue(all(len(x['pin']) == 40 for x in data['sources']))
        ids = {x['id'] for x in data['sources']}
        self.assertTrue({'free-for-dev','awesome-mcp-servers','awesome-llm-apps','ollama','scrapling','open-design'} <= ids)

    def test_executable_sources_have_restrictions(self):
        sources = {x['id']: x for x in kd.registry()['sources']}
        for source_id in ['ollama', 'scrapling', 'open-design']:
            self.assertEqual('executable-capability', sources[source_id]['mode'])
            self.assertTrue(sources[source_id]['restrictions'])
        self.assertIn('no-unverified-mcp-execution', sources['awesome-mcp-servers']['restrictions'])

    def test_source_routing(self):
        self.assertEqual('awesome-selfhosted', kd.plan('find a self-hosted open source alternative to analytics')['sources'][0]['source'])
        self.assertEqual('awesome-python', kd.plan('find an agent memory library', 'python')['sources'][0]['source'])
        self.assertEqual('awesome-go', kd.plan('find a bot framework', 'go')['sources'][0]['source'])
        self.assertEqual('book-of-secret-knowledge', kd.plan('linux security troubleshooting cli reference')['sources'][0]['source'])

    def test_builds_normalized_cross_source_index(self):
        index = kd.build_index({'awesome-selfhosted': SELFHOSTED, 'awesome-python': PYTHON, 'awesome-go': GO, 'book-of-secret-knowledge': SECRET})
        self.assertEqual('2.0', index['schema_version'])
        self.assertEqual(5, index['record_count'])
        plausible = next(x for x in index['records'] if x['name'] == 'Plausible')
        self.assertEqual('https://github.com/plausible/analytics', plausible['upstream_repository'])
        self.assertEqual('unverified-discovery-candidate', plausible['approval_status'])

    def test_search_and_agent_handoff(self):
        index = kd.build_index({'awesome-selfhosted': SELFHOSTED, 'awesome-python': PYTHON, 'awesome-go': GO})
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / 'index.json'
            kd.write_index(index, path)
            result = kd.search_index('agent memory', path=path)
            self.assertEqual('mem0', result['results'][0]['name'])
            self.assertEqual('not-authorized', result['execution'])
            handoff = kd.agent_brain_handoff('telegram bot', language='go', path=path)
            self.assertEqual('teleflow', handoff['candidate_resources'][0]['name'])
            self.assertEqual('agent-brain-verification-and-stack-composition', handoff['next_stage'])

    def test_deduplicates_same_upstream(self):
        duplicate = '## AI\n- [Mem Zero](https://github.com/mem0ai/mem0/) - Another description.\n'
        index = kd.build_index({'awesome-python': PYTHON, 'awesome-go': duplicate})
        matching = [r for r in index['records'] if 'mem0ai/mem0' in (r.get('upstream_repository') or '')]
        self.assertEqual(1, len(matching))
        self.assertEqual(['awesome-go', 'awesome-python'], matching[0]['discovered_by'])

    def test_high_risk_reference_hidden_by_default(self):
        index = kd.build_index({'book-of-secret-knowledge': SECRET})
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / 'index.json'; kd.write_index(index, path)
            result = kd.search_index('reverse shell exploit', path=path)
            self.assertEqual([], result['results'])
            result = kd.search_index('reverse shell exploit', path=path, include_high_risk=True)
            self.assertEqual('high', result['results'][0]['risk_class'])

if __name__ == '__main__':
    unittest.main()
