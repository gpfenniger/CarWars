'''
Components Left:
    Armor
    Weapons
'''

class BodyType:
    # Component Class for Body
    def __init__(self, body_type, price, weight, max_load, spaces, cargo_spaces, armor_cost_to_weight):
        self.body_type = body_type
        self.price = price
        self.weight = weight
        self.max_load = max_load
        self.spaces = spaces
        self.cargo_spaces = cargo_spaces
        self.armor_cost_to_weight = armor_cost_to_weight


class ArmorType:
    # Component Class for Armor
    # TODO
    def __init__(self, armour_type):
        self.armour_type = armour_type

class Chassis:
    # Component Class for Chassis
    def __init__(self, strength, weight_mod, price):
        self.strength = strength
        self.weight_mod = weight_mod
        self.price = price

class Suspension:
    # Component Class for Suspension
    def __init__(self, suspension_type, price, hc, van_hc, sub_hc): 
        self.suspension_type = suspension_type
        self.price = price
        self.hc = hc
        self.van_hc = van_hc
        self.sub_hc = sub_hc

class Power_Plant:
    # Component Class for Power Plants
    def __init__(self, plant, cost, weight, spaces, dp, power_factors):
        self.plant = plant
        self.cost = cost
        self.weight = weight
        self.spaces = spaces
        self.max_dp = dp
        self.dp = dp
        self.power_factors = power_factors

    def damage(self, dmg):
        if dp - dmg > 0:
            dp -= dmg
        else:
            dp = 0
            print("Engine is destroyed")

class Tires:
    # Component Class for Tires
    def __init__(self, tire_type, price, weight, dp):
        self.tire_type = tire_type
        self.price = price
        self.weight = weight
        self.max_dp = dp
        self.dp = {
            "Front_Right": dp,
            "Front_Left": dp,
            "Back_Right": dp,
            "Back_Left": dp
        }

