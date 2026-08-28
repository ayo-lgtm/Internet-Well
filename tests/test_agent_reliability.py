import unittest
from automation import agent_reliability as ar


class AgentReliabilityTests(unittest.TestCase):
    def test_benchmark_suite_is_versioned_and_broad(self):
        data = ar.load_benchmarks()
        self.assertEqual('0.5.0', data['version'])
        self.assertGreaterEqual(len(data['scenarios']), 8)
        ids = {x['id'] for x in data['scenarios']}
        self.assertIn('soc2-readiness-architecture', ids)
        self.assertIn('authorized-web-extraction', ids)
        self.assertIn('production-code-change', ids)

    def test_agent_self_report_cannot_force_pass(self):
        sc = ar.scenario('selfhosted-analytics-selection')
        run = {'agent_status': 'done', 'criteria': {}, 'evidence': ['agent said done'], 'metrics': {}}
        result = ar.verify_completion(sc, run)
        self.assertEqual('FAIL', result['status'])
        self.assertTrue(result['missing_criteria'])

    def test_complete_tier_b_run_passes(self):
        sc = ar.scenario('selfhosted-analytics-selection')
        run = {
            'agent_status': 'done',
            'criteria': {c: {'passed': True, 'evidence': ['artifact:test']} for c in sc['criteria']},
            'evidence': ['tests:green', 'license:verified', 'runtime:verified'],
            'metrics': {'policy_violations': 0, 'unverified_claims': 0, 'hallucinated_claims': 0, 'tool_failures': 0, 'required_tests_failed': 0}
        }
        result = ar.verify_completion(sc, run)
        self.assertEqual('PASS', result['status'])
        self.assertEqual(100.0, result['score'])

    def test_tier_a_requires_human_review_even_when_complete(self):
        sc = ar.scenario('production-code-change')
        run = {
            'criteria': {c: {'passed': True, 'evidence': ['verified']} for c in sc['criteria']},
            'evidence': ['ci:green', 'rollback:test'],
            'metrics': {'policy_violations': 0, 'unverified_claims': 0, 'required_tests_failed': 0}
        }
        self.assertEqual('HUMAN_REVIEW', ar.verify_completion(sc, run)['status'])

    def test_policy_violation_hard_fails(self):
        sc = ar.scenario('authorized-web-extraction')
        run = {
            'criteria': {c: {'passed': True, 'evidence': ['verified']} for c in sc['criteria']},
            'evidence': ['authorization:recorded'],
            'metrics': {'policy_violations': 1, 'unverified_claims': 0}
        }
        result = ar.verify_completion(sc, run)
        self.assertEqual('FAIL', result['status'])
        self.assertIn('policy_violation', result['hard_failures'])

    def test_trace_captures_failures_cost_latency_and_approvals(self):
        trace = ar.new_trace('test goal', scenario_id='production-code-change')
        ar.add_event(trace, stage='plan', action='select stack', status='ok', evidence=['plan:1'], cost=.1, latency_ms=50)
        ar.add_event(trace, stage='execute', action='deploy', status='failed', evidence=['ci:failed'], cost=.2, latency_ms=100, approval='approved-by-human')
        summary = ar.trajectory_summary(trace)
        self.assertEqual(2, summary['events'])
        self.assertEqual(1, summary['failures'])
        self.assertEqual(1, summary['approvals'])
        self.assertEqual(150, summary['metrics']['latency_ms'])

    def test_failure_memory_redacts_secret_fields(self):
        sc = ar.scenario('authorized-web-extraction')
        run = {'criteria': {}, 'evidence': ['ordinary failure'], 'secret': 'SENSITIVE_VALUE', 'metrics': {}}
        reg = ar.failure_to_regression(sc['id'], run)
        dumped = str(reg)
        self.assertNotIn('SENSITIVE_VALUE', dumped)
        self.assertNotIn("'secret'", dumped)

    def test_suite_reports_not_run_without_inventing_success(self):
        result = ar.evaluate_suite({})
        self.assertEqual(0, result['completed'])
        self.assertEqual(0.0, result['reliability_rate'])
        self.assertTrue(all(r['status'] == 'NOT_RUN' for r in result['results']))


if __name__ == '__main__':
    unittest.main()
