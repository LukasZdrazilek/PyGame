ZATÍM BEZ NÁZVU

Jedná se o 2D skákačku na motivy hry Jump King (2019, studio Nexile). 
Ovládá se klávesy "A" pro chůzi vlevo, "D" pro chůzi vpravo, držení "SPACE" pro skok a "ESC" pro uložení a vypnutí.
Hra je zajímavá svým ovládáním a obtížností, kdy nabíjíte skok držením mezerníku a nikdy přímo nevidíte, jak daleko vyskočíte.
Zdánlivě jednoduchý koncept (mnou samozřejmě nevymyšlený) dokáže zabavit na několik hodin, protože mapa (jednotlivé obrazovky) je navržená tak, že téměř vždy můžete odkudkoliv spadnout až na úplný začátek.

Ve hře je mimo jiné:
    časomíra 
    mluvící NPC, sloužící spíše pro pobavení (snad), nemá ve hře žádnou větší funkci
    sbírání 'coinů', které můžete darovat NPC a to vám naoplátku řekne životní moudro. Sbíráním se dá také trackovat progress (vždy 1 coin na obrazovce)
    ukládání postupu (pouze v .txt souboru), které ukládá pozici hráče, časomíru a posbírané coiny

Není přímo v gameplayi, ale pro jednodušší, přehlednější a celkově efektivnější stavění mapy (obrazovek) jsem vymyslel funkci, která načítá .txt soubor a dle určených parametrů přidává na obrazovku kolize
daných zdí nebo platforem. Každou obrazovku pak tedy stačí 'napsat' v texťáku a není potřeba nic víc rešit (dle potřeby testování je k dispozici i funkce na vykreslení kolizí, tedy jejich rectanglů). 
Tím pádem se nemusí po jednom vytvářet objekty a přidávat jim kolize přímo v kódu, viz ukázka jedné obrazovky pod textem.

Kvůli docela komplexní grafice pozadí nepřidávám objektům texturu, ale na obrazovku je pouze 'nalepena' textura celé obrazovky (i tak opět efektivnější způsob).
Hra funguje na jednom screenu o velikosti 1280x960, textura mapy a kolize se mění po hráčově přechodu když jeho x < 0, poté se objeví na pozici x = 960 a mapa + kolize se updatují.
O hře by se dalo říci, že je to opět DEMO pouze o 3 obrazovkách, ale díky 'editoru' map stačí pouze napsat novou obrazovku a nakreslit její texturu, čímž se hra dá lehce rozšířit - popřípadě dokončit.


Ukázka obrazovky v .txt souboru.
Znak "-" nedělá nic, 
"+" slouží pro boční kolizi, 
"B" pro kolizi zespodu platformy, 
"T" pro kolizi zvrchu platformy,
"S" pro kolizi platformy která je pouze 40x40 pixelů velká (1 tile), tudíž má kolize zespodu i zvrchu (a zboku samozřejmě)

+------------------------------+

+------------------------------+

+------------------------------+

+------------------------------+

+------------------------------+

+TTTT--------------------------+

+++++--------------------------+

+++++--------------------------+

+++++----TTTT------------------+

+++++----++++------------------+

+BBBB----BBBB------------------+

+------------------------------+

+------------------------------+

+------------------------------+

+----------------TTTT------TTTT+

+----------------BBBB------BBBB+

+------------------------------+

+------------------------------+

+------------------------------+

+------------------------------+

+--------------------TTTTTT----+

+--------------------BBBBBB----+

+------------------------------+

+------------------------------+

Projektem opět cílím na známku "A", přijímám tedy připomínky a návrhy k obsahu hry nebo struktury kódu.
