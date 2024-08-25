from src import db
from typing import List
from datetime import date, time
from src.model import Korisnik, GrupaLeka, Supstanca, Pakovanje, MernaJedinica, Narudzbina, ZapakovanLek, Lek, Sadrzi, StavkaNarudzbine
from .services import stavka_narudzbine_service

def create_grupa_leka_entities():
    grupe_lekova: List[GrupaLeka] = []
    grupe_lekova.append(GrupaLeka(naziv='Analgetik')) #1
    grupe_lekova.append(GrupaLeka(naziv='Antipiretik')) #2
    grupe_lekova.append(GrupaLeka(naziv='Antibiotik')) #3
    grupe_lekova.append(GrupaLeka(naziv='NSAIL')) #4
    grupe_lekova.append(GrupaLeka(naziv='Antihipertenziv')) #5
    grupe_lekova.append(GrupaLeka(naziv='Diutetik')) #6
    grupe_lekova.append(GrupaLeka(naziv='Vitamin')) #7
    grupe_lekova.append(GrupaLeka(naziv='Pomoćno lekovito sredstvo')) #8
    db.session.add_all(grupe_lekova)
    db.session.commit()


def create_supstanca_entities():
    supstance: List[Supstanca] = []
    supstance.append(Supstanca(naziv='Amoksicilin')) #1
    supstance.append(Supstanca(naziv='Metamizol-natrijum ')) #2
    supstance.append(Supstanca(naziv='Ibuprofen')) #3
    supstance.append(Supstanca(naziv='Cefaleksin')) #4
    supstance.append(Supstanca(naziv='Furosemid')) #5
    supstance.append(Supstanca(naziv='Dihlorbenzilalkohol')) #6
    supstance.append(Supstanca(naziv='Amilmetakrezol')) #7
    supstance.append(Supstanca(naziv='Levomentol')) #8
    supstance.append(Supstanca(naziv='Paracetamol')) #9
    supstance.append(Supstanca(naziv='Cefiksim')) #10
    supstance.append(Supstanca(naziv='Perindopril')) #11
    supstance.append(Supstanca(naziv='Amlodipin')) #12
    supstance.append(Supstanca(naziv='Indapamid')) #13
    supstance.append(Supstanca(naziv='VitaminC')) #14

    db.session.add_all(supstance)
    db.session.commit()


def create_pakovanje_entities():
    pakovanja: List[Pakovanje] = []
    pakovanja.append(Pakovanje(vrsta='Tableta')) #1
    pakovanja.append(Pakovanje(vrsta='Kapsula')) #2
    pakovanja.append(Pakovanje(vrsta='Ampula')) #3
    pakovanja.append(Pakovanje(vrsta='Lozenga')) #4
    pakovanja.append(Pakovanje(vrsta='Sirup')) #5
    pakovanja.append(Pakovanje(vrsta='Granule za oralni rastvor')) #6
    pakovanja.append(Pakovanje(vrsta='Disperzibilna tableta')) #7
    pakovanja.append(Pakovanje(vrsta='šumeća tableta')) #8
    db.session.add_all(pakovanja)
    db.session.commit()


def create_merna_jedinica_entities():
    merne_jedinice: List[MernaJedinica] = []
    merne_jedinice.append(MernaJedinica(naziv='mg')) #1
    merne_jedinice.append(MernaJedinica(naziv='mL')) #2
    merne_jedinice.append(MernaJedinica(naziv='mg/mL')) #3
    db.session.add_all(merne_jedinice)
    db.session.commit()


def create_korisnik_entities():
    korisnici: List[Korisnik] = []
    korisnici.append(Korisnik(
                            ime='Ana',
                            prezime='Peric',
                            email='ana.peric@gmail.com',
                            broj_telefona="+381621234424"
                        ))
    korisnici.append(Korisnik(
                            ime='Nikola',
                            prezime='Nikolic',
                            email='nikolicn@gmai.com',
                            broj_telefona="+381636567732"
                        ))
    korisnici.append(Korisnik(
                            ime='Milica',
                            prezime='Pesic',
                            email='mperisic@gmail.com',
                            broj_telefona="+381610003976"
                        ))
    db.session.add_all(korisnici)
    db.session.commit()