class VehicleBuilder:
    # This class is used to build Vehicles and can be a sole import
    def __init__(self):
        print("We're in business!")
        # TODO move this section onto a MySQL Database
        self.body_types = {
            "Description": [ "Type", " Price", "Weight", "Max Load", "Spaces", "Cargo Spaces", "Armor Cost / Weight"],
            "Types": ["Subcompact", "Compact", "Mid_Sized", "Sedan", "Luxury", "Station_Wagon", "Pickup", "Camper", "Van"],
            "Subcompact": [ "300", "1000", "2300", "7", "0", "11/05" ],
            "Compact": [ "400", "1300", "3700", "10", "0", "13/06" ],
            "Mid_Sized": [ "600", "1600", "4800", "13", "0", "16/08" ],
            "Sedan": [ "700", "1700", "5100", "16", "0", "18/09" ],
            "Luxury": [ "800", "1800", "5500", "19", "0", "20/10" ],
            "Station_Wagon": [ "800", "1800", "5500", "14", "7", "20/10" ],
            "Pickup": [ "900", "2100", "6500", "13", "11", "22/11" ],
            "Camper": [ "1400", "2300", "6500", "17", "7", "30/14" ],
            "Van": [ "1000", "2000", "6000", "24", "6", "30/14" ]
        }
        self.armor_types = {

        }
        self.chassis_types = {
            "Description": [ "Strength", "Weight Modifier", "Price percent of body" ],
            "Types": [ "Light", "Standard", "Heavy", "Extra_Heavy" ],
            "Light": [ -10, -0.20 ],
            "Standard": [ 0, 0 ],
            "Heavy": [ 10, 0.50 ],
            "Extra_Heavy": [ 20, 1 ]
        }
        self.suspension_types = {
            "Description": [ "Type", "Price percent of body", "HC", "Van HC", "Sub HC"],
            "Types": [ "Light", "Improved", "Heavy", "Offroad" ],
            "Light": [ 0, 1, 0, 2 ],
            "Improved": [ 1, 2, 1, 3 ],
            "Heavy": [ 1.5, 3, 2, 4 ],
            "Offroad": [ 5, 2, 1, 3 ]
        }
        self.power_plant_types = {
            "Description": [ "Type", "Cost", "Weight", "Spaces", "DP", "Power Factors" ],
            "Types": [ "Small", "Medium", "Large", "Super", "Sport", "Thundercat" ],
            "Small": [ 500, 500, 3, 5, 800 ],
            "Medium": [ 1000, 700, 4, 8, 1400 ],
            "Large": [ 2000, 900, 5, 10, 2000 ],
            "Super": [ 3000, 1100, 6, 12, 2600 ],
            "Sport": [ 6000, 1000, 6, 12, 3000 ],
            "Thundercat": [ 1200, 2000, 8, 15, 6700 ]
        }
        self.tire_types = {
            "Description": [ "Type", "Price", "Weight", "DP" ],
            "Types": [ "Standard", "Heavy_Duty", "Puncture_Resistant", "Solid" ],
            "Standard": [ 50, 30, 4 ],
            "Heavy_Duty": [ 100, 40, 6 ],
            "Puncture_Resistant": [ 200, 50, 9 ],
            "Solid": [ 500, 75, 12 ]
        }

    # This builds a vehicle
    # NO ARGS : RETURN { Vehicle }
    def build(self):
        prompts = [
            "First select the body type",
            "Now select a chasis type",
            "Next your car needs suspension",
            "Almost done, now choose a power plant to power your car",
            "Lastly select the type of tires you would like?"
        ]
        component_list = [
            self.body_types, self.chassis_types, 
            self.suspension_types, self.power_plant_types, self.tire_types
        ]
        component_types = ["body", "chassis", "suspension", "power_plant", "tires"]
        components_made = []
        for i in range(len(prompts)):
            print(prompts[i])
            for item in component_list[i]["Types"]:
                print(item)
            print("Your choice: ")
            choice = self.user_select(component_list[i]["Types"])
            component_stats = component_list[i][choice]
            component_stats.append(choice) # Adds the component name to the end of the array
            components_made.append(self.make_component(component_types[i], component_stats))

        return Vehicle(
            components_made[0], 
            components_made[1], 
            components_made[2], 
            components_made[3], 
            components_made[4]
        )

    # Takes in a component type and array and returns an object of that type
    # ARGS { component_type STRING, array GENERIC } : RETURN OBJECT OF component_type
    def make_component(self, component_type, array):
        if component_type == "body":
            return BodyType(array[6], array[0], array[1], array[2], array[3], array[4], array[5])
        elif component_type == "chassis":
            return Chassis(array[2], array[0], array[1])
        elif component_type == "suspension":
            return Suspension(array[4], array[0], array[1], array[2], array[3])
        elif component_type == "power_plant":
            return Power_Plant(array[5], array[0], array[1], array[2], array[3], array[4])
        elif component_type == "tires":
            return Tires(array[3], array[0], array[1], array[2]) 


    # Private method for making a user choice based on an array
    # ARGS { array STRING[] } : RETURN { STRING }
    def user_select(self, array):
        user_input = input()
        for array_item in array:
            if user_input == array_item:
                return array_item
        print("That's not a proper choice")
        return self.user_select(array)


class Vehicle:
    # Record Class for storing Vehicle information and methods

    # Constructor Method
    # NO ARGS : RETURN { Vehicle OBJECT }
    def __init__(self, body, chassis, suspension, power_plant, tires):
        self.body = body
        self.chassis = chassis
        self.suspension = suspension
        self.power_plant = power_plant
        self.tires = tires

        self.weight = int(self.body.weight) + self.power_plant.weight + self.tires.weight
        if power_plant.power_factors < (self.weight / 3):
            self.accel = 0 
        elif power_plant.power_factors < (self.weight / 2):
            self.accel = 5
        elif power_plant.power_factors < self.weight:
            self.accel = 10
        else:
            self.accel = 15
        
        self.cost = int(self.body.price) + (int(self.body.price) * self.chassis.price) 
        self.cost += (int(self.body.price) * self.suspension.price) 
        self.cost += self.power_plant.cost + self.tires.price