from varasto import Varasto


def nayta_varastot(mehu, olut):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehu}")
    print(f"Olutvarasto: {olut}")
    print("Olut getterit:")
    print(f"saldo = {olut.saldo}")
    print(f"tilavuus = {olut.tilavuus}")
    print(f"paljonko_mahtuu = {olut.paljonko_mahtuu()}")


def testaa_mehu(mehu):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehu.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehu}")
    print("Otetaan 3.14")
    mehu.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehu}")


def testaa_virhetilanteet(mehu, olut):
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    print(Varasto(-100.0))
    print("Varasto(100.0, -50.7)")
    print(Varasto(100.0, -50.7))

    print("olutta.lisaa_varastoon(1000.0)")
    olut.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olut}")

    print("mehua.lisaa_varastoon(-666.0)")
    mehu.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehu}")


def testaa_varastosta_otto(mehu, olut):
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olut.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olut}")

    print("mehua.ota_varastosta(-32.9)")
    saatiin = mehu.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehu}")


def main():
    mehu = Varasto(100.0)
    olut = Varasto(100.0, 20.2)
    nayta_varastot(mehu, olut)
    testaa_mehu(mehu)
    testaa_virhetilanteet(mehu, olut)
    testaa_varastosta_otto(mehu, olut)


if __name__ == "__main__":
    main()
