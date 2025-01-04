# Třída RAM reprezentuje operační paměť
class RAM:
    # Inicializace paměti o velikosti 256 s výchozími nulami
    def __init__(self, size=256):
        self.memory = [0] * size

    # Načtení hodnoty do paměti na adresu
    def load(self, address, value):
        self.memory[address] = value

    # Čtení hodnoty z paměti na adrese
    def read(self, address):
        return self.memory[address]

# Třída CPU simuluje jednoduchý procesor
class CPU:
    # Připojení paměti RAM k CPU
    def __init__(self, ram):
        self.ram = ram
        # Akumulátor slouží k uchování mezivýsledků
        self.accumulator = 0
        # Programový čítač určuje aktuální instrukci
        self.pc = 0 

    # Metoda pro vykonávání instrukcí
    def execute(self, instructions):
        while self.pc < len(instructions):
            instr, *args = instructions[self.pc]  # Načtení aktuální instrukce a argumentů
            if instr == "LOAD":
                self.load(*args)  # Načtení hodnoty do akumulátoru
            elif instr == "COMPARE":
                self.compare(*args)  # Porovnání hodnoty s akumulátorem
            elif instr == "JUMP":
                self.jump(*args)  # Skok na jinou instrukci
            elif instr == "NOP":
                self.nop()
            self.pc += 1

    # Načtení hodnoty z paměti na adresu do akumulátoru
    def load(self, address):
        self.accumulator = self.ram.read(address)

    # Porovnání hodnoty na adrese s akumulátorem
    def compare(self, address):
        value = self.ram.read(address)
        if value > self.accumulator:
            self.accumulator = value

    # Skok na zadanou instrukci
    def jump(self, target_pc):
        self.pc = target_pc - 1 

    # NOP (No Operation) - žádná operace
    def nop(self):
        pass

# Inicializace paměti RAM a CPU
if __name__ == "__main__":
    ram = RAM(size=256)

    # Datového pole
    data = [3, 1, 4, 10, 5, 9]

    start_address = 0 

    # Načtení hodnot do RAM
    for i, value in enumerate(data):
        ram.load(start_address + i, value)  

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
