# Dijkstrův algoritmus pro hledání nejkratších cest v grafech

## 1. Úvod do grafů

### Definice grafu

**Graf** G = (V, E) je matematická struktura sestávající z množiny vrcholů V a množiny hran E, kde každá hrana spojuje dva vrcholy.

#### Typy grafů:

**Neorientovaný graf:**
- Hrany nemají směr
- Hrana {u, v} je totožná s hranou {v, u}
- Používá se pro modelování symetrických vztahů (např. vzdálenosti mezi městy)

**Orientovaný graf (digraf):**
- Hrany mají směr
- Hrana (u, v) není totožná s hranou (v, u)
- Používá se pro modelování asymetrických vztahů (např. jednosměrné ulice)

**Ohodnocený graf:**
- Každé hraně je přiřazena číselná hodnota (váha)
- Váha může reprezentovat vzdálenost, čas, cenu, atd.
- Formálně: funkce w: E → ℝ

### Kostra grafu

**Kostra** (spanning tree) souvislého neorientovaného grafu G je podgraf, který:
- Obsahuje všechny vrcholy grafu G
- Je souvislý (mezi každými dvěma vrcholy existuje cesta)
- Je acyklický (neobsahuje cykly)
- Má právě |V| - 1 hran

**Minimální kostra** je kostra s nejmenším možným součtem vah hran.

### Reprezentace grafů

#### Matice sousednosti
```
    A  B  C  D
A [ 0  4  2  ∞ ]
B [ 4  0  1  5 ]
C [ 2  1  0  8 ]
D [ ∞  5  8  0 ]
```

**Výhody:**
- Rychlé určení existence hrany O(1)
- Jednoduchá implementace
- Vhodné pro husté grafy

**Nevýhody:**
- Paměťová složitost O(V²)
- Neefektivní pro řídké grafy

#### Seznam sousedů
```
A: [(B,4), (C,2)]
B: [(A,4), (C,1), (D,5)]
C: [(A,2), (B,1), (D,8)]
D: [(B,5), (C,8)]
```

**Výhody:**
- Paměťová složitost O(V + E)
- Efektivní pro řídké grafy
- Rychlé procházení sousedů

**Nevýhody:**
- Pomalejší test existence hrany O(deg(v))

### Reálné příklady využití

#### Navigace a doprava
- **GPS navigace**: Grafy silniční sítě pro hledání nejkratších tras
- **Letecká doprava**: Optimalizace letových tras
- **Městská hromadná doprava**: Plánování tras a jízdních řádů

#### Počítačové sítě
- **Internet routing**: Směrování paketů mezi routery
- **Telekomunikační sítě**: Optimalizace propustnosti
- **Sociální sítě**: Analýza spojení mezi uživateli

#### Plánování a optimalizace
- **Projektové řízení**: PERT/CPM diagramy
- **Výrobní procesy**: Optimalizace výrobních linek
- **Logistika**: Distribuce zboží, skladové hospodářství

## 2. Problém hledání nejkratší cesty

### Co znamená „nejkratší cesta"

**Nejkratší cesta** mezi dvěma vrcholy u a v je cesta s minimální celkovou váhou (součtem vah všech hran na cestě).

**Formální definice:**
Pro cestu P = (v₀, v₁, ..., vₖ) kde v₀ = u a vₖ = v, je váha cesty:
```
w(P) = Σ w(vᵢ, vᵢ₊₁) pro i = 0 až k-1
```

Nejkratší cesta je cesta s minimální hodnotou w(P).

### Varianty problému nejkratší cesty

1. **Single-source shortest path (SSSP)**: Z jednoho vrcholu do všech ostatních
2. **Single-pair shortest path**: Mezi dvěma konkrétními vrcholy  
3. **All-pairs shortest path**: Mezi všemi páry vrcholů

### Negativní hrany a jejich vliv

#### Problém s negativními hranami
- **Negativní hrana**: Hrana s váhou w(u,v) < 0
- **Negativní cyklus**: Cyklus s celkovou zápornou váhou

