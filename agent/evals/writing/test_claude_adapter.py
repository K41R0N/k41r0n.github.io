"""Offline official-CLI contract tests. Never launch Claude or use an account."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import subprocess
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('adapter',ROOT/'scripts/local/writing_claude_adapter.py');a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
class AdapterTests(unittest.TestCase):
    def packet(self):return {'role':'reviewer','step':'ogilvy','before':{'path':'synthetic.md','sha256':'synthetic'},'receipt_fields':{'step':'Exact current step'}}
    def test_isolated_argv_no_resume_no_tools(self):
        cmd=a.build_command('/absolute/claude','host-selected-model',{})
        self.assertIn('--restricted',cmd);self.assertIn('--no-session-persistence',cmd)
        self.assertEqual(cmd[cmd.index('--tools')+1],'');self.assertNotIn('--resume',cmd);self.assertNotIn('--continue',cmd)
        self.assertEqual(json.loads(cmd[cmd.index('--mcp-config')+1]),{'mcpServers':{}})
    def test_pin_mismatch_blocks_before_process(self):
        with tempfile.NamedTemporaryFile() as f,patch.object(a.subprocess,'run') as run:
            with self.assertRaisesRegex(ValueError,'pin'):a.run(self.packet(),f.name,'wrong','version','model')
            run.assert_not_called()
    def call(self,p,outer,exitcode=0):
        with tempfile.NamedTemporaryFile() as f:
            f.write(b'synthetic binary');f.flush()
            responses=[subprocess.CompletedProcess([],0,'synthetic version',''),subprocess.CompletedProcess([],0,' '.join(a.REQUIRED_FLAGS),''),subprocess.CompletedProcess([],exitcode,json.dumps(outer),'')]
            with patch.object(a.subprocess,'run',side_effect=responses) as run:
                result=a.run(p,f.name,a.sha(f.name),'synthetic version','synthetic-model')
                actual=run.call_args.kwargs
                self.assertNotIn('ANTHROPIC_API_KEY',actual['env']);self.assertNotIn('CLAUDE_CODE_OAUTH_TOKEN',actual['env'])
                self.assertNotEqual(actual['cwd'],str(Path.cwd()))
                return result
    def test_structured_receipt(self):
        p=self.packet();r={'step':p['step'],'before':p['before'],'after':p['before']}
        self.assertEqual(self.call(p,{'structured_output':{'receipt':r}}),r)
    def test_missing_structured_output_no_fallback(self):
        with self.assertRaisesRegex(ValueError,'structured_output'):self.call(self.packet(),{'result':'looks fine'})
    def test_process_failure_no_fallback(self):
        with self.assertRaisesRegex(ValueError,'process failed'):self.call(self.packet(),{},1)
    def test_changed_artifact_blocked(self):
        p=self.packet();r={'step':p['step'],'before':p['before'],'after':{'path':'different'}}
        with self.assertRaisesRegex(ValueError,'substitute'):self.call(p,{'structured_output':{'receipt':r}})
    def test_writer_stays_held(self):
        with tempfile.NamedTemporaryFile() as f,patch.object(a.subprocess,'run') as run:
            p=self.packet();p['role']='writer'
            with self.assertRaisesRegex(ValueError,'review-only'):a.run(p,f.name,a.sha(f.name),'v','m')
            run.assert_not_called()
