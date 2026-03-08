from pathlib import Path
import unittest


class HomepageStructureTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]

    def test_homepage_uses_data_driven_template_without_hidden_sections(self):
        about_page = (self.root / "_pages" / "about.md").read_text(encoding="utf-8")
        self.assertIn("include homepage.html", about_page)

        data_path = self.root / "_data" / "homepage.yml"
        include_path = self.root / "_includes" / "homepage.html"
        guide_path = self.root / "docs" / "homepage-editing.md"

        self.assertTrue(data_path.exists())
        self.assertTrue(include_path.exists())
        self.assertTrue(guide_path.exists())

        homepage_source = data_path.read_text(encoding="utf-8")
        for section in [
            "site",
            "hero",
            "about",
            "news",
            "research",
            "publications",
            "cv",
        ]:
            self.assertIn(f"{section}:", homepage_source)

        include_source = include_path.read_text(encoding="utf-8")
        for section_id in ['id="about"', 'id="research"', 'id="publications"']:
            self.assertIn(section_id, include_source)

        self.assertNotIn('href="#teaching"', include_source)
        self.assertNotIn('href="#recruitment"', include_source)
        self.assertNotIn('href="#awards"', include_source)
        self.assertNotIn('Join My Lab', include_source)
        self.assertNotIn('Highlights', include_source)
        self.assertNotIn('Academic Service', include_source)
        self.assertNotIn('id="teaching"', include_source)
        self.assertNotIn('id="recruitment"', include_source)
        self.assertNotIn('id="awards"', include_source)
        self.assertNotIn('直博生', include_source)
        self.assertIn('hidden-item{% endif %}" data-cat="{{ pub.category }}"', include_source)
        self.assertIn('id="publications-more"', include_source)
        self.assertIn('data-visible-count="{{ data.publications.initial_visible }}"', include_source)
        self.assertIn("item.classList.toggle('hidden-item', !shouldShow);", include_source)
        self.assertIn('Download CV', homepage_source)
        self.assertIn('/files/CV_en.pdf', homepage_source)
        self.assertTrue((self.root / "files" / "CV_en.pdf").exists())


if __name__ == "__main__":
    unittest.main()