#### Vliv na algoritmy:
**Dijkstrův algoritmus:**
- Nefunguje správně s negativními hranami
- Předpokládá, že přidání hrany k cestě nikdy nesníží celkovou váhu
- Může dát nesprávný výsledek

**Příklad problému:**
```
A --(-2)--> B
 \          |
  \----5----/
```
Dijkstra může zpracovat B dříve než nalezne cestu A→B s váhou -2.

## 3. Přehled algoritmů pro nejkratší cesty

### a) Dijkstrův algoritmus

#### Princip algoritmu

**Greedy přístup:**
- Vždy vybere nezpracovaný vrchol s nejmenší známou vzdáleností
- Zaručuje, že když je vrchol zpracován, jeho vzdálenost je optimální

**Klíčová myšlenka:**
Pro grafy s nezápornými váhami musí nejkratší cesta k vrcholu v procházet přes vrcholy bližší ke zdroji než v.

#### Algoritmus krok za krokem:

1. **Inicializace:**
   - Nastav vzdálenost ke zdroji = 0
   - Nastav všechny ostatní vzdálenosti = ∞
   - Vytvoř prioritní frontu s (0, zdroj)

2. **Hlavní smyčka:**
   - Vyber vrchol s minimální vzdáleností z fronty
   - Pro každého nenavštíveného souseda:
     - Vypočítaj novou vzdálenost přes aktuální vrchol
     - Pokud je kratší, aktualizuj vzdálenost a předchůdce
     - Přidej do prioritní fronty

3. **Ukončení:**
   - Když jsou všechny vrcholy zpracované nebo fronta prázdná

#### Pseudokód:
```
DIJKSTRA(G, s):
    for each vertex v in G.V:
        dist[v] = ∞
        pred[v] = NIL
    
    dist[s] = 0
    Q = priority queue containing all vertices
    
    while Q is not empty:
        u = EXTRACT-MIN(Q)
        for each vertex v adjacent to u:
            if dist[u] + weight(u,v) < dist[v]:
                dist[v] = dist[u] + weight(u,v)
                pred[v] = u
                DECREASE-KEY(Q, v, dist[v])
```

#### Relaxace hrany
**Relaxace** je klíčová operace:
```
RELAX(u, v, w):
    if dist[u] + w(u,v) < dist[v]:
        dist[v] = dist[u] + w(u,v)
        pred[v] = u
```

#### Časová složitost

| Implementace prioritní fronty | Časová složitost |
|-------------------------------|------------------|
| Pole | O(V²) |
| Binární halda | O((V + E) log V) |
| Fibonacciho halda | O(E + V log V) |

**Nejčastěji používaná implementace:** Binární halda s O((V + E) log V)

#### Prostorová složitost
O(V) - pro uložení vzdáleností a předchůdců

#### Omezení
1. **Nefunguje s negativními hranami** - může dát nesprávný výsledek
2. **Single-source only** - pro all-pairs je nutné spustit V-krát
3. **Paměťové nároky** - musí uchovávat celý graf v paměti

#### Optimalizace
- **Předčasné ukončení** pro single-pair dotazy
- **Obousměrné hledání** pro point-to-point dotazy
- **A* algoritmus** s heuristickou funkcí

### b) Bellman-Fordův algoritmus

#### Základní princip
- **Relaxace hran**: Opakovaně relaxuje všechny hrany
- **Iterace**: Provádí až V-1 iterací
- **Detekce záporných cyklů**: Dokáže detekovat negativní cykly

#### Výhody
- Funguje i s negativními hranami
- Detekuje negativní cykly
- Jednoduchá implementace

#### Časová složitost
O(VE) - pomalejší než Dijkstra pro nezáporné grafy

### c) Floyd-Warshallův algoritmus

#### Základní princip
- **Dynamické programování**: Postupně zlepšuje odhady vzdáleností
- **All-pairs**: Řeší problém pro všechny páry vrcholů najednou
- **Tři vnořené smyčky**: Pro každý vrchol jako mezilehlý bod

#### Výhody
- Řeší all-pairs shortest path
- Funguje s negativními hranami (bez negativních cyklů)
- Kompaktní implementace

#### Časová složitost
O(V³) - vhodné pro malé až střední grafy