def create_lek_entities():
    lekovi: List[Lek] = []
    lekovi.append(Lek(
                        naziv='Amoksicilin HF',
                        opis_namena='Amoksicilin je antibiotik širokog spektra dejstva iz grupe penicilina. Primenjuje se u lečenju velikog broja bakterijskih infekcija, ali i u cilju sprečavanja pojave infekcija nakon hirurških intervencija (npr. vađenje zuba). Takođe se može koristiti u sklopu kombinovane terapije ulkusne bolesti (čir na želucu).',
                        doziranje='Doziranje leka određuje lekar zasnovano na faktorima kao što su uzrok infekcije, njena lokacija, težina, kao i pacijentove godine, telesna masa i opšte zdravstveno stanje, pri čemu lečenje treba biti što kraće. Odrasli i deca težine 40 kg i više mogu uzimati 250-500 mg za akutni bakterijski sinuzitis svakih 8 sati ili 750 mg do 1 g svakih 12 sati, dok se akutni cistitis može lečiti sa 3 g dvaput dnevno jedan dan. Za povišenu temperaturu i grip, doza je 500 mg do 1 g svakih 8 sati. Lajmska bolest se tretira sa 500 mg do 1 g svakih 8 sati, sa maksimumom do 4 g dnevno. Za decu ispod 40 kg, doze variraju od 20 do 90 mg/kg/dan za akutni bakterijski sinuzitis i otitis media, do 100 mg/kg/dan za tifoidnu i paratifoidnu groznicu, dok je za Lajmsku bolest u ranoj fazi 25 do 50 mg/kg/dan, a u kasnijoj fazi do 100 mg/kg/dan. Deca mlađa od šest meseci trebaju koristiti amoksicilin u obliku praška za oralnu suspenziju, a doziranje za decu telesne mase 40 kg ili više je isto kao i za odrasle.',
                        nezeljena_dejstva='Ako tokom upotrebe leka doživite ozbiljne neželjene efekte kao što su alergijske reakcije (otok lica, usana, teškoće u disanju), kožne promene poput crvenkasto-ljubičastih osipa, osip koji može biti praćen bolom u zglobovima i oštećenjem bubrežne funkcije, ili simptome nalik gripu sa osipom i groznicom, odmah prekinite sa uzimanjem leka i potražite hitnu medicinsku pomoć. Ostali teški oblici kožnih reakcija mogu uključivati promene boje kože, plikove, i svrab. Jarisch-Herxheimer reakcija može se javiti prilikom lečenja Lajmske bolesti i manifestuje se groznicom, glavoboljom i osipom. Takođe, mogući su teški poremećaji funkcije jetre, posebno kod dugotrajne terapije. Manje ozbiljni simptomi poput kožnih osipa, otoka na ekstremitetima, mučnine, i dijareje trebaju biti konsultovani sa lekarom. U slučaju pojačanih reakcija ili trajanja simptoma duže od nekoliko dana, neophodno je obratiti se lekaru.',
                        grupa_leka_id=3,
                        ))
    lekovi.append(Lek(
                        naziv='Analgin',
                        opis_namena='Lek Analgin sadrži aktivnu supstancu metamizol natrijum. Metamizol je derivat pirazolona i spada u grupu neopioidnih analgetika. Poseduje analgetičko, antipiretičko, spazmolitičko i antiinflamatorno dejstvo. Lek Analgin je indikovan za kratkotrajnu primenu kod jakih bolova (posttraumatskih i postoperativnih), kada se terapija drugim neopioidnim analgeticima pokaže neuspešnom.',
                        doziranje='Za oralnu upotrebu. Analgin tablete se uzimaju po potrebi. Preporučena doza je jedna tableta svakih 6-8 sati. Izuzetno se može uzeti i po 2 tablete. Maksimalna dnevna doza je 8 tableta.',
                        nezeljena_dejstva='Neka neželjena dejstva mogu biti ozbiljna i zahtevati hitno prekidanje upotrebe leka i traženje medicinske pomoći. Odmah se obratite lekaru ako doživite ozbiljne reakcije preosetljivosti, ozbiljne kožne reakcije kao što su Stevens-Johnsonov sindrom ili toksična epidermalna nekroliza, agranulocitozu, pancitopeniju ili trombocitopeniju. Blagovremeno prekidanje leka može biti ključno za oporavak. Ako primetite simptome kao što su pogoršanje opšteg stanja, groznica, drhtavica, bol u grlu, otežano gutanje ili ponovno javljanje groznice, prestanite sa uzimanjem Analgina i odmah obavite kompletan pregled krvi. Ne nastavljajte sa upotrebom leka bez nadzora lekara.',
                        grupa_leka_id=1,
                        ))
    lekovi.append(Lek(
                        naziv='Brufen',
                        opis_namena='Lek Brufen sadrži ibuprofen, aktivnu supstancu iz grupe nesteroidnih antiinflamatornih lekova (NSAIL), koji ublažavaju bol, oticanje i visoku temperaturu. Brufen se koristi za kratkotrajno ublažavanje blagih do umerenih bolova kao što su zubobolja, menstrualni bolovi, bolovi nakon operacija, glavobolja, uključujući migrenu, i za smanjenje simptoma prehlade i groznice. Takođe se koristi za lečenje reumatskih stanja, uključujući reumatoidni artritis, ankilozirajući spondilitis, osteoartritis, artrozu i giht, kao i za bolove u donjem delu leđa, kapsulitis ("smrznuto rame"), burzitis, tendinitis i tendosinovitis. Preporučuje se konsultacija sa lekarom ukoliko simptomi potraju duže od preporučenog perioda ili se pogoršaju.',
                        doziranje = 'Odrasli i adolescenti stariji od 12 godina (≥40 kg):Uobičajena doza je od 200 mg do 400 mg (5 mL do 10 mL) tri do četiri puta dnevno za Brufen 200 mg/5 mL oralna suspenzija, i od 200 mg do 400 mg (10 mL do 20 mL) tri do četiri puta dnevno za Brufen 100 mg/5 mL sirup. Maksimalna pojedinačna doza ne sme prekoračiti 400 mg, a ukupna dnevna doza ne sme biti veća od 1200 mg za sirup i 2400 mg za oralnu suspenziju. U teškim i akutnim stanjima, doza se može povećati do trenutka kada bol bude pod kontrolom, pri čemu ukupna dnevna doza ne sme da pređe 2400 mg. Deca starija od 3 meseca (preko 5 kg telesne mase): Dnevno doziranje je 20 – 30 mg/kg telesne mase podeljeno u više doza, kako za Brufen 100 mg/5 mL sirup tako i za Brufen 200 mg/5 mL oralna suspenzija.',
                        nezeljena_dejstva='Lek Brufen može izazvati različite neželjene efekte, uglavnom gastrointestinalne prirode. Postoji rizik od razvoja peptičkih ulkusa, perforacija ili gastrointestinalnog krvarenja, što može biti fatalno, naročito kod starijih pacijenata. Uobičajeni simptomi uključuju mučninu, povraćanje, proliv, nadimanje, zatvor, bol u stomaku, crnu stolicu nalik katranu, povraćanje krvi, i ulcerozni stomatitis. Moguće je i pogoršanje kolitisa i Kronove bolesti. Gastritis je ređe zabeležen. Upotreba visokih doza Brufena (2400 mg dnevno) može povećati rizik od srčanog udara ili šloga. Ostali efekti uključuju oticanje, visok krvni pritisak i slabost srca. Često se javljaju gorušica, vrtoglavica, umor i otežano varenje.',
                        grupa_leka_id=4,
                        ))
    lekovi.append(Lek(
                        naziv='Cefaleksin_HF',
                        opis_namena='Lek Cefaleksin HF je antibiotik iz grupe cefalosporina koji sadrži cefaleksin kao aktivnu supstancu. Primarno se koristi za lečenje različitih infekcija izazvanih mikroorganizmima osjetljivim na ovaj lek. Njegova primena obuhvata lečenje infekcija organa za disanje kao što su tonzilitis, faringitis, sinuzitis i bronhitis, infekcije srednjeg uha poput otitis media, te infekcije kože i mekih tkiva uključujući mišiće. Takođe se koristi za tretman infekcija kostiju i zglobova, mokraćnih puteva i polnih organa, uključujući cistitis i akutnu upalu prostate (prostatitis), kao i za lečenje infekcija zuba.',
                        doziranje='Lek Cefaleksin HF je namenjen za oralnu upotrebu i treba ga uzimati tačno prema uputima lekara. Uobičajena doza za odrasle varira od 1-4 g dnevno, podeljeno na više doza, sa 500 mg na svakih 8 sati za većinu infekcija. Za infekcije kože, streptokokni faringitis i blage infekcije mokraćnih puteva, doziranje je 250 mg na svakih 6 sati ili 500 mg na svakih 12 sati. U teškim slučajevima ili kada su mikroorganizmi manje osetljivi, može biti potrebna veća doza, a kod doza većih od 4 g dnevno, razmatra se upotreba intravenskih ili intramuskularnih cefalosporina. Kod starijih osoba i onih sa oštećenjem bubrega doziranje se prilagođava. Za decu, doza se određuje na osnovu telesne mase, obično između 25-50 mg/kg dnevno, podeljeno na više doza, a kod odojčadi i male dece koriste se granule za oralnu suspenziju. Kod težih infekcija kod dece, doza se može udvostručiti. Lečenje infekcija izazvanih beta-hemolitičkim streptokokom treba da traje najmanje 10 dana.',
                        nezeljena_dejstva='Lek Cefaleksin HF može izazvati neželjene efekte, uključujući ozbiljne alergijske reakcije kao što su osip, svrab, oticanje lica i očnih kapaka, teškoće u disanju koje mogu napredovati do anafilakse. Ukoliko doživite ove simptome, hitno prekinite sa uzimanjem leka i obratite se lekaru. Retko se mogu pojaviti teške kožne reakcije kao što su erythema multiforme, Stevens-Johnsonov sindrom, toksična epidermalna nekroliza i AGEP, koje zahtevaju hitnu medicinsku intervenciju. Gastrointestinalni poremećaji poput teškog proliva, pseudomembranoznog kolitisa, mučnine i povraćanja takođe su mogući. Pored toga, mogu se javiti poremećaji krvi kao što su eozinofilija, neutropenija, trombocitopenija i hemolitička anemija, što može zahtevati analizu krvi.',
                        grupa_leka_id=3,
                        ))
    lekovi.append(Lek(
                        naziv='Lasix',
                        opis_namena='Lek Lasix sadrži aktivnu supstancu furosemid. Lek Lasix pripada grupi lekova koji se zovu diuretici (lekovi za izbacivanje tečnosti). Lek Lasix se upotrebljava za odstranjivanje viška tečnosti iz organizma. Daje se kada se nakupi prekomerna količina vode u organizmu. Lasix tablete se koriste kada imate puno vode oko srca, pluća, jetre ili bubrega. Lek Lasix Vam pomaže da izbacite višak tečnosti iz organizma, putem urina. Ako se višak vode iz organizma ne ukloni, može nepovoljno uticati na srce, krvne sudove, pluća, bubrege ili jetru.',
                        doziranje = 'Pratite uputstva Vašeg lekara o tome kada i kako da uzimate lek Lasix. Ako imate bilo kakve nedoumice, posavetujte se sa Vašim lekarom ili farmaceutom. Za odrasle i starije osobe, uobičajena doza je 2 tablete dnevno, ali stariji pacijenti mogu početi terapiju s nižim dozama. Kod dece, doza se određuje na osnovu telesne mase (1-3 mg/kg telesne mase dnevno), ali ne prelazi maksimalnu dozu od 1 tablete dnevno. Ukoliko vam lekar nije dao drugačija uputstva, uzimajte lek ujutru i popijte ga sa čašom vode.',
                        nezeljena_dejstva='Hitno se obratite lekaru ako doživite simptome kao što su alergijske reakcije uključujući osip, svrab, iznenadni pad krvnog pritiska, ubrzani rad srca, otežano disanje, ili ako primetite modrice, infekcije, slabost, umor, što može ukazivati na probleme sa krvnim ćelijama. Veoma česta neželjena dejstva uključuju hipovolemiju sa simptomima kao što su ortostatska hipotenzija, vrtoglavica ili nesvestica, povećane vrednosti triglicerida, serumskog kreatinina, promene u nivoima mineralnih soli i dehidraciju. Česta neželjena dejstva obuhvataju povećanje gustine krvi, smanjenje nivoa kalijuma i natrijuma, hepatičnu encefalopatiju kod pacijenata sa oboljenjem jetre, blagi porast mokraćne kiseline koji može izazvati giht, povišeni holesterol u krvi i povećanu produkciju urina.',
                        grupa_leka_id=6,
                        ))
    lekovi.append(Lek(
                        naziv='Neo-angin bez šećera',
                        opis_namena='Lek neo-angin bez šećera spada u grupu lekova koji se zovu antiseptici. Koristi se kao dodatna terapija zapaljenja sluzokože ždrela, praćene tipičnim simptomima poput bola u grlu, crvenila i otoka. Lek je namenjen za odrasle i decu stariju od 6 godina.',
                        doziranje = 'Uvek uzimajte ovaj lek tačno onako kako je navedeno u ovom uputstvu ili kako Vam je to objasnio Vaš lekar ili farmaceut. Ukoliko niste sigurni proverite sa Vašim lekarom ili farmaceutom. 3 od 4 Ukoliko nije drugačije propisano, odrasli i deca starija od 6 godina treba da na svaka 2 do 3 sata u ustima polako otope jednu lozengu. Maksimalna dnevna doza je 6 lozengi. Bez preporuke lekara ovaj lek ne treba uzimati duže od 3 do 4 dana. Lek neo-angin bez šećera je namenjen za oromukozalnu upotrebu.',
                        nezeljena_dejstva='Nakon upotrebe ovog leka primećena su sledeća neželjena dejstva: Veoma retka neželjena dejstva (mogu da se jave kod najviše 1 na 10000 pacijenata koji uzimaju lek): iritacija oralne sluzokože i sluzokože želuca kao što su otežano varenje, mučnina. Nepoznata učestalost (ne može se proceniti na osnovu dostupnih podataka): alergijske reakcije kao što su oticanje usta, jezika i usana, osip. Ukoliko Vam se javi alergijska reakcija, odmah prekinite sa uzimanjem leka i konsultujte se sa svojim lekarom ili farmaceutom.',
                        grupa_leka_id=8,
                        ))
    lekovi.append(Lek(
                        naziv='Ospamox DT',
                        opis_namena='Lek Ospamox DT, čija je aktivna supstanca amoksicilin, trihidrat, pripada grupi penicilinskih antibiotika. Lek Ospamox DT se primenjuje u terapiji infekcija čiji su izazivači bakterije u različitim delovima tela. Lek Ospamox DT se kombinaciji sa drugim lekovima može koristiti i za lečenje čira na želucu.',
                        doziranje = 'Lek Ospamox DT se uzima tačno prema uputstvima lekara ili farmaceuta. Tabletu treba rastvoriti u čaši vode i odmah popiti, a doze rasporediti tokom dana sa najmanje 4 sata između njih. Za decu telesne mase manje od 40 kg, doza je 40 do 90 mg/kg dnevno, podeljeno na dve ili tri doze, sa maksimalnom dozom od 100 mg/kg dnevno. Za odrasle i decu težu od 40 kg, uobičajene doze amoksicilina variraju od 250 mg do 500 mg tri puta dnevno ili 750 mg do 1 g na svakih 12 sati, u zavisnosti od težine infekcije. Za teške infekcije može biti potrebno 750 mg do 1 g tri puta na dan, dok se za infekcije mokraćnih puteva može koristiti 3 g dva puta na dan. Lajmska bolest se leči sa 4 g dnevno u ranom stadijumu, do 6 g dnevno u kasnijem stadijumu. Za sprečavanje srčane infekcije pri operaciji i lečenje čira na želucu koriste se specifične doze u kombinaciji sa drugim lekovima. Maksimalna preporučena dnevna doza je 6 g.',
                        nezeljena_dejstva='Ako uzimate lek Ospamox DT i primetite bilo koju od sledećih ozbiljnih neželjenih reakcija, odmah prestanite s upotrebom leka i potražite medicinsku pomoć: teške alergijske reakcije kao što su svrab, osip, oticanje lica ili teškoće u disanju; ozbiljne kožne reakcije poput erythema multiforme, Stevens-Johnsonovog sindroma, toksične epidermalne nekrolize; simptome poput groznice, bolova u zglobovima, povećanih limfnih čvorova, ili teške reakcije gastrointestinalnog sistema kao što su težak proliv sa mogućim prisustvom krvi, zapaljenje debelog creva, i teške poremećaje funkcije jetre. Česta neželjena dejstva uključuju kožni osip, mučninu i proliv. Povremeno neželjeno dejstvo je povraćanje. Preporučuje se unos dovoljne količine tečnosti za sprečavanje pojave kristala u mokraći.',
                        grupa_leka_id=3,
                        ))
    lekovi.append(Lek(
                        naziv='Panadol Advanced',
                        opis_namena='Lek Panadol Advance se koristi za brzo i efikasno otklanjanje glavobolje, zubobolje, bola u leđima, reumatskog i mišićnog bola, i menstrualnog bola. Lek Panadol Advance pomaže u otklanjanju bola u grlu i groznice, bolova u zglobovima i bolova kod prehlade i gripa. Lek Panadol Advance takođe pomaže u otklanjanju bola kod osteoartritisa, dijagnostikovanog od strane lekara. Aktivni sastojak leka Panadol Advance je paracetamol koji je služi za otklanjanje bola i takođe snižava povišenu temperaturu kada imate groznicu.',
                        doziranje = 'Odrasli, stariji i deca iznad 12 godina: Uzmite 1 do 2 tablete sa dovoljnom količinom vode 3-4 puta dnevno, ukoliko je potrebno. Vremenski razmak između uzimanja tableta ne sme da bude manji od 4 sata. Ne sme se uzeti više od 8 tableta u toku 24 časa. Deca uzrasta 6-12 godina: Dati pola do jednu tabletu 3-4 puta dnevno, ukoliko je potrebno. Vremenski razmak između uzimanja tableta ne sme da bude manji od 4 sata. Ne sme se uzeti više od 4 tablete u toku 24 časa.',
                        nezeljena_dejstva='Prestanite da uzimate lek i obratite se odmah Vašem lekaru ili farmaceutu ukoliko ste doživeli neka od navedenih neželjenih dejstava: Alergijske reakcije (kao što je osip na koži, svrab, nekad problem sa disanjem ili otok usana, jezika, grla, lica) ili nedostatak vazduha. Kožni osip, perutanje ili ljušćenje kože, ulceracije (oštećenja sluzokože) i mekih tkiva u ustima. Problemi sa disanjem. Veća je verovatnoća da se ovi simptomi jave ukoliko ste pre imali iste ili slične simptome pri upotrebi drugih lekova protiv bolova kao što su aspirina ili nesteroidni antireumatici. Pojava modrica ili krvarenja koja se ne može objasniti.',
                        grupa_leka_id=2,
                        ))
    lekovi.append(Lek(
                        naziv='Pancef',
                        opis_namena='Lek Pancef je antibiotik koji pripada grupi lekova zvanoj cefalosporini, i sadrži aktivnu supstancu cefiksim. Koristi se za lečenje infekcija izazvanih bakterijama osetljivim na ovaj antibiotik: infekcija srednjeg uha (otitis media), infekcija gornjih disajnih puteva uključujući nos i sinuse (sinuzitis), zapaljenja grla (tonzilitis, faringitis), infekcija donjih disajnih puteva kao što su bronhitis i pneumonija, te infekcije urinarnog sistema uključujući zapaljenje mokraćne bešike (cistitis) i infekcije bubrega.',
                        doziranje = 'Uvek uzimajte lek Pancef tačno kako vam je objasnio Vaš lekar ili farmaceut. Lek Pancef, film tablete, namenjene su za oralnu upotrebu: tabletu progutajte sa odgovarajućom količinom vode. Pažljivo pročitajte uputstvo i pitajte Vašeg farmaceuta ako niste sigurni koju dozu treba da uzmete. Lek treba uzimati u isto vreme svakog dana, obično trajanje terapije je 7 dana, ali Vaš lekar može da produži lečenje do 14 dana. Uobičajena doza za odrasle i decu stariju od 10 godina ili težu od 50 kg je jedna tableta od 400 mg dnevno, kao pojedinačna doza ili podeljena u dve jednake doze od 200 mg (1/2 tablete).',
                        nezeljena_dejstva='Prestanite sa uzimanjem leka i odmah se obratite lekaru ako primetite alergijske reakcije koje uključuju osip, bol u zglobovima, otežano gutanje ili disanje, otok usana, lica, grla ili jezika, ili ako se pojave simptomi kao što su plikovi ili krvarenje kože oko usana, očiju, nosa, genitalija praćeno bolom, glavoboljom i povišenom temperaturom što može ukazivati na Stevens-Johnsonov sindrom. Ozbiljni osipi koji uključuju plikove na nogama, rukama, licu i usnama mogu ukazivati na toksičnu epidermalnu nekrolizu. Ako imate sklonost ka čestim infekcijama, modrice ili krvarenje, žuticu, težak proliv, konvulzije, promene u radu bubrega ili simptome encefalopatije, odmah se obratite lekaru. Dugotrajni ili ozbiljni simptomi poput mučnine, povraćanja, bolova u stomaku, proliva, glavobolje ili vrtoglavice zahtevaju medicinsku pažnju.',
                        grupa_leka_id=3,
                        ))
    lekovi.append(Lek(
                        naziv='Spedifen',
                        opis_namena='Lek Spedifen sadrži ibuprofen u formi arginat soli i pripada grupi nesteroidnih antiinflamatornih lekova (NSAIL) koji ublažavaju bolove, sprečavaju zapaljenja i snižavaju telesnu temperaturu. Koristi se za lečenje blagog do umerenog bola kod zubobolje, glavobolje, menstrualnog bola, neuralgije, bolova u kostima i mišićima, kao i za simptomatsko lečenje povišene telesne temperature i simptoma gripe. Ako se simptomi ne poboljšaju ili se pogoršaju nakon 4 dana kod bolova ili 3 dana kod temperature, potrebno je konsultovati lekara.',
                        doziranje = 'Odrasli i deca starija od 12 godina: Preporučena doza je 400 mg (jedna kesica), 2-3 puta dnevno, tako da maksimalna dnevna doza ne pređe 1200 mg (3 kesice tokom 24 h). Lek nije namenjen za upotrebu kod dece mlađe od 12 godina, jer je pojedinačna doza leka veća od one preporučene za tu starosnu grupu. Adolescenti uzrasta od 12 do 18 godina: posavetujte se s lekarom ukoliko treba da koristite lek duže od 3 dana ili ako Vam se stanje pogorša. Stariji pacijenti: ukoliko spadate u ovu grupu, pridržavajte se najmanje preporučene doze. Uvek se posavetujte sa lekarom, jer se može javiti potreba da se doza leka dodatno smanji. Pacijenti sa oštećenom funkcijom bubrega, jetre ili srca: Ukoliko imate problema sa bubrezima, jetrom ili srcem, uvek se posavetujte sa lekarom, jer se može javiti potreba da se doza leka dodatno smanji. U slučaju teške insuficijencije bubrega, jetre ili srca, lek Spedifen ne smete koristiti (videti odeljak “Lek Spedifen ne smete uzimati”).',
                        nezeljena_dejstva='Spedifen 400 može izazvati neželjena dejstva, iako se ona ne javljaju kod svih pacijenata. Ukoliko primetite bilo koje ozbiljno neželjeno dejstvo ili neko koje nije navedeno u uputstvu, obavestite svog lekara ili farmaceuta. Rizik od neželjenih dejstava može se smanjiti upotrebom najniže efikasne doze u najkraćem potrebnom periodu. Veoma česta neželjena dejstva uključuju otežano varenje i proliv. Česta neželjena dejstva obuhvataju bolove u stomaku, mučninu, gasove, gorušicu, nelagodnost u stomaku, glavobolje, vrtoglavice, kožne poremećaje i osip.',
                        grupa_leka_id=4,
                        ))
    lekovi.append(Lek(
                        naziv='Triplixam',
                        opis_namena='Lek Triplixam je antihipertenzivni lek koji kombinuje tri aktivne supstance: perindopril, indapamid i amlodipin, koristi se za terapiju povišenog krvnog pritiska. Pacijenti koji su prethodno uzimali perindopril/indapamid i amlodipin kao odvojene tablete, sada mogu koristiti jednu tabletu Triplixam koja obuhvata sve tri supstance. Perindopril, kao inhibitor angiotenzin konvertujućeg enzima, širi krvne sudove i olakšava rad srca u pumpingu krvi. Indapamid, diuretik iz grupe derivata sulfonamida sa indolnim prstenom, povećava izlučivanje urina ali manje intenzivno od ostalih diuretika. Amlodipin, blokator kalcijumskih kanala iz grupe dihidropiridina, opušta krvne sudove, što omogućava lakši protok krvi. Ove supstance zajedno efikasno kontrolišu krvni pritisak.',
                        doziranje = 'Uvek uzimajte ovaj lek tačno onako kako Vam je to objasnio Vaš lekar ili farmaceut. Ukoliko niste sigurni, proverite sa Vašim lekarom ili farmaceutom. Tabletu progutajte sa čašom vode, po mogućstvu ujutru, pre obroka. Vaš lekar će odlučiti koja je doza odgovarajuća za Vas. Uobičajena doza je jedna tableta dnevno.',
                        nezeljena_dejstva='Ako primetite bilo koje od sledećih ozbiljnih neželjenih dejstava, odmah prestanite sa uzimanjem leka i obratite se lekaru: iznenadno šištanje, bol u grudima, oticanje kapaka, lica ili usana, teškoće pri disanju ili angioedem, teške kožne reakcije kao što su intenzivan osip, koprivnjača, jak svrab, plikovi, Stevens-Johnsonov sindrom, toksična epidermalna nekroliza, teška vrtoglavica ili nesvestica zbog niskog krvnog pritiska, srčani udar, životno ugrožavajući nepravilni srčani ritam, ili zapaljenje pankreasa sa jakim bolom u stomaku. Neželjena dejstva variraju u učestalosti, od veoma retkih, kao što su neki kožni uslovi i srčani problemi, do čestih poput niskog krvnog pritiska i veoma čestih poput edema.',
                        grupa_leka_id=5,
                        ))
    lekovi.append(Lek(
                        naziv='Vitamin C',
                        opis_namena='Biofar vitamin C 1000 mg je dodatak ishrani kojiima antioksidantno dejstvo i obezbeđuje visoke doze vitamina C organizmu. Potreba za ovim vitaminom se javlja kod pušača, osoba kojima je oslabljen imuni sistem i za poboljšanje opšteg stanja odraslih osoba i adolescenata.',
                        doziranje = 'Jednu tabletu dnevno rastvoriti u velikoj čaši vode, poželjno je popiti ujutro, nakon doručka. Nemojte prekoračiti preporučenu dnevnu dozu. Dodaci ishrani se ne mogu koristiti kao zamena za uravnoteženu ishranu i zdrav način života.',
                        nezeljena_dejstva='Lek Vitamin C se obično dobro podnosi. U retkim slučajevima mogu da se jave stomačne tegobe (mučnina , grčevi, nadutost) praćene prolivom. Ukoliko bolujete od hiperoksalurije (visok nivo oksalata u mokraći), lek Vitamin C ne smete da koristite jer pri primeni visokih doza može doći do povećanja nivoa oksalata u mokraći i formiranja oksalatnih bubrežnih kamenaca. Pojava bola u predelu bubrega, krvi u urinu i učestalog i bolnog mokrenja ukazuje na pojavu kamena u bubregu. Ako imate deficit glukozo-6-fosfat dehidrogenaze, visoke doze leka Vitamin C mogu dovesti do hemolize (razgradnje crvenih krvnih zrnaca). Moguća je pojava alergijske reakcije na vitamin C ili na neku od pomoćnih supstanci preparata.',
                        grupa_leka_id=7,
                        ))
    db.session.add_all(lekovi)
    db.session.commit()


