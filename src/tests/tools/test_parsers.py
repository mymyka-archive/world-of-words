from unittest import TestCase
from tools.parsers import *


class TestTextParser(TestCase):
    def test_content(self):
        text: str = "gtdAagDtiKC@4r7FbwqCGcod6V4D5sbVXZ%" \
                    "vKYeF3sz8!Fu!S7226&FqY@WscYU&$LUzdF" \
                    "DDH^v4SN3D5 Fd!x4@G KBg^4xUtK 53mx9" \
                    "r8 B QE $ d Fv$K!n Y Maeegn DuW 8K3"
        parser: Parser = TextParser(text)
        self.assertEqual(parser.content, text)


class TestWebsiteParser(TestCase):
    def test_content(self):
        link: str = "https://en.wikipedia.org/wiki/Anime"
        parser: WebsiteParser = WebsiteParser(link)
        self.assertGreater(len(parser.content), 100)
        self.assertEqual(parser.status_code, 200)