## 4. Implementace Dijkstrova algoritmu

### Struktura projektu
```
src/
├── dijkstra.py        # Hlavní implementace algoritmu
├── graph.py           # Struktura grafu
├── file_handler.py    # Načítání dat
└── visualization.py   # Vizualizace výsledků
```

### Klíčové funkce

#### Hlavní funkce algoritmu
```python
def dijkstra(graph, start):
    """
    Dijkstrův algoritmus pro hledání nejkratších cest.
    
    Argumenty:
        graph: Objekt grafu
        start: Počáteční vrchol
        
    Vrací:
        distances: Slovník vzdáleností
        predecessors: Slovník předchůdců
    """
```

#### Rekonstrukce cesty
```python
def reconstruct_path(predecessors, start, end):
    """Rekonstruuje cestu ze slovníku předchůdců"""
```

### Formáty vstupních dat

#### Seznam hran
```
undirected
A B 4
A C 2
B C 1
B D 5
```

#### JSON formát
```json
{
  "directed": false,
  "edges": [
    {"from": "A", "to": "B", "weight": 4},
    {"from": "A", "to": "C", "weight": 2}
  ]
}
```

### Testovací data

Projekt obsahuje několik testovacích souborů:
- `image_graph.txt` - Graf z přiloženého obrázku
- `test_data.txt` - Základní testovací graf
- `czech_cities.json` - Reálný příklad s českými městy

### Vizualizace

Implementace zahrnuje pokročilé vizualizační funkce:
- **Původní graf** - Zobrazení struktury grafu
- **Nejkratší cesta** - Zvýraznění konkrétní cesty
- **Kompletní řešení** - Všechny nejkratší cesty ze zdroje

## 5. Praktické použití a výkon

### Charakteristiky výkonu

#### Malé grafy (< 100 vrcholů)
- Čas provádění: < 1ms
- Využití paměti: Zanedbatelné

#### Střední grafy (100-1,000 vrcholů)  
- Čas provádění: 1-10ms
- Využití paměti: < 1MB

#### Velké grafy (> 10,000 vrcholů)
- Čas provádění: 10-100ms
- Využití paměti: Několik MB

### Praktické aplikace

1. **GPS navigace** - Hledání nejkratších tras
2. **Směrování v sítích** - Internetové směrování paketů
3. **Herní AI** - Pathfinding ve hrách
4. **Sociální sítě** - Analýza stupňů oddělení
5. **Plánování letů** - Hledání nejlevnějších letů

## 6. Závěr

### Shrnutí poznatků

Dijkstrův algoritmus je jedním z nejdůležitějších algoritmů v informatice pro řešení problému nejkratších cest. Hlavní poznatky:

#### Silné stránky:
- **Efektivita**: O((V + E) log V) s binární haldou
- **Spolehlivost**: Garantuje optimální řešení pro nezáporné grafy
- **Všestrannost**: Široké spektrum praktických aplikací
- **Implementace**: Relativně jednoduchá implementace

#### Omezení:
- **Negativní hrany**: Nefunguje s negativními váhami hran
- **Paměť**: Vyžaduje uložení celého grafu v paměti
- **Single-source**: Pro all-pairs nutné opakované spuštění

#### Praktické doporučení:
- Použít pro grafy s nezápornými hranami
- Vhodný pro single-source a single-pair dotazy
- Pro husté grafy zvážit implementaci s Fibonacciho haldou
- Pro negativní hrany použít Bellman-Ford algoritmus

### Možnosti rozšíření

#### A* algoritmus
- Rozšíření Dijkstrova algoritmu s heuristickou funkcí
- Rychlejší pro single-pair dotazy
- Používá odhad vzdálenosti k cíli: f(v) = g(v) + h(v)

#### Johnsonův algoritmus
- Kombinuje Bellman-Ford a Dijkstra pro all-pairs
- Efektivní pro řídké grafy s negativními hranami
- Časová složitost: O(V² log V + VE)

#### Bidirektionální vyhledávání
- Současné hledání ze zdroje i cíle
- Může být až 2× rychlejší pro point-to-point dotazy
- Setkání uprostřed cesty