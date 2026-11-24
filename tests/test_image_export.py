"""Exercise encoded file bytes, dimensions, disclosure and portrait preservation."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

from PIL import Image, features

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/scaling-editorial-image-creator/scripts/export_editorial_image.py'
spec = importlib.util.spec_from_file_location('image_export', SCRIPT)
exporter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exporter)


class EditorialImageExport(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root / 'source.png'
        Image.linear_gradient('L').resize((2048, 1152)).convert('RGB').save(self.source)

    def tearDown(self):
        self.temp.cleanup()

    @unittest.skipUnless(features.check('webp'), 'Pillow WebP codec required')
    def test_title_is_actual_labeled_webp_at_full_resolution(self):
        destination = self.root / 'title.webp'
        result = exporter.export_image(self.source, destination, 'title')
        raw = destination.read_bytes()
        self.assertEqual(raw[:4], b'RIFF')
        self.assertEqual(raw[8:12], b'WEBP')
        with Image.open(destination) as image:
            self.assertEqual(image.format, 'WEBP')
            self.assertEqual(image.size, (1920, 1080))
        self.assertEqual(result['bytes'], len(raw))
        self.assertEqual(result['quality'], 85)
        self.assertEqual(result['ai_label']['type'], 'AI created')
        self.assertFalse(result['ai_label']['visual_legibility_verified'])
        self.assertFalse(result['source_copied_unchanged'])

    def test_title_rejects_png_destination(self):
        with self.assertRaisesRegex(ValueError, '\\.webp'):
            exporter.export_image(self.source, self.root / 'title.png', 'title')
        self.assertFalse((self.root / 'title.png').exists())

    def test_invalid_quality_does_not_create_file(self):
        for quality in (0, 101, True):
            destination = self.root / f'invalid-{quality}.webp'
            with self.assertRaisesRegex(ValueError, 'quality'):
                exporter.export_image(self.source, destination, 'title', quality=quality)
            self.assertFalse(destination.exists())

    def test_unchanged_authentic_avatar_remains_byte_identical_png(self):
        Image.new('RGB', (240, 240), 'gray').save(self.source)
        destination = self.root / 'avatar.png'
        result = exporter.export_image(self.source, destination, 'avatar',
                                       label='none', label_reason='Authentic supplied portrait, unchanged.')
        self.assertEqual(destination.read_bytes(), self.source.read_bytes())
        self.assertEqual(result['format'], 'PNG')
        self.assertEqual(result['dimensions'], [240, 240])
        self.assertTrue(result['source_copied_unchanged'])

    def test_refuses_overwrite_and_keeps_source(self):
        original = self.source.read_bytes()
        destination = self.root / 'existing.webp'
        destination.write_bytes(b'existing asset')
        with self.assertRaises(FileExistsError):
            exporter.export_image(self.source, destination, 'title')
        self.assertEqual(destination.read_bytes(), b'existing asset')
        self.assertEqual(self.source.read_bytes(), original)


if __name__ == '__main__':
    unittest.main()
