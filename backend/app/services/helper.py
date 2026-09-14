straight_he = "אבגדהוזחטיכלמנסעפצקרשת"
opposite_he = straight_he[:: -1]
he_end_letters_str = "ךםןףץ"
he_end_letters_opp = "ליטוה"

straight_en_sm = "abcdefghijklmnopqrstuvwxyz"
opposite_en_sm = straight_en_sm[::-1]
straight_en_lg = straight_en_sm.upper()
opposite_en_lg = straight_en_lg[:: -1]

at_bash_dict = {}
for i in range(len(straight_he)):
    at_bash_dict[straight_he[i]] = opposite_he[i]

for i in range(len(he_end_letters_str)):
    at_bash_dict[he_end_letters_str[i]] = he_end_letters_opp[i]

for i in range(len(straight_en_sm)):
    at_bash_dict[straight_en_sm[i]] = opposite_en_sm[i]
    at_bash_dict[straight_en_lg[i]] = opposite_en_lg[i]

