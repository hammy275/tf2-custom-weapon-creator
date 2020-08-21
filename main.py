#!/usr/bin/python3

import sys

"""
Percentage types:

1-percentage: Example: A value of 0.85 means it will do 15% (1-0.85) of that attribute
percentage-1: Example: A value of 1.01 means it will do 1% (1.01-1) of that attribute
toggle: Add in with a value of 1 to enable
add: Example: A value of 10 means it will add 10 (ex. At 16: on hit, you would heal up to 10 HP)
add-1: 'add' except multiplied by -1
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
    "36": {"num_type": "percentage-1", "desc": "{}% less accurate"},
    "39": {"num_type": "1-percentage", "desc": "Deal {}% less damage to non-stunned players"},
    "41": {"num_type": "percentage-1", "desc": "Snipe rifle charge rate increased by {}%"},
    "42": {"num_type": "toggle", "desc": "Can't headshot"},
    "44": {"num_type": "toggle", "desc": "Scattergun does knockback"},
    "45": {"num_type": "percentage-1", "desc": "+{}% bullets per shot"},
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
    "76": {"num_type": "percentage-1", "desc": "+{}% max primary ammo"},
    "77": {"num_type": "1-percentage", "desc": "-{}% max primary ammo"},
    "80": {"num_type": "percentage-1", "desc": "Hold {}% more metal"},
    "81": {"num_type": "1-percentage", "desc": "Hold {}% less metal"},
    "82": {"num_type": "1-percentage", "desc": "{}% less cloak duration"},
    "83": {"num_type": "percentage-1", "desc": "{}% more cloak duration"},
    "85": {"num_type": "1-percentage", "desc": "Decreased cloak regen rate by {}%"},
    "84": {"num_type": "percentage-1", "desc": "Increased cloak regen rate by {}%"},
    "86": {"num_type": "percentage-1", "desc": "{}% slower spin up time"},
    "87": {"num_type": "1-percentage", "desc": "{}% faster spin up time"},
    "90": {"num_type": "percentage-1", "desc": "{}% faster sniper charge rate"},
    "91": {"num_type": "1-percentage", "desc": "{}% slower sniper charge rate"},
    "96": {"num_type": "percentage-1", "desc": "{}% slower reload time"},
    "97": {"num_type": "1-percentage", "desc": "{}% faster reload speed"},
    "98": {"num_type": "add-1", "desc": "Take {} damage on hitting someone"},
    "99": {"num_type": "percentage-1", "desc": "+{}% explosion radius"},
    "100": {"num_type": "1-percentage", "desc": "-{}% explosion radius"},
    "103": {"num_type": "percentage-1", "desc": "+{}% projectile speed"},
    "104": {"num_type": "1-percentage", "desc": "-{}% projectile speed"},
    "106": {"num_type": "1-percentage", "desc": "{}% more accurate"},
    "113": {"num_type": "add", "desc": "Regenerate {} metal every 5 seconds"},
    "114": {"num_type": "toggle", "desc": "Mini-crit targets launched airbone by explosions, grapple hooks, or rocket packs"},
    "115": {"num_type": "toggle", "desc": "Deal more melee damage as the user becomes more damaged"},
    "119": {"num_type": "toggle", "desc": "Only detonate sticky bombs at feet and near crosshair"},
    "120": {"num_type": "add", "desc": "Sticky bombs arm {} seconds slower"},
    "124": {"num_type": "toggle", "desc": "The wrench builds mini-sentries"},
    "125": {"num_type": "add-1", "desc": "{} less max health on wearer"},
    "126": {"num_type": "add-1", "desc": "Sticky bombs arm {} seconds faster"},
    "128": {"num_type": "toggle", "desc": "Any attributes added after this one only apply while weapon is active"},
    "129": {"num_type": "add-1", "desc": "Up to {} health drained per second on wearer"},
    "136": {"num_type": "toggle", "desc": "On sentry death, gain 2 crits per sentry kill and 1 per sentry assist."},
    "146": {"num_type": "toggle", "desc": "Damage removes sappers."},
    "148": {"num_type": "1-percentage", "desc": "{}% metal reduction in building cost"},
    "149": {"num_type": "add", "desc": "Bleed for {} seconds on hit"},
    "150": {"num_type": "toggle", "desc": "Imbued with an ancient power"},
    "154": {"num_type": "toggle", "desc": "Disguise on backstab"},
    "155": {"num_type": "toggle", "desc": "Wearer cannot disguise"},
    "156": {"num_type": "toggle", "desc": "Backstabs are silent"},
    "158": {"num_type": "add", "desc": "Gain {}% cloak on kill"},
    "160": {"num_type": "toggle", "desc": "Decloaks are quieter"},
    "166": {"num_type": "add", "desc": "Gain {}% cloak on hit"},
    "168": {"num_type": "toggle", "desc": "Immune to fire damage while disguised"},
    "175": {"num_type": "add", "desc": "Apply jarate from 2 to {} seconds on scoped hit based on charge level"},
    "177": {"num_type": "percentage-1", "desc": "{}% longer weapon switch"},
    "178": {"num_type": "1-percentage", "desc": "{}% faster weapon switch"},
    "179": {"num_type": "toggle", "desc": "This weapon crits when it would normally mini-crit"},
    "181": {"num_type": "toggle", "desc": "Don't take damage from self inflicted blast damage"},
    "182": {"num_type": "add", "desc": "Slow enemy by 40% for {} seconds on hit"},
    "188": {"num_type": "add", "desc": "Keep up to {}% of your uber on death"},
    "199": {"num_type": "1-percentage", "desc": "{}% faster holster speed"},
    "200": {"num_type": "toggle", "desc": "AOE heal taunt on alt-fire"},
    "203": {"num_type": "toggle", "desc": "Those killed drop a small health pack."},
    "204": {"num_type": "toggle", "desc": "Hit yourself on miss"},
    "208": {"num_type": "toggle", "desc": "Target is engulfed in flames on hit"},
    "209": {"num_type": "toggle", "desc": "Mini-crit vs. burning players"},
    "217": {"num_type": "toggle", "desc": "Absorb health from victim on backstab"},
    "218": {"num_type": "toggle", "desc": "Mark target for death on hit. Only one target can be marked."},
    "220": {"num_type": "add", "desc": "Gain {}% of base health on kill"},
    "226": {"num_type": "toggle", "desc": "Take 50 damage when sheathing except when it's killed."},
    "231": {"num_type": "toggle", "desc": "UberCharge acts like quickfix (300% heal rate and stuff)"},
    "235": {"num_type": "toggle", "desc": "Move speed increases as the user becomes injured"},
    "238": {"num_type": "toggle", "desc": "Minigun barrel spin is silent"},
    "250": {"num_type": "toggle", "desc": "Triple jump and crit with melee in air while this item is held."},
    "251": {"num_type": "toggle", "desc": "Speed boost for self and teammate on teammate hit"},
    "267": {"num_type": "toggle", "desc": "Deal crits while rocket jumping"},
    "269": {"num_type": "toggle", "desc": "You can see enemy health"},
    "351": {"num_type": "add", "desc": "Build +{} additional disposable-sentries"},
    "389": {"num_type": "toggle", "desc": "Shots penetrate players"},

}

def ask_for_attributes():
    ans = ""
    attribs = []
    while ans != "e":
        ans = input("Type in the attribute's number, a string to search for one, 'd' to delete an attribute, or 'e' to finish selecting attributes: ")
        if ans == 'd':
            if len(attribs) == 0:
                print("No attributes attatched to weapon!")
                continue
            c = 0
            for a in attribs:
                print("{}: ".format(str(c)) + attributes[a[0]]["desc"].format(a[1]))
                c += 1
            opts = ['c']
            for i in range(0,c+1):
                opts.append(str(i))
            to_del = get_input("Type in the number of the attribute you want to delete or 'c' to cancel.", opts)
            if to_del == 'c':
                continue
            else:
                del attribs[int(to_del)]
                print("Deleted!")
                continue
        try:
            ans = str(int(ans))
            if not ans in attributes.keys():
                print("Invalid attribute!")
                continue
        except ValueError:
            if ans == "e":
                continue
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
        print("Current weapon stats:")
        for a in attribs:
            print(attributes[a[0]]["desc"].format(a[1]))
    return attribs


def get_input(question, answers):
    answer = ""
    while answer not in answers:
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
    elif selected["num_type"] == "add-1":
        return str(value_from_user * -1)
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
    weapon["baseclass"] = input("Enter the weapon's' baseclass (basically how the weapon functions): ")
    try:
        weapon["baseindex"] = str(int(input("Enter the weapon's baseindex used for sounds and model: ")))
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