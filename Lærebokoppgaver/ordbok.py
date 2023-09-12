meg = {
    "fornavn": "Evelyn Rose",
    "etternavn": "Stellberg",
    "foedselsaar": "2005"
}

print(f"{meg['fornavn']} {meg['etternavn']} er født i {meg['foedselsaar']}")

for noekkel, verdi in meg.items():
    print(f"Nøkkel: {noekkel}, verdi: {verdi}.")