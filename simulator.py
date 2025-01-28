# Třída RAM reprezentuje operační paměť
class RAM:
    def __init__(self, size=256):
        self.memory = [0] * size

    def load(self, address, value):
        self.memory[address] = value

    def read(self, address):
        return self.memory[address]

# Třída CPU simuluje jednoduchý procesor
class CPU:
    def __init__(self, ram):
        self.ram = ram
        self.accumulator = 0  # Akumulátor
        self.pc = 0           # Programový čítač
        self.registers = [0] * 4  # Čtyři univerzální registry (R0, R1, R2, R3)

    def execute(self, instructions):
        while self.pc < len(instructions):
            instr, *args = instructions[self.pc]

            if instr == "LOAD":
                self.load(*args)
            elif instr == "COMPARE":
                self.compare(*args)
            elif instr == "JUMP_IF":
                self.jump_if(*args)
            elif instr == "MOV":
                self.mov(*args)
            elif instr == "NOP":
                self.nop()
            
            self.pc += 1

    def load(self, address):
        self.accumulator = self.ram.read(address)

    def compare(self, address):
        value = self.ram.read(address)
        if value > self.accumulator:
            self.accumulator = value

    def jump_if(self, condition, target_pc):
        if eval(condition):  # Vyhodnocení podmínky
            self.pc = target_pc - 1

    def mov(self, reg, value):
        self.registers[reg] = value

    def nop(self):
        pass

# Hlavní program
if __name__ == "__main__":
    ram = RAM(size=256)

    # Načtení pole čísel do paměti
    user_input = input("Zadejte pole pěti čísel oddělených čárkou (např. 3,1,4,10,5): ")
    data = list(map(int, user_input.split(',')))
    start_address = 0

    for i, value in enumerate(data):
        ram.load(start_address + i, value)

    # Explicitně definované instrukce
    instructions = [
        ("LOAD", start_address),            # Načti první hodnotu do akumulátoru
        ("COMPARE", start_address + 1),    # Porovnej s druhou hodnotou
        ("COMPARE", start_address + 2),    # Porovnej s třetí hodnotou
        ("COMPARE", start_address + 3),    # Porovnej s čtvrtou hodnotou
        ("COMPARE", start_address + 4),    # Porovnej s pátou hodnotou
        ("MOV", 0, 10),                    # Ulož hodnotu 10 do registru R0
        ("JUMP_IF", "self.accumulator < self.registers[0]", 10),  # Pokud akumulátor < R0, skoč na reset
        ("STORE", 0, start_address + 5),   # Ulož hodnotu z R0 do paměti (např. nový výsledek)
        ("NOP",),                          # Konec programu
        # Pokud je akumulátor < R0, provede se toto:
        ("MOV", 1, 0),                     # Ulož hodnotu 0 do registru R1 (reset hodnoty)
        ("STORE", 1, start_address + 6),   # Ulož hodnotu 0 do paměti na novou adresu
        ("NOP",)                           # Konec
    ]


    # Spuštění instrukcí
    cpu = CPU(ram)
    cpu.execute(instructions)

    # Výpis maximální hodnoty
    print(f"Maximum value: {cpu.accumulator}")
    print("Memory:", ram.memory[:len(data)])