def create_sadrzi_entities():
    sadrzi_podaci: List[Sadrzi] = []
    sadrzi_podaci.append(Sadrzi(
                            lek_id=1,
                            supstanca_id=1,
                        ))
    sadrzi_podaci.append(Sadrzi(
                            lek_id=2,
                            supstanca_id=2,
                        ))
    sadrzi_podaci.append(Sadrzi(
                            lek_id=3,
                            supstanca_id=3,
                        ))
    sadrzi_podaci.append(Sadrzi(
                            lek_id=4,
                            supstanca_id=4,
                        ))
    sadrzi_podaci.append(Sadrzi(
                            lek_id=5,
                            supstanca_id=5,
                        ))
    sadrzi_podaci.append(Sadrzi(
                            lek_id=6,
                            supstanca_id=6,
                        ))
    sadrzi_podaci.append(Sadrzi(
                            lek_id=6,
                            supstanca_id=7,
                        ))
    sadrzi_podaci.append(Sadrzi(
                            lek_id=6,
                            supstanca_id=8,
                        ))
    sadrzi_podaci.append(Sadrzi(
                            lek_id=7,
                            supstanca_id=1,
                        ))
    sadrzi_podaci.append(Sadrzi(
                            lek_id=8,
                            supstanca_id=9,
                        ))
    sadrzi_podaci.append(Sadrzi(
                            lek_id=9,
                            supstanca_id=10,
                        ))
    sadrzi_podaci.append(Sadrzi(
                            lek_id=10,
                            supstanca_id=3,
                        ))
    sadrzi_podaci.append(Sadrzi(
                            lek_id=11,
                            supstanca_id=11,
                        ))
    sadrzi_podaci.append(Sadrzi(
                            lek_id=11,
                            supstanca_id=12,
                        ))
    sadrzi_podaci.append(Sadrzi(
                            lek_id=11,
                            supstanca_id=13,
                        ))
    sadrzi_podaci.append(Sadrzi(
                            lek_id=12,
                            supstanca_id=14,
                        ))
    db.session.add_all(sadrzi_podaci)
    db.session.commit()


