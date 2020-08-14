#!/usr/bin/python3

import sys

"""
Percentage types:

1-percentage: Example: A value of 0.85 means it will do 15% (1-0.85) of that attribute
percentage-1: Example: A value of 1.01 means it will do 1% (1.01-1) of that attribute
toggle: Add in with a value of 1 to enable
add: Example: A value of 10 means it will add 10 (ex. At 16: on hit, you would heal up to 10 HP)
add_percent: Example: 17 (add X% uber on hit). It's 'add', but for things in game that are %'s.
"""
attributes = {
    "1": {"num_type": "1-percentage", "desc": "Deal {}% less damage"},  # "Less/Penalty" 'percentage'
    "2": {"num_type": "percentage-1", "desc": "Deal {}% more damage"},  # "More/Bonus" 'percentage'
    "3": {"num_type": "1-percentage", "desc": "Have a {}% smaller clip"},
    "4": {"num_type": "percentage-1", "desc": "Have a {}% larger clip"},
    "5": {"num_type": "1-percentage", "desc": "Fire {}% slower"},  # Penalty 'inverted_percentage'
    "6": {"num_type": "1-percentage", "desc": "Fire {}% faster"},  # Bonus 'inverted_percentage'
    "7": {"num_type": "1-percentage", "desc": "Heal {}% slower"},
    "8": {"num_type": "percentage-1", "desc": "Heal {}% slower"},
    "9": {"num_type": "1-percentage", "desc": "Build uber {}% slower"},
    "10": {"num_type": "percentage-1", "desc": "Build uber {}% faster"},
    "11": {"num_type": "percentage-1", "desc": "Have {}% more max overheal"},
    "12": {"num_type": "1-percentage", "desc": "Overheal time is decreased by {}%"},
    "13": {"num_type": "1-percentage", "desc": "Overheal time is increased by {}%"},
    "14": {"num_type": "toggle", "desc": "Prevent overheal decay"},
    "15": {"num_type": "toggle", "desc": "No random crits"},
    "16": {"num_type": "add", "desc": "Gain up to {} health on it"},
    "17": {"num_type": "add_percent", "desc": "Gain {}% ubercharge on hit"},
    "20": {"num_type": "toggle", "desc": "Crit vs. burning players"},
    "21": {"num_type": "1-percentage", "desc": "Deal {}% less damage to non-burning players"},
    "22": {"num_type": "toggle", "desc": "No critical hits vs. non-burning players"},
    "24": {"num_type": "toggle", "desc": "Critical hit from behind (flamethrowers only)"},
    "26": {"num_type": "add", "desc": "+{} max health on wearer"},
    "31": {"num_type": "add", "desc": "Gain {} seconds of critical hit chance on kill"},
    "32": {"num_type": "add_percent", "desc": "{}% chance to slow target on hit"},
    "34": {"num_type": "percentage-1", "desc": "Drain cloak {}% faster"},
    "35": {"num_type": "percentage-1", "desc": "Regenerate cloak {}% faster"},
    "36": {"num_type": "1-percentage", "desc": "{}% less accurate"},
    "39": {"num_type": "1-percentage", "desc": "Deal {}% less damage to non-stunned players"},
    "41": {"num_type": "percentage-1", "desc": "Snipe rifle charge rate increased by {}%"},
    "42": {"num_type": "toggle", "desc": "Don't headshot"},
    "44": {"num_type": "toggle", "desc": "Scattergun does knockback"},
    "45": {"num_type": "percentage-1", "desc": "Shoot {}% more bullets"},
    "51": {"num_type": "toggle", "desc": "Revolver crits on headshot"},
    "54": {"num_type": "1-percentage", "desc": "Move {}% slower"},
    "57": {"num_type": "add", "desc": "+{} health regen on wearer"},
    "60": {"num_type": "1-percentage", "desc": "Take {}% less damage from fire"},
    "61": {"num_type": "percentage-1", "desc": "Take {}% more damage from fire"},
    "62": {"num_type": "1-percentage", "desc": "Take {}% less damage from crits"},
    "63": {"num_type": "percentage-1", "desc": "Take {}% more damage from crits"},
    "64": {"num_type": "1-percentage", "desc": "Take {}% less damage from blasts"},
    "65": {"num_type": "percentage-1", "desc": "Take {}% more damage from blasts"},
    "66": {"num_type": "1-percentage", "desc": "Take {}% less damage from bullets"},
    "67": {"num_type": "percentage-1", "desc": "Take {}% more damage from bullets"},
    "68": {"num_type": "add", "desc": "+{} capture rate on wearer"},
    "69": {"num_type": "1-percentage", "desc": "Heal {}% less from healers"},
    "70": {"num_type": "percentage-1", "desc": "Heal {}% more from healers"},
    "71": {"num_type": "percentage-1", "desc": "Afterburn from this weapon does {}% more damage"},
    "72": {"num_type": "1-percentage", "desc": "Afterburn from this weapon does {}% less damage"},
    "73": {"num_type": "percentage-1", "desc": "Afterburn from this weapon lasts {}% longer"},
    "74": {"num_type": "1-percentage", "desc": "Afterburn from this weapon lasts {}% shorter"},
    "75": {"num_type": "percentage-1", "desc": "Move {}% faster while deployed"},
    "80": {"num_type": "percentage-1", "desc": "Hold {}% more metal"},
    "81": {"num_type": "1-percentage", "desc": "Hold {}% less metal"},
    "82": {"num_type": "1-percentage", "desc": "{}% less cloak duration"},
    "83": {"num_type": "percentage-1", "desc": "{}% more cloak duration"},
    "85": {"num_type": "1-percentage", "desc": "Decreased cloak regen rate by {}%"},
    "84": {"num_type": "percentage-1", "desc": "Increased cloak regen rate by {}%"},
    "86": {"num_type": "percentage-1", "desc": "{}% slower spin up time"},
    "87": {"num_type": "1-percentage", "desc": "{}% faster spin up time"},

}

