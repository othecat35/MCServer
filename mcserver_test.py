#!/usr/bin/env python3
from pathlib import Path
import subprocess
import tempfile
import unittest

class TestMCServer(unittest.TestCase):
  script_path = Path.cwd() / "mcserver"

  def setUp(self):
    self.temporary_directory = tempfile.TemporaryDirectory()
    self.test_directory = Path(self.temporary_directory.name)

    self.mcserver_path = self.test_directory / ".mcserver"
    self.configs_path = self.mcserver_path / "configs"

  def tearDown(self):
    self.temporary_directory.cleanup()

  # Test success
  def test_initializing_directory(self):
    output = subprocess.run(
      [self.script_path, "init"],
      cwd=self.test_directory,
      capture_output=True,
      text=True
    )

    self.assertIn("Directory has been initialized", output.stderr)

    # Check directories structure
    self.assertTrue(self.mcserver_path.exists())
    self.assertTrue(self.configs_path.exists())

    # Check files
    self.assertTrue((self.configs_path / "server.json").exists())

  # Test failure
  def test_start_without_initializing(self):
    output = subprocess.run(
      [self.script_path, "start"],
      cwd=self.test_directory,
      capture_output=True,
      text=True
    )

    self.assertIn("Directory '.mcserver' is not found, is this directory not been initialized?", output.stderr)

if __name__ == "__main__":
  unittest.main()
