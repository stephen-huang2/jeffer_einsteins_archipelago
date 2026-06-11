class Room:
    
    def __init__(self, name:str, key:bool=False, unlocked:bool=False, key_type:str = "Key"):
        self.name = name
        self.key = key
        self.unlocked = unlocked
        self.key_type = key_type
    
    def __str__(self):
        return self.name

class Dryad(Room):

    RIDDLE = (
        "I drink the sun to paint the world in emerald, yet I have no mouth.\n"
        "I hold the earth in a silent grip, yet I have no hands.\n"
        "I have a heart that does not beat, and a crown that I cast aside when the world turns cold.\n"
        "What am I?"
    )
    ANSWERS = ["1. A mountain", "2. A tree", "3. A River"]
    CORRECT = "2"

    def __init__(self):
        super().__init__("Dryad", key=True, key_type="Magical Branch")
        self.riddle_solved = False

    def attempt_riddle(self, type_write_fn, bold_start, bold_end):
        type_write_fn(
            "\nThe ancient Dryad stirs, her bark-like skin cracking as she turns to face you...\n"
        )
        type_write_fn(f'"{self.RIDDLE}"\n')
        for ans in self.ANSWERS:
            type_write_fn(ans)
        answer = type_write_fn(
            f"\nChoose your answer ({bold_start}1{bold_end}/{bold_start}2{bold_end}/{bold_start}3{bold_end}):",
            userin=True
        )
        if answer.strip() == self.CORRECT:
            type_write_fn(
                '\n"Yes... a tree. You understand the living world. I shall grant you passage."\n'
            )
            self.riddle_solved = True
            self.key = False
            self.unlocked = True
            return True
        else:
            type_write_fn(
                '\n"No, that is not correct, and I will not take this disrespect!"\n'
            )
            return False


class Kraken(Room):

    RIDDLE = (
        "I have a thousand arms but no hands to hold.\n"
        "I have a beak like a bird but no wings to fly.\n"
        "I sleep in the crushing dark where the sun is forgotten,\n"
        "and when I rise, the mountains of the sea tremble\n"
        "and the wooden birds of men are shattered.\n"
        "What am I?"
    )
    ANSWERS = ["1. An Anchor", "2. A Coral Reef", "3. The Kraken"]
    CORRECT = "3"

    def __init__(self):
        super().__init__("The Kraken", key=False, unlocked=True)
        self.riddle_solved = False

    def attempt_riddle(self, type_write_fn, bold_start, bold_end):
        type_write_fn(
            "\nThe ocean floor trembles. A colossal eye opens in the darkness below you...\n"
        )
        type_write_fn(f'"{self.RIDDLE}"\n')
        for ans in self.ANSWERS:
            type_write_fn(ans)
        answer = type_write_fn(
            f"\nChoose your answer ({bold_start}1{bold_end}/{bold_start}2{bold_end}/{bold_start}3{bold_end}):",
            userin=True
        )
        if answer.strip() == self.CORRECT:
            type_write_fn(
                '\n"...Correct. You are not entirely worthless. I shall allow you to pass."\n'
            )
            self.riddle_solved = True
            self.unlocked = True
            return True
        else:
            type_write_fn(
                '\n"You are so unintelligent. You do not deserve to speak with me. Leave my sight."\n'
            )
            return False


class DemonsPalace(Room):

    RIDDLE = (
        "I was born in the breath of a whispered wish, yet I have grown into a titan that eclipses the sun.\n"
        "I am the invisible ink that writes the contracts of this realm, yet I have no hand to hold the pen.\n"
        "I am the feast that leaves you starving, the drink that leaves you parched,\n"
        "and the gold that turns to lead in the light of day.\n"
        "I am the only burden that becomes heavier the more you try to ignore it,\n"
        "and the only debt that is paid in the currency of your own blood.\n"
        "I am the foundation upon which these black spires were raised,\n"
        "and the mirror in which you will finally see your true face.\n"
        "I am the builder of your cage, and the key that you broke in the lock long before you arrived.\n"
        "Tell me, mortal: What am I?"
    )
    ANSWERS = [
        "1. Greed", "2. A Lie", "3. Guilt", "4. Sin",
        "5. Ambition", "6. Time", "7. Betrayal",
        "8. The Truth", "9. A Shadow", "10. Memory"
    ]
    CORRECT = "4"

    def __init__(self):
        super().__init__("Demon's Palace", key=True, key_type="Eye of Hell")
        self.riddle_solved = False

    def attempt_riddle(self, type_write_fn, bold_start, bold_end):
        type_write_fn(
            "\nThe gates of the Demon's Palace groan open. A voice like grinding stone fills the air...\n"
        )
        type_write_fn(f'"{self.RIDDLE}"\n')
        for ans in self.ANSWERS:
            type_write_fn(ans)
        answer = type_write_fn(
            f"\nChoose your answer ({bold_start}1{bold_end}/{bold_start}2{bold_end}/{bold_start}3{bold_end}"
            f"/{bold_start}4{bold_end}/{bold_start}5{bold_end}/{bold_start}6{bold_end}"
            f"/{bold_start}7{bold_end}/{bold_start}8{bold_end}/{bold_start}9{bold_end}/{bold_start}10{bold_end}):",
            userin=True
        )
        if answer.strip() == self.CORRECT:
            type_write_fn(
                '\n"...Sin. You are someone who truly understands us."\n'
            )
            type_write_fn(
                '"You are the first mortal we have ever let walk back to the real world. Go."\n'
            )
            self.riddle_solved = True
            self.key = False
            self.unlocked = True
            return True
        else:
            type_write_fn(
                '\nThe demons sneer at you. Your answer echoes off the black spires and means nothing.\n'
                '"Pathetic. Come back when you have truly looked at yourself. Try again next time."\n'
            )
            return False