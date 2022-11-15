import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_kassapaatteen_alustus_toimii(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kateinen_maksu_riittaa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(vaihtoraha, 500 - 240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 240)
        
    def test_edullinen_kateinen_maksu_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(vaihtoraha, 230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaat_kateinen_maksu_riittaa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(vaihtoraha, 500 - 400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 400)

    def test_maukkaat_kateinen_maksu_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(vaihtoraha, 399)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_kortti_saldo_riittaa(self):
        kortti = Maksukortti(1000)
        success = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(success, True)
        self.assertEqual(str(kortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_kortti_saldo_ei_riita(self):
        kortti = Maksukortti(230)
        success = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(success, False)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.30 euroa")
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukkaat_kortti_saldo_riittaa(self):
        kortti = Maksukortti(500)
        success = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(success, True)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaat_kortti_saldo_ei_riita(self):
        kortti = Maksukortti(399)
        success = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(success, False)
        self.assertEqual(str(kortti), "Kortilla on rahaa 3.99 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahan_lataus_kortille_onnistuu(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, 1000)
        self.assertEqual(str(kortti), "Kortilla on rahaa 11.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000 + 1000)
    
    def test_rahan_lataus_ei_voi_olla_negatiivinen(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, -100)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)      