hp = 100
spaider_onehit = 40
thombi_onehit = 5
skelet_onehit = 15
hits = skelet_onehit + 2*spaider_onehit + 5*thombi_onehit
if hp > hits:
    print("stay alive")
else:
    print("die")