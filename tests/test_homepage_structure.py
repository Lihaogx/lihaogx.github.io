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
        self.assertIn('extra-item hidden-item{% endif %}', include_source)
        self.assertIn('id="publications-more"', include_source)
        self.assertNotIn('data-lightbox=', include_source)
        self.assertNotIn('pub-filter', include_source)
        self.assertNotIn('hero-eyebrow', include_source)
        self.assertNotIn('pub-thumb', include_source)
        self.assertIn('class="publication-image"', include_source)
        self.assertIn('class="news-tabs"', include_source)
        self.assertIn('data-year="{{ item.date | slice: 0, 4 }}"', include_source)
        self.assertIn('class="research-description"', include_source)
        self.assertIn('years:', homepage_source)
        self.assertIn('name: "Li Hao"', homepage_source)
        self.assertIn('title: "Selected Publications"', homepage_source)
        self.assertNotIn('TDiscNet:', homepage_source)
        self.assertNotIn('DHGAT:', homepage_source)
        self.assertNotIn('ORCID', homepage_source)
        self.assertNotIn('data.cv.file', include_source)
        self.assertIn('ai-google-scholar', include_source)


if __name__ == "__main__":
    unittest.main()
