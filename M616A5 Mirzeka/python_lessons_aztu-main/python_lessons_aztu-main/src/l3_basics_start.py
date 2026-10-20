row = {"cell_id": "BAK-0207", "region": "Nesimi", "rsrp_dbm": -108.1}
print(row["region"])
print(row["rsrp_dbm"])
row["band"] = "LTE800"
print(row)

row["region"]="Yasamal"
print(row)


rsrp_list = [-91.5, -108.1, -86.2, -103.3, -110.4]
for v in rsrp_list:
    print(v)
    v = v * int(input())
    print(v)
