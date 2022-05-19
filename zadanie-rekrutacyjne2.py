tekst1 = "ilśeJ ycsyzsw ąlśym kat ,omas ot śotk ein ilsym elacw"

tekst2 = tekst1.split()
tekst_odwrocony =[]

for i in tekst2:
    i = i[::-1]
    tekst_odwrocony.append(i)
    
print("napis oryginalny: ", tekst1)
print("napis po odwroceniu")
print(" ".join(tekst_odwrocony))


        


