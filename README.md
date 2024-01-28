Tímto Vám představuji moji PyGame - Jump like Ted

Jedná se o 2D skákačku na motivy hry Jump King (2019, studio Nexile). 
Ovládá se klávesy "A" pro chůzi vlevo, "D" pro chůzi vpravo, držení "SPACE" pro skok a "ESC" pro uložení a vypnutí.
Hra je zajímavá svým ovládáním a obtížností, kdy nabíjíte skok držením mezerníku a nikdy přímo nevidíte, jak daleko vyskočíte.
Zdánlivě jednoduchý koncept (mnou samozřejmě nevymyšlený) dokáže zabavit na několik hodin, protože mapa (jednotlivé obrazovky) je navržená tak, že téměř vždy můžete odkudkoliv spadnout až na úplný začátek.

Ve hře je mimo jiné:
    časomíra,
    mluvící NPC, sloužící spíše pro pobavení, nemá ve hře žádnou větší funkci,
    sbírání 'coinů', které můžete darovat NPC a to vám naoplátku řekne životní moudro. Sbíráním se dá také trackovat progress (vždy 1 coin na obrazovce),
    ukládání postupu (v .txt souboru), které ukládá pozici hráče, časomíru, posbírané coiny a postup v NPC dialogu.

S NPC interagujete jeho kolizí s Vámi, když u sebe máte jeden nebo více coinů. NPC dialogy by se neměly překrývat, i když má hráč u sebe více coinů, musí počkat až NPC domluví, pak mu může věnovat další.
Tento veškerý postup se ukládá v save souboru.

Pro jednodušší, přehlednější a celkově efektivnější stavění mapy (obrazovek) jsem vymyslel funkci, která načítá .txt soubor a dle určených parametrů přidává na obrazovku kolize
daných zdí nebo platforem. Každou obrazovku pak tedy stačí 'napsat' v texťáku a není potřeba nic víc rešit (dle potřeby testování je k dispozici i funkce na vykreslení kolizí, tedy jejich rectanglů). 
Tím pádem se nemusí po jednom vytvářet objekty a přidávat jim kolize přímo v kódu, viz ukázka jedné obrazovky pod textem.

Veškeré textury, které vidíte ve hře jsem sám nakreslil. Textury pozadí jsou inspirované těmi ve hře Jump King, samotné textury postav a coinů jsou pak mými výtvory.
Ve hře je také hudba. Hudba v samotné hře je bez licence, stejně tak jako zvukové efekty coiny a bounce od zdi. Hudbu v menu jsem vytvořil sám (snad bez copyrightu, tak úžasný to zase není) a zvuky NPC jsou z youtube videa
dostupného zde: https://www.youtube.com/watch?v=D-UmfqFjpl0.

Kvůli docela komplexní grafice pozadí nepřidávám objektům texturu, ale na obrazovku je pouze 'nalepena' textura celho screenu (rychlejší a opět efektivnější způsob).
Hra funguje na jedné obrazovce o velikosti 1280x960, textura mapy a kolize se mění po hráčově přechodu: když jeho x < 0, objeví se na pozici x = 960 a mapa + kolize se updatují.
O hře by se dalo říci, že je to opět DEMO pouze o 3 screenech, ale díky 'editoru' map stačí pouze napsat novou obrazovku, nakreslit její texturu a pripsat coin, čímž se hra dá lehce rozšířit - popřípadě dokončit.

Dostali-jste se až na třetí screen a zajímá Vás, jde-li vůbec vyskákat až nahoru? Ano, skutečně jde i když to není dvakrát snadné a možná by se dal screen lehce upravit. Pokud bych hru někdy dodělával, nejspíše bych tak učinil.

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
