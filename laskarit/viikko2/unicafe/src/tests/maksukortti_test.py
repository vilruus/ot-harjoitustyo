import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alustuu_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")

    def test_rahan_ottaminen_toimii_kun_riittavasti(self):
        success = self.maksukortti.ota_rahaa(500)
        self.assertEqual(success, True)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_muutu_nostettaessa_yli_saldon(self):
        success = self.maksukortti.ota_rahaa(1500)
        self.assertEqual(success, False)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