def create_narudzbina_entities():
    narudzbine: List[Narudzbina] = []
    narudzbine.append(Narudzbina(
                            datum=date(2023, 7, 20),
                            vreme=time(14, 34),
                            adresa='Cara Dušana 30, 11000 Beograd',
                            korisnik_id=2
                        ))
    narudzbine.append(Narudzbina(
                            datum=date(2023, 8, 8),
                            vreme=time(10, 5),
                            adresa='Miloša Trebinjca 96, 26000 Pančevo',
                            korisnik_id=3
                        ))
    narudzbine.append(Narudzbina(
                            datum=date(2023, 8, 9),
                            vreme=time(20, 20),
                            adresa='Şavska 23, 11000 Beograd',
                            korisnik_id=1
                        ))
    db.session.add_all(narudzbine)
    db.session.commit()


def create_zapakovan_lek_entities():
    zapakovani_lekovi: List[ZapakovanLek] = []
    zapakovani_lekovi.append(ZapakovanLek(
                            lek_id=1,
                            pakovanje_id=2,
                            merna_jedinica_id=1,
                            zaliha=100,
                            jacina='500',
                            kolicina=16,
                            cena=151.00,
                            url='static/resources/lekovi/Amoksicilin_HF_500mg.jpg'
                        ))
    zapakovani_lekovi.append(ZapakovanLek(
                            lek_id=2,
                            pakovanje_id=1,
                            merna_jedinica_id=1,
                            zaliha=100,
                            jacina='500',
                            kolicina=10,
                            cena=599.42,
                            url='static/resources/lekovi/Analgin.jpg',
                        ))
    zapakovani_lekovi.append(ZapakovanLek(
                            lek_id=3,
                            pakovanje_id=5,
                            merna_jedinica_id=3,
                            zaliha=100,
                            jacina='100/5',
                            kolicina=100,
                            cena=293.00,
                            url='static/resources/lekovi/Brufen_100mg.jpg',
                        ))
    zapakovani_lekovi.append(ZapakovanLek(
                            lek_id=3,
                            pakovanje_id=5,
                            merna_jedinica_id=3,
                            zaliha=100,
                            jacina='200/5',
                            kolicina=150,
                            cena=530.00,
                            url='static/resources/lekovi/Brufen_200mg.jpg',
                        ))
    zapakovani_lekovi.append(ZapakovanLek(
                            lek_id=4,
                            pakovanje_id=2,
                            merna_jedinica_id=1,
                            zaliha=100,
                            jacina='500',
                            kolicina=150,
                            cena=274.00,
                            url='static/resources/lekovi/Cefaleksin_HF_500mg.jpg',
                        ))
    zapakovani_lekovi.append(ZapakovanLek(
                            lek_id=5,
                            pakovanje_id=1,
                            merna_jedinica_id=1,
                            zaliha=100,
                            jacina='40',
                            kolicina=150,
                            cena=74.00,
                            url='static/resources/lekovi/Lasix_40mg.jpg',
                        ))
    zapakovani_lekovi.append(ZapakovanLek(
                            lek_id=6,
                            pakovanje_id=4,
                            merna_jedinica_id=1,
                            zaliha=100,
                            jacina='1,25/0,6/5,72',
                            kolicina=150,
                            cena=648.30,
                            url='static/resources/lekovi/Neo_angin.jpg',
                        ))
    zapakovani_lekovi.append(ZapakovanLek(
                            lek_id=7,
                            pakovanje_id=7,
                            merna_jedinica_id=1,
                            zaliha=100,
                            jacina='1000',
                            kolicina=150,
                            cena=312.10,
                            url='static/resources/lekovi/Ospamox_1000mg.jpg',
                        ))
    zapakovani_lekovi.append(ZapakovanLek(
                            lek_id=8,
                            pakovanje_id=1,
                            merna_jedinica_id=1,
                            zaliha=100,
                            jacina='500',
                            kolicina=100,
                            cena=201.00,
                            url='static/resources/lekovi/Panadol_Advanced.jpg',
                        ))
    zapakovani_lekovi.append(ZapakovanLek(
                            lek_id=9,
                            pakovanje_id=1,
                            merna_jedinica_id=1,
                            zaliha=100,
                            jacina='400',
                            kolicina=100,
                            cena=498.00,
                            url='static/resources/lekovi/Pancef_400mg.jpg',
                        ))
    zapakovani_lekovi.append(ZapakovanLek(
                            lek_id=10,
                            pakovanje_id=6,
                            merna_jedinica_id=1,
                            zaliha=100,
                            jacina='400',
                            kolicina=100,
                            cena=284.36,
                            url='static/resources/lekovi/Spedifen_400mg.jpg',
                        ))
    zapakovani_lekovi.append(ZapakovanLek(
                            lek_id=11,
                            pakovanje_id=1,
                            merna_jedinica_id=1,
                            zaliha=100,
                            jacina='5/5/1,25',
                            kolicina=100,
                            cena=1095.00,
                            url='static/resources/lekovi/Triplixam.jpg',
                        ))
    zapakovani_lekovi.append(ZapakovanLek(
                            lek_id=12,
                            pakovanje_id=8,
                            merna_jedinica_id=1,
                            zaliha=100,
                            jacina='1000',
                            kolicina=100,
                            cena=419.00,
                            url='static/resources/lekovi/Vitamin_C.jpg',
                        ))
    db.session.add_all(zapakovani_lekovi)
    db.session.commit()


def create_stavka_narudzbine_entities():
    stavka_narudzbine_service.create(zapakovan_lek_id=2,
                                narudzbina_id=1,
                                kolicina=10) 
    stavka_narudzbine_service.create(
                                zapakovan_lek_id=1,
                                narudzbina_id=2,
                                kolicina=5)