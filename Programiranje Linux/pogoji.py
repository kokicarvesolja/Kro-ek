# uporabnik naj vpiše številko meseca
# mi mu odgovorimo s število v milisekund v mesecu

uporabnikov_mesec = int(input("Za kateri mesec bi želel vedeti število milisekund? "))

milis_v_dnevu = 24 * 60 * 60 * 1000

if uporabnikov_mesec == 1 or uporabnikov_mesec == 3 or uporabnikov_mesec == 5 or uporabnikov_mesec == 7 or uporabnikov_mesec == 8 or uporabnikov_mesec == 10 or uporabnikov_mesec == 12: 
    stevilo_milis_v_mesecu = milis_v_dnevu * 31
elif uporabnikov_mesec == 2:
    stevilo_milis_v_mesecu = milis_v_dnevu * 28
elif uporabnikov_mesec > 12:
    print ("Ni toliko mesecev.")
else:
    stevilo_milis_v_mesecu = milis_v_dnevu * 30

print (" Število milisekund v ", uporabnikov_mesec, " mesecu je: ", stevilo_milis_v_mesecu )