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

    @unittest.skipUnless(features.check('webp'), 'Pillow WebP codec required')
    def test_teaser_pair_uses_same_source_and_crop_and_real_smaller_file(self):
        title = self.root / 'title.webp'
        teaser = self.root / 'teaser.webp'
        main = exporter.export_image(self.source, title, 'title')
        small = exporter.export_image(self.source, teaser, 'teaser')
        self.assertEqual(main['source_sha256'], small['source_sha256'])
        self.assertEqual(main['crop_box'], small['crop_box'])
        self.assertEqual(small['kind'], 'teaser')
        with Image.open(teaser) as image:
            self.assertEqual(image.format, 'WEBP')
            self.assertEqual(image.size, (1536, 864))
        self.assertEqual(small['bytes'], teaser.stat().st_size)
        self.assertFalse(small['ai_label']['visual_legibility_verified'])
        self.assertFalse(small['ai_label']['downstream_crops_verified'])

    @unittest.skipUnless(features.check('webp'), 'Pillow WebP codec required')
    def test_compact_is_small_three_by_two_without_mark_but_keeps_ai_origin(self):
        destination = self.root / 'compact.webp'
        result = exporter.export_image(self.source, destination, 'compact')
        self.assertEqual(result['dimensions'], [480, 320])
        self.assertEqual(result['format'], 'WEBP')
        self.assertEqual(result['ai_label']['type'], 'AI created')
        self.assertFalse(result['ai_label']['visible_label_applied'])
        self.assertIn('120x80', result['ai_label']['omission_scope'])
        with Image.open(self.source) as source:
            # Match the direct source crop/resize with no overlay; do not derive from a labeled WebP.
            reference = source.crop(tuple(result['crop_box'])).resize((480, 320), Image.Resampling.LANCZOS)
            import io
            encoded = io.BytesIO()
            reference.save(encoded, format='WEBP', quality=85, method=6, lossless=False)
        self.assertEqual(destination.read_bytes(), encoded.getvalue())
        main = exporter.export_image(self.source, self.root / 'main.webp', 'title')
        self.assertEqual(result['source_sha256'], main['source_sha256'])
        self.assertNotEqual(result['crop_box'], main['crop_box'])

    @unittest.skipUnless(features.check('webp'), 'Pillow WebP codec required')
    def test_large_medium_teaser_retains_visible_original_artwork(self):
        result = exporter.export_image(self.source, self.root / 'teaser.webp', 'teaser')
        self.assertTrue(result['ai_label']['visible_label_applied'])
        self.assertEqual(result['ai_label']['type'], 'AI created')
        self.assertIn('ai-created-', result['ai_label']['asset'])
        self.assertNotIn('omission_scope', result['ai_label'])

    def test_teaser_rejects_png_and_invalid_quality(self):
        with self.assertRaisesRegex(ValueError, '\\.webp'):
            exporter.export_image(self.source, self.root / 'teaser.png', 'teaser')
        with self.assertRaisesRegex(ValueError, 'quality'):
            exporter.export_image(self.source, self.root / 'teaser.webp', 'teaser', quality=101)

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
