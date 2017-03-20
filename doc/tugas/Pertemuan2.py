graph = {
             'Sarijadi': ['Jl. Sutami'],
             'Jl. Sutami': ['Jl. Nendeut'],
             'Jl. Nendeut': ['Jl. Suryasumantri'],
             'Jl. Suryasumantri': ['Jl. Pasteur'],
			 'Jl. Pasteur': ['Jl. Pasupati'],
			 'Jl. Pasupati': ['Jl. Surapati'],
             'Jl. Surapati': ['Cicaheum'],
        }

def mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[]):
        jalur = jalur + [jalanawal]
        if jalanawal == jalantujuan:
            return jalur
            if not graph.has_key(jalanawal):
                    return None
        jalurpendek = None
        for node in graph[jalanawal]:
            if node not in jalur:
                newjalur = mencari_jalur_terpendek(graph, node, jalantujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalur Sarijadi sampai Cicaheum")
print("(Sarijadi,Jl. Sutami,Jl. Neundeut,Jl. Suryasumantri,Jl. Pasteur,Jl. Pasupati,Jl. Surapati,Cicaheum)")
print("\n")
jalanawal = raw_input("Masukan jalanawal : ")
jalantujuan = raw_input("Masukan jalantujuan : ")
hasil = mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[])
print "Jalur Terpendek", hasil
