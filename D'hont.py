def dividing(mandates, committeevotes, dividedvotes):

    for i in range(1, mandates):

        dividedvotes.append(0)
        dividedvotes[i-1] = committeevotes / i
        
    return dividedvotes

PiSdivided = []
KOdivided = []
TDdivided = []
NLdivided = []
Konfadivided = []

amandates = int(input('Podaj liczbe mandatow w okregu '))
avotes = int(input('Podaj liczbe wszystkich glosow oddanych w okregu '))

PiSvotes = (float(input('Podaj procent glosow uzyskanych przez KW Prawo i Sprawiedliwosc ')) / 100) * avotes
KOvotes = (float(input('Podaj procent glosow uzyskanych przez KKW Koalicja Obywatelska PO .N IPL Zieloni ')) / 100) * avotes
TDvotes = (float(input('Podaj procent glosow uzyskanych przez KKW TRZECIA DROGA PSL-PL2050 SZYMONA HOŁOWNI ')) / 100) * avotes
NLvotes = (float(input('Podaj procent glosow uzyskanych przez KW Nowa Lewica ')) / 100) * avotes
Konfavotes = (float(input('Podaj procent glosow uzyskanych przez KW Konfederacja Wolnosc i Niepodlegosc ')) / 100) * avotes

PiSdivided = dividing(amandates, PiSvotes, PiSdivided)
KOdivided = dividing(amandates, KOvotes, KOdivided)
TDdivided = dividing(amandates, TDvotes, TDdivided)
NLdivided = dividing(amandates, NLvotes, NLdivided)
Konfadivided = dividing(amandates, Konfavotes, Konfadivided)

distributedmandates = [0, 0, 0, 0, 0]

while sum(distributedmandates) < amandates:

    matchedvotes = max(PiSdivided[distributedmandates[0]], KOdivided[distributedmandates[1]], TDdivided[distributedmandates[2]], NLdivided[distributedmandates[3]], Konfadivided[distributedmandates[4]])

    if matchedvotes == PiSdivided[distributedmandates[0]]:

        distributedmandates[0] += 1

    elif matchedvotes == KOdivided[distributedmandates[1]]:

        distributedmandates[1] += 1

    elif matchedvotes == TDdivided[distributedmandates[2]]:

        distributedmandates[2] += 1

    elif matchedvotes == NLdivided[distributedmandates[3]]:

        distributedmandates[3] += 1

    elif matchedvotes == Konfadivided[distributedmandates[4]]:

        distributedmandates[4] += 1

print(f'W tym okregu KW Prawo i Sprawiedliwosc uzyskal {PiSvotes} glosow, a co za tym idzie {distributedmandates[0]} mandatow')
print(f'KKW Koalicja Obywatelska PO .N IPL Zieloni uzyskal {KOvotes} glosow, a co za tym idzie {distributedmandates[1]} mandatow')
print(f'KKW TRZECIA DROGA PSL-PL2050 SZYMONA HOŁOWNI uzyskal {TDvotes} glosow, a co za tym idzie {distributedmandates[2]} mandatow')
print(f'KW Nowa Lewica uzyskal {NLvotes} glosow, a co za tym idzie {distributedmandates[3]} mandatow')
print(f'KW Konfederacja Wolnosc i Niepodleglosc uzyskal {Konfavotes} glosow, a co za tym idzie {distributedmandates[4]} mandatow')
