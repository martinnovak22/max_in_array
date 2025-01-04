class RAM:
    # Třída RAM reprezentuje operační paměť
    def __init__(self, size=256):
        # Inicializace paměti o velikosti 'size' s výchozími nulami
        self.memory = [0] * size

    def load(self, address, value):
        # Načtení hodnoty 'value' do paměti na adresu 'address'
        self.memory[address] = value

    def read(self, address):
        # Čtení hodnoty z paměti na adrese 'address'
        return self.memory[address]

class CPU:
    # Třída CPU simuluje jednoduchý procesor
    def __init__(self, ram):
        # Připojení paměti RAM k CPU
        self.ram = ram
        self.accumulator = 0  # Akumulátor slouží k uchování mezivýsledků
        self.pc = 0  # Programový čítač určuje aktuální instrukci

    def execute(self, instructions):
        # Metoda pro vykonávání instrukcí
        while self.pc < len(instructions):
            instr, *args = instructions[self.pc]  # Načtení aktuální instrukce a argumentů
            if instr == "LOAD":
                self.load(*args)  # Načtení hodnoty do akumulátoru
            elif instr == "COMPARE":
                self.compare(*args)  # Porovnání hodnoty s akumulátorem
            elif instr == "JUMP":
                self.jump(*args)  # Skok na jinou instrukci
            elif instr == "NOP":
                self.nop()  # Žádná operace
            self.pc += 1  # Posun na další instrukci

    def load(self, address):
        # Načtení hodnoty z paměti na adresu 'address' do akumulátoru
        self.accumulator = self.ram.read(address)

    def compare(self, address):
        # Porovnání hodnoty na adrese 'address' s akumulátorem
        value = self.ram.read(address)
        if value > self.accumulator:
            self.accumulator = value  # Pokud je hodnota větší, aktualizuje se akumulátor

    def jump(self, target_pc):
        # Skok na zadanou instrukci
        self.pc = target_pc - 1  # Posun na novou adresu

    def nop(self):
        # NOP (No Operation) - žádná operace
        pass

if __name__ == "__main__":
    # Inicializace paměti RAM a CPU
    ram = RAM(size=256)

    # Načtení datového pole do paměti RAM
    data = [3, 1, 4, 10, 5, 9]  # Pole hodnot, které budeme zpracovávat
    start_address = 0  # Počáteční adresa v paměti pro uložení dat
    for i, value in enumerate(data):
        ram.load(start_address + i, value)  # Načtení hodnot do RAM

    # Vytvoření instrukcí pro nalezení maxima v poli
    instructions = [("LOAD", start_address)]  # První instrukce: načtení první hodnoty
    for i in range(1, len(data)):
        instructions.append(("COMPARE", start_address + i))  # Přidání instrukcí COMPARE
    instructions.append(("NOP",))  # Instrukce NOP pro ukončení programu

    # Inicializace CPU a vykonání instrukcí
    cpu = CPU(ram)
    cpu.execute(instructions)

    # Výpis výsledku: maximální hodnoty v poli
    print(f"Maximum value: {cpu.accumulator}")
