import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
        
    def test_nolla_tai_negatiivinen_tilavuus_nollataan(self):
        # Nollan tai negatiivisen tilavuuden pitäisi muuttua nollaksi.
        self.assertEqual(Varasto(0).tilavuus, 0.0)
        self.assertEqual(Varasto(-1).tilavuus, 0.0)
        
    def test_negatiivinen_alkusaldo_nollataan(self):
        # Negatiivinen alkusaldo nollataan.
        self.assertEqual(Varasto(10, -1).saldo, 0.0)

    def test_alkusaldo_mahtuu_varastoon(self):
        # Varastoon mahtuva alkusaldo säilyy ennallaan.
        self.assertEqual(Varasto(10, 5).saldo, 5)

    def test_alkusaldo_yli_tilavuuden_tayttaa_varaston(self):
        # Tilavuuden ylittävä alkusaldo rajataan varaston tilavuuteen.
        self.assertEqual(Varasto(10, 11).saldo, 10)

    def test_negatiivista_maaraa_ei_lisata(self):
        # Negatiivisen määrän lisääminen ei muuta saldoa.
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.saldo, 0)

    def test_varasto_tayttyy_jos_lisatty_maara_yli_vapaan_tilan(self):
        # Jos lisättävä määrä ylittää vapaan tilan, varasto täyttyy.
        self.varasto.lisaa_varastoon(11)
        self.assertEqual(self.varasto.saldo, 10)

    def test_negatiivinen_ottomaara_palauttaa_nollan(self):
        # Negatiivisen määrän ottaminen palauttaa nollan eikä muuta saldoa.
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(self.varasto.ota_varastosta(-1), 0.0)
        self.assertEqual(self.varasto.saldo, 5)

    def test_yli_saldon_ottaminen_palauttaa_saatavilla_olevan_maaran(self):
        # Jos pyydetty määrä ylittää saldon, palautetaan kaikki mitä voidaan.
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(self.varasto.ota_varastosta(6), 5)
        self.assertEqual(self.varasto.saldo, 0.0)

    def test_merkkijonoesitys(self):
        # Tarkistetaan varaston merkkijonoesitys.
        self.varasto.lisaa_varastoon(3)
        self.assertEqual(
            str(self.varasto),
            "saldo = 3, vielä tilaa 7"
        )
