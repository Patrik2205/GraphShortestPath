# Dijkstrův algoritmus pro hledání nejkratších cest

Implementace Dijkstrova algoritmu pro hledání nejkratších cest v grafech.

## O Dijkstrově algoritmu

Dijkstrův algoritmus nalézá nejkratší cestu ze zdrojového vrcholu do všech ostatních vrcholů v ohodnoceném grafu s nezápornými váhami hran. Používá chamtivý přístup s prioritní frontou.

- **Časová složitost**: O((V + E) log V) s binární haldou
- **Prostorová složitost**: O(V)
- **Omezení**: Nefunguje s negativními vahami hran

## Instalace

```bash
pip install -r requirements.txt
```

## Použití

```bash
python main.py <vstupní_soubor> -s <počáteční_vrchol> [volby]

Povinné argumenty:
  vstupní_soubor      Cesta k souboru s grafem
  -s, --start         Počáteční vrchol pro Dijkstrův algoritmus

Volitelné argumenty:
  -e, --end           Koncový vrchol (zobrazí konkrétní cestu)
  -o, --output        Uložit výsledky do souboru
  -v, --visualize     Zobrazit vizualizaci grafu
  -h, --help          Zobrazit nápovědu
```

### Příklady použití

```bash
# Najít nejkratší cesty z vrcholu 1 v ukázkovém grafu
python main.py tests/image_graph.txt -s 1

# Najít cestu z 1 do 5 s vizualizací
python main.py tests/image_graph.txt -s 1 -e 5 -v

# Uložit výsledky do souboru
python main.py tests/test_data.txt -s A -o output/results.txt

# Spustit na příkladu českých měst
python main.py tests/czech_cities.json -s Praha -e Ostrava -v
```

## Formát vstupních dat

### Formát seznamu hran
```
# Komentáře začínají #
undirected
vrchol1 vrchol2 váha
vrchol1 vrchol3 váha
...
```

Pro orientované grafy použijte `directed` místo `undirected`.

### JSON formát
```json
{
  "directed": false,
  "edges": [
    {"from": "A", "to": "B", "weight": 5},
    {"from": "B", "to": "C", "weight": 3}
  ]
}
```

## Testovací soubory

- `tests/image_graph.txt` - Graf z přiloženého obrázku (vrcholy 1-5)
- `tests/test_data.txt` - Obecný testovací graf
- `tests/directed_graph.txt` - Příklad orientovaného grafu
- `tests/czech_cities.json` - Reálný příklad s českými městy
- `tests/extended_graph.txt` - Rozšířený testovací graf

## Struktura projektu

```
.
├── main.py                    # Hlavní aplikace
├── example.py                 # Ukázkové použití
├── setup.py                   # Instalační skript
├── requirements.txt           # Python závislosti
├── src/
│   ├── __init__.py
│   ├── graph.py              # Struktura grafu
│   ├── dijkstra.py           # Dijkstrův algoritmus
│   ├── visualization.py      # Vizualizace grafu
│   └── file_handler.py       # Operace se soubory
├── tests/                    # Testovací datové soubory
├── documentation/            # Dokumentace algoritmu
└── output/                   # Výstupní soubory
```

## Detaily algoritmu

Dijkstrův algoritmus funguje tak, že:
1. Začíná se zdrojovým vrcholem na vzdálenosti 0
2. Udržuje prioritní frontu nenavštívených vrcholů
3. Vždy zpracovává nejbližší nenavštívený vrchol
4. Aktualizuje vzdálenosti k sousedům (relaxace)
5. Pokračuje, dokud nejsou zpracovány všechny dosažitelné vrcholy

Algoritmus zaručuje nalezení nejkratší cesty v grafech s nezápornými vahami hran.

## Vizualizace

Implementace zahrnuje funkce grafické vizualizace:
- **Původní graf** - Zobrazuje strukturu vstupního grafu
- **Nejkratší cesta** - Zvýrazňuje konkrétní cestu červeně
- **Kompletní řešení** - Zobrazuje všechny nejkratší cesty ze zdroje se vzdálenostmi

## Výkon

- Malé grafy (< 100 vrcholů): < 1ms
- Střední grafy (100-1,000 vrcholů): 1-10ms  
- Velké grafy (> 10,000 vrcholů): 10-100ms

## Teoretická dokumentace

Kompletní teoretická dokumentace je k dispozici v souboru `documentation/dijkstra-teoria.md`, která pokrývá:
- Úvod do grafů a jejich reprezentace
- Problém nejkratších cest
- Detailní popis Dijkstrova algoritmu
- Porovnání s ostatními algoritmy
- Praktické aplikace a rozšíření

## Autor

Tato implementace byla vytvořena jako součást projektu algoritmy na grafech.