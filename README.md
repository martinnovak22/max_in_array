# Simulátor CPU a RAM

Tento program simuluje jednoduchý procesor (CPU) a operační paměť (RAM) pro vykonávání základních instrukcí. Demonstruje hledání maximální hodnoty v poli zadaném uživatelem.

## Struktura kódu

### Třída `RAM`
Reprezentuje operační paměť s pevnou velikostí.
- **Metody**:
  - `__init__(size=256)`: Inicializuje paměť o velikosti `size` s výchozími nulovými hodnotami.
  - `load(address, value)`: Uloží hodnotu na zadanou adresu.
  - `read(address)`: Načte hodnotu z dané adresy.

### Třída `CPU`
Simuluje jednoduchý procesor schopný vykonávat základní instrukce.
- **Vlastnosti**:
  - `ram`: Odkaz na připojenou paměť RAM.
  - `accumulator`: Akumulátor, který uchovává mezivýsledky výpočtů.
  - `pc`: Programový čítač, který určuje aktuální instrukci.
- **Metody**:
  - `__init__(ram)`: Připojí paměť RAM k CPU.
  - `execute(instructions)`: Vykoná sadu instrukcí zadaných jako seznam.
  - `load(address)`: Načte hodnotu z paměti na zadané adrese do akumulátoru.
  - `compare(address)`: Porovná hodnotu na adrese s akumulátorem a případně aktualizuje akumulátor.
  - `jump(target_pc)`: Přeskočí na jinou instrukci podle programového čítače.
  - `nop()`: Instrukce, která neprovádí žádnou operaci.

## Příklad použití
Program načte pole čísel od uživatele, uloží je do paměti RAM a poté CPU vykoná instrukce pro nalezení maximální hodnoty.

### Hlavní kroky
1. **Načtení pole čísel**:
   - Program vyzve uživatele k zadání pole čísel oddělených čárkou, například:
     ```
     Zadejte pole čísel oddělených čárkou (např. 3,1,4,10,5,9): 8,2,7,4,10,1
     ```

2. **Načtení dat do RAM**:
   - Hodnoty jsou uloženy do paměti RAM.

3. **Definice instrukcí**:
   - Instrukce zahrnují načtení první hodnoty (`LOAD`) a postupné porovnání s dalšími hodnotami (`COMPARE`).

4. **Spuštění CPU**:
   - CPU vykonává instrukce a ukládá maximální hodnotu do akumulátoru.

5. **Výsledek**:
   - Maximální hodnota z pole se zobrazí v konzoli.

### Ukázka výstupu
Příklad zadání:
