# maincode.py

class Alchemist:
    def __init__(self, attack, strength, defense, magic, ranged, necromancy, laboratory):
        self.attack = attack
        self.strength = strength
        self.defense = defense
        self.magic = magic
        self.ranged = ranged
        self.necromancy = necromancy
        self.laboratory = laboratory
        self.recipes = {
            "Super Attack": ("Irit", "Eye of Newt"),
            "Super Strength": ("Kwuarm", "Limpwurt Root"),
            "Super Defence": ("Cadantine", "White Berries"),
            "Super Magic": ("Lantadyme", "Potato Cactus"),
            "Super Ranging": ("Dwarf Weed", "Wine of Zamorak"),
            "Super Necromancy": ("Arbuck", "Blood of Orcus"),
            "Extreme Attack": ("Avantoe", "Super Attack"),
            "Extreme Strength": ("Dwarf Weed", "Super Strength"),
            "Extreme Defence": ("Lantadyme", "Super Defence"),
            "Extreme Magic": ("Ground Mud Rune", "Super Magic"),
            "Extreme Ranging": ("Grenwall Spike", "Super Ranging"),
            "Extreme Necromancy": ("Ground Miasma Rune", "Super Necromancy"),
        }

    def getLaboratory(self):
        return self.laboratory

    def getRecipes(self):
        return self.recipes

    def mixPotion(self, name):
        if name in self.recipes:
            primary_ingredient, secondary_ingredient = self.recipes[name]
            
            # Check if the ingredients are available in the laboratory
            if primary_ingredient in self.laboratory.herbs and secondary_ingredient in self.laboratory.catalysts:
                herb = self.laboratory.herbs[primary_ingredient]
                catalyst = self.laboratory.catalysts[secondary_ingredient]

                # Remove used ingredients from the laboratory
                del self.laboratory.herbs[primary_ingredient]
                del self.laboratory.catalysts[secondary_ingredient]

                # Check if the potion is a SuperPotion or ExtremePotion
                if name.startswith("Super"):
                    potion = SuperPotion(name, herb.getStat(), 0.0, herb, catalyst)
                elif name.startswith("Extreme"):
                    super_potion_name = f"Super {name.split(' ')[1]}"
                    super_potion = self.laboratory.potions[super_potion_name]
                    potion = ExtremePotion(name, super_potion.getStat(), 0.0, catalyst, super_potion)

                # Calculate and set the boost for the mixed potion
                potion.setBoost(potion.calculateBoost())

                # Add the mixed potion to the laboratory
                self.laboratory.potions[name] = potion

                return f"{name} has been successfully mixed."
            else:
                return f"Insufficient ingredients to mix {name}."
        else:
            return f"{name} is not in the list of known recipes."

    def drinkPotion(self, potion):
        potion_name = potion.getName()

        if potion_name in self.laboratory.potions:
            potion = self.laboratory.potions[potion_name]

            # Determine the attribute to increase based on the potion's stat
            stat_to_increase = potion.getStat()

            # Increase the corresponding attribute of the alchemist
            setattr(self, stat_to_increase.lower(), getattr(self, stat_to_increase.lower()) + potion.getBoost())

            # Remove the consumed potion from the laboratory
            del self.laboratory.potions[potion_name]

            return f"You drank {potion_name}. Your {stat_to_increase} has increased by {potion.getBoost()}."
        else:
            return f"{potion_name} is not available in the laboratory."

    def collectReagent(self, reagent, amount):
        if reagent.getName() in self.laboratory.herbs:
            # Check if the specified herb is available in the laboratory
            herb = self.laboratory.herbs[reagent.getName()]

            # Add the specified amount of the herb to the laboratory
            herb.setPotency(herb.getPotency() + amount)
            self.laboratory.herbs[reagent.getName()] = herb

            return f"You collected {amount} of {reagent.getName()}."
        elif reagent.getName() in self.laboratory.catalysts:
            # Check if the specified catalyst is available in the laboratory
            catalyst = self.laboratory.catalysts[reagent.getName()]

            # Add the specified amount of the catalyst to the laboratory
            catalyst.setPotency(catalyst.getPotency() + amount)
            self.laboratory.catalysts[reagent.getName()] = catalyst

            return f"You collected {amount} of {reagent.getName()}."
        else:
            return f"{reagent.getName()} is not available in the laboratory."

    def refineReagents(self):
        for herb_name, herb in self.laboratory.herbs.items():
            # Refine herbs and print the result
            refined_herb = herb.refine()
            print(refined_herb)

            # Update the laboratory with the refined herb
            self.laboratory.herbs[herb_name] = refined_herb

        for catalyst_name, catalyst in self.laboratory.catalysts.items():
            # Refine catalysts and print the result
            refined_catalyst = catalyst.refine()
            print(refined_catalyst)

            # Update the laboratory with the refined catalyst
            self.laboratory.catalysts[catalyst_name] = refined_catalyst

        return "Reagents have been refined."


