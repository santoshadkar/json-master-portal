import os
import re
import unittest

class TestJsonMasterPortal(unittest.TestCase):
    def setUp(self):
        self.portal_path = os.path.join(os.path.dirname(__file__), "..", "index.html")
        self.assertTrue(os.path.exists(self.portal_path), "index.html does not exist in root directory!")
        with open(self.portal_path, "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_required_sections_exist(self):
        """Verify that all 9 enterprise sections are properly defined as sibling sections."""
        expected_sections = [
            "tab-fundamentals",
            "tab-variants",
            "tab-hallucination",
            "tab-mitigation",
            "tab-prompts",
            "tab-playground",
            "tab-synthesizer",
            "tab-sdks",
            "tab-security"
        ]
        for sec in expected_sections:
            pattern = rf'<section[^>]+id=["\']{sec}["\']'
            self.assertTrue(re.search(pattern, self.content), f"Missing section #{sec}")

    def test_section_tags_balanced(self):
        """Ensure every <section> opening tag has a matching </section> closing tag."""
        open_sections = len(re.findall(r'<section\b', self.content))
        close_sections = len(re.findall(r'</section>', self.content))
        self.assertEqual(open_sections, close_sections, f"Mismatched section tags: {open_sections} open vs {close_sections} close")

    def test_synthesizer_presets_exist(self):
        """Verify synthesizer preset entities exist in JavaScript."""
        self.assertIn("ecommerce:", self.content)
        self.assertIn("clinical:", self.content)
        self.assertIn("financial:", self.content)
        self.assertIn("user:", self.content)

    def test_no_unrendered_latex_math(self):
        """Ensure no raw LaTeX math tokens are accidentally present in text nodes."""
        self.assertNotIn("$-\\infty$", self.content)
        self.assertNotIn("$t_{100}$", self.content)
        self.assertNotIn("$t_{4096}$", self.content)

    def test_ai_sdk_snippets_present(self):
        """Verify key modern AI framework integrations are documented."""
        self.assertIn("google.generativeai", self.content)
        self.assertIn("client.beta.chat.completions.parse", self.content)
        self.assertIn("instructor.from_openai", self.content)
        self.assertIn("anthropic", self.content)

    def test_security_section_topics(self):
        """Verify security vulnerabilities and streaming are documented."""
        self.assertIn("Prototype Pollution", self.content)
        self.assertIn("JSON Bomb", self.content)
        self.assertIn("partial-json", self.content)

if __name__ == "__main__":
    unittest.main()
