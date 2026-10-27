import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from readme_audit import analyze  # noqa: E402
from preview_concepts import render  # noqa: E402


class AuditTests(unittest.TestCase):
    def test_valid_document_with_local_image(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "screen.svg").write_text("<svg/>", encoding="utf-8")
            doc = root / "README.md"
            doc.write_text("# Project\n\n![Screenshot](screen.svg)\n\n## Usage\n\nDone.\n", encoding="utf-8")
            result = analyze(doc)
            self.assertEqual(result["errors"], [])
            self.assertEqual(result["image_count"], 1)

    def test_missing_image_and_empty_alt(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = Path(tmp) / "README.md"
            doc.write_text("# Example\n\n![](missing.png)\n", encoding="utf-8")
            result = analyze(doc)
            self.assertTrue(any("Missing relative target" in x for x in result["errors"]))
            self.assertTrue(any("empty alt" in x for x in result["warnings"]))

    def test_unbalanced_code_fence(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = Path(tmp) / "README.md"
            doc.write_text("# Example\n\n```sh\ncommand\n", encoding="utf-8")
            self.assertTrue(any("fenced" in x for x in analyze(doc)["errors"]))


class PreviewTests(unittest.TestCase):
    def test_all_directions_render(self):
        for style in ("editorial", "product", "expressive"):
            with self.subTest(style=style):
                value = render(style, "Demo", "True description")
                self.assertIn("<svg ", value)
                self.assertIn("Discussion concept only", value)

    def test_svg_escapes_untrusted_text(self):
        value = render("editorial", "<unsafe>", "A & B")
        self.assertIn("&lt;unsafe&gt;", value)
        self.assertIn("A &amp; B", value)


if __name__ == "__main__":
    unittest.main()