class Laboratory:
    def __init__(self):
        self.potions = []
        self.herbs = []
        self.catalysts = []

    def mixPotion(self, name, stat, primaryIngredient, secondaryIngredient):
        if primaryIngredient in self.herbs and secondaryIngredient in self.catalysts:
            herb = self.herbs[primaryIngredient]
            catalyst = self.catalysts[secondaryIngredient]

            # Remove used ingredients from the laboratory
            del self.herbs[primaryIngredient]
            del self.catalysts[secondaryIngredient]

            # Check if the potion is a SuperPotion or ExtremePotion
            if type == "Super":
                potion = SuperPotion(name, stat, 0.0, herb, catalyst)
            elif type == "Extreme":
                super_potion_name = f"Super {name.split(' ')[1]}"
                super_potion = self.potions[super_potion_name]
                potion = ExtremePotion(name, stat, 0.0, catalyst, super_potion)

            # Calculate and set the boost for the mixed potion
            potion.setBoost(potion.calculateBoost())

            # Add the mixed potion to the laboratory
            self.potions[name] = potion

            return f"{name} has been successfully mixed."
        else:
            return f"Insufficient ingredients to mix {name}."

    def addReagent(self, reagent, amount):
        if isinstance(reagent, Herb) or isinstance(reagent, Catalyst):
            reagent_name = reagent.getName()

            if reagent_name not in self.herbs and reagent_name not in self.catalysts:
                # Check the type of reagent and add it to the corresponding storage
                if isinstance(reagent, Herb):
                    self.herbs[reagent_name] = reagent
                elif isinstance(reagent, Catalyst):
                    self.catalysts[reagent_name] = reagent

                # Set the initial amount for the reagent
                reagent.setPotency(amount)

                return f"{amount} of {reagent_name} has been added to the laboratory."
            else:
                return f"{reagent_name} already exists in the laboratory. Cannot add duplicate reagents."
        else:
            return "Invalid reagent type. Only Herb and Catalyst types are allowed."


    
class Potion:
    def __init__(self, name, stat, boost):
        self.name = name
        self.stat = stat
        self.boost = boost

    def calculateBoost(self):
        # Common implementation for both SuperPotion and ExtremePotion
        pass

    def getName(self):
        return self.name

    def getStat(self):
        return self.stat

    def getBoost(self):
        return self.boost

    def setBoost(self, boost):
        self.boost = boost


class SuperPotion(Potion):
    def __init__(self, name, stat, boost, herb, catalyst):
        super().__init__(name, stat, boost)
        self.herb = herb
        self.catalyst = catalyst

    def calculateBoost(self):
        super_boost = self.herb.getPotency() + (self.catalyst.getPotency() * self.catalyst.getQuality()) * 1.5
        return round(super_boost, 2)

    def getHerb(self):
        return self.herb

    def getCatalyst(self):
        return self.catalyst


class ExtremePotion(Potion):
    def __init__(self, name, stat, boost, reagent, super_potion):
        super().__init__(name, stat, boost)
        self.reagent = reagent
        self.super_potion = super_potion

    def calculateBoost(self):
        extreme_boost = (self.reagent.getPotency() * self.super_potion.getBoost()) * 3.0
        return round(extreme_boost, 2)

    def getReagent(self):
        return self.reagent

    def getPotion(self):
        return self.super_potion





class Reagent:
    def __init__(self, name, potency):
        self.name = name
        self.potency = potency

    def refine(self):
        pass

    def getName(self):
        return self.name

    def getPotency(self):
        return self.potency

    def setPotency(self, potency):
        self.potency = potency


class Herb(Reagent):
    def __init__(self, name, potency, grimy=True):
        super().__init__(name, potency)
        self.grimy = grimy

    def refine(self):
        if self.grimy:
            self.grimy = False
            self.setPotency(self.getPotency() * 2.5)
            print(f"{self.getName()} has been refined and is no longer grimy.")
        else:
            print(f"{self.getName()} is already refined.")

    def getGrimy(self):
        return self.grimy

    def setGrimy(self, grimy):
        self.grimy = grimy


class Catalyst(Reagent):
    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self.quality = quality

    def refine(self):
        if self.quality < 8.9:
            self.quality += 1.1
            print(f"{self.getName()} quality increased to {self.quality}.")
        else:
            self.quality = 10
            print(f"{self.getName()} cannot be refined any further.")

    def getQuality(self):
        return self.quality





# Example usage:
lab = Laboratory()
alchemist = Alchemist(50, 60, 70, 80, 90, 100, lab)
herb = Herb("Irit", 1.0)
catalyst = Catalyst("Eye of Newt", 4.3, 1.0)
super_potion = SuperPotion("Super Attack", "attack", 0.0, herb, catalyst)
extreme_potion = ExtremePotion("Extreme Attack", "attack", 0.0, catalyst, super_potion)