def ask_for_attributes():
    ans = ""
    attribs = []
    while ans != "e":
        ans = input("Type in the attribute's number, a string to search for one, or 'e' to finish selecting attributes: ")
        try:
            ans = str(int(ans))
            if not ans in attributes.keys():
                print("Invalid attribute!")
                continue
        except ValueError:
            for a in attributes.keys():
                if ans in attributes[a]["desc"].lower():
                    print(a + ": " + attributes[a]["desc"].format("x"))
            continue
        selected = attributes[ans]
        if selected["num_type"] != "toggle":
            failed = True
            while failed:
                try:
                    value = str(float(input("Fill in the blank: '{}'".format(selected["desc"].format("__")) + ": ")))
                    failed = False
                except ValueError:
                    print("Not a number!")
                    failed = True
            attribs.append([ans, value])
        else:
            attribs.append([ans, "1"])
    return attribs


def get_input(question, answers):
    answer = ""
    while not answer and answer not in answers:
        answer = input(question).lower()
    return answer


def get_attrib_value(attrib):
    selected = attributes[str(attrib[0])]
    value_from_user = float(attrib[1])
    if selected["num_type"] == "1-percentage":
        return str(1 - (value_from_user / 100))
    elif selected["num_type"] == "percentage-1":
        return str((value_from_user / 100) + 1)
    elif selected["num_type"] == "add":
        return str(value_from_user)
    elif selected["num_type"] == "toggle":
        return "1"
    elif selected["num_type"] == "add_percent":
        return str(value_from_user)


def get_attrib_str(attrib):
    selected = attributes[str(attrib[0])]
    value_from_user = float(attrib[1])
    value_for_game = get_attrib_value(attrib)
    return '		"{attrib_no}"  //{attrib_comment}\n		{{\n			"plugin"	"tf2items"\n			"value"	"{attrib_val}"\n		}}'.format(
        attrib_no=str(attrib[0]), attrib_comment=selected["desc"].format(value_from_user), attrib_val=value_for_game
    )


def assemble_weapon(weapon, attribs):
    weapon_text = '"{name}"\n{{\n	"classes"\n	{{\n		"{wepclass}" "{slot}"\n	}}\n	"baseclass"	"{baseclass}"\n	"baseindex"	"{baseindex}"\n	"nobots"	"{nobots}"\n	"quality"	"{quality}"\n	"logname"	"{logname}"\n	"description"	"{description}"\n	"attributes"\n	{{\n{attributes}\n	}}\n}}'
    
    attrib_str = ""
    for a in attribs:
        attrib_str += "\n" + get_attrib_str(a)
    
    weapon_text = weapon_text.format(name=weapon["name"], wepclass=weapon["class"], slot=weapon["slot"], baseclass=weapon["baseclass"], baseindex=weapon["baseindex"],
    nobots=weapon["nobots"], quality=weapon["quality"], logname=weapon["logname"], description=weapon["description"], attributes=attrib_str)
    print(weapon_text)


def weapon_creator():
    weapon = {}
    weapon["name"] = input("Enter the weaon's name: ")
    weapon["class"] = get_input("Enter a class [scout/soldier/pyro/demoman/heavy/engineer/sniper/spy]: ", ["scout", "soldier", "pyro", "demoman", "heavy", "engineer", "medic", "sniper", "spy"])
    slots = ["first", "second", "third"]
    weapon["slot"] = slots.index(get_input("Which slot: " + ", ".join(slots) + "?: ", slots))
    weapon["baseclass"] = input("Enter the weapon's' baseclass (what the model is, basically): ")
    try:
        weapon["baseindex"] = str(int(input("Enter the weapon's baseindex used for sounds: ")))
    except ValueError:
        print("Not a number! Restarting weapon creation...")
        weapon_creator()
    weapon["nobots"] = "1"
    weapon["quality"] = "6"
    weapon["logname"] = weapon["name"].strip().replace(" ", "_")
    weapon["description"] = input("Enter a description: ")
    weapon_attributes = ask_for_attributes()
    assemble_weapon(weapon, weapon_attributes)


def main():
    while True:
        opt = get_input("'C'reate a weapon or 'E'xit?: [c/e] ", ['c', 'e'])
        if opt == 'c':
            weapon_creator()
        elif opt == 'e':
            sys.exit(0)


if __name__ == "__main__":
    main()