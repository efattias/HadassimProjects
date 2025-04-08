persons = [
    {"Person_Id": 1, "Personal_Name": "Moshe", "Family_Name": "Attias", "Gender": "male", "Father_Id": 5, "Mother_Id": 6, "Spouse_Id": 2},
    {"Person_Id": 2, "Personal_Name": "Rachel", "Family_Name": "Attias", "Gender": "female", "Father_Id": None, "Mother_Id": None, "Spouse_Id": None},
    {"Person_Id": 3, "Personal_Name": "Hadas", "Family_Name": "Attias", "Gender": "female", "Father_Id": 1, "Mother_Id": 2, "Spouse_Id": None},
    {"Person_Id": 4, "Personal_Name": "Efrat", "Family_Name": "Attias", "Gender": "female", "Father_Id": 1, "Mother_Id": 2, "Spouse_Id": None},
    {"Person_Id": 5, "Personal_Name": "Benjamin", "Family_Name": "Attias", "Gender": "male", "Father_Id": None, "Mother_Id": None, "Spouse_Id": 6},
    {"Person_Id": 6, "Personal_Name": "Ester", "Family_Name": "Attias", "Gender": "female", "Father_Id": None, "Mother_Id": None, "Spouse_Id": 5},
] # person table

def build_tree(persons):
    family_tree = [] #present the relations

    person_by_id = {p["Person_Id"]: p for p in persons} # get all the ID

    for p in persons:
        pid = p["Person_Id"] # keep person id in var

        if p["Father_Id"]: # if it father relations
            family_tree.append({"Person_Id": pid, "Relative_Id": p["Father_Id"], "Connection_Type": "Father of"}) # connect father of
            family_tree.append({"Person_Id": p["Father_Id"], "Relative_Id": pid, "Connection_Type": "Son of" if p["Gender"] == "male" else "daughter of"}) # connect son/daughter of

        if p["Mother_Id"]: # if it mother relations
            family_tree.append({"Person_Id": pid, "Relative_Id": p["Mother_Id"], "Connection_Type": "Mother of"}) # connect mother of
            family_tree.append({"Person_Id": p["Mother_Id"], "Relative_Id": pid, "Connection_Type": "Son of" if p["Gender"] == "male" else "daughter of"}) # connect son/daughter of

        if p["Spouse_Id"]: # if it spouse relations
            spouse = person_by_id.get(p["Spouse_Id"])
            if spouse:
                conn_type = "Spouse of" if p["Gender"] == "male" else "Spouse of" # connect spouse of
                family_tree.append({"Person_Id": pid, "Relative_Id": spouse["Person_Id"], "Connection_Type": conn_type}) # connect spouse of

        for other in persons: # find sibling
            if other["Person_Id"] == pid:
                continue
            if (p["Father_Id"] == other["Father_Id"] and
                p["Mother_Id"] == other["Mother_Id"] and
                p["Father_Id"] is not None and
                p["Mother_Id"] is not None):
                conn_type = "Brother of" if other["Gender"] == "male" else "Sister of" 
                family_tree.append({"Person_Id": pid, "Relative_Id": other["Person_Id"], "Connection_Type": conn_type}) # connect sister of

    return family_tree

def main():
    tree = build_tree(persons) 
    for row in tree: # print tree
        print(row)

if __name__ == "__main__":
    main()