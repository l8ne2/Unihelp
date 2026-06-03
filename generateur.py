import os

# Configuration des dossiers à scanner
dossiers = ['l2_s2']
fichier_sortie = 'resultat_tableau.html'

with open(fichier_sortie, 'w', encoding='utf-8') as f:
    f.write('<table class="table-subjects">\n')
    f.write('  <thead>\n    <tr><th>Nom du Sujet</th><th>Niveau</th><th>Action</th></tr>\n  </thead>\n')
    f.write('  <tbody>\n')

    for dossier in dossiers:
        if os.path.exists(dossier):
            for filename in os.listdir(dossier):
                if filename.endswith(".pdf"):
                    name_clean = os.path.splitext(filename)[0].replace('_', ' ')
                    label = dossier.upper().replace('_', ' ')
                    
                    # --- CORRECTION ICI ---
                    # dossier[:2] récupère "l2", puis .upper() le transforme en "L2"
                    niveau_auto = dossier[:2].upper() 
                    # dossier[-2:] récupère "s1", puis .upper() le transforme en "S1"
                    semestre_auto = dossier[-2:].upper()
                    
                    # On utilise maintenant niveau_auto au lieu de "L1"
                    ligne = f'    <tr data-licence="{niveau_auto}" data-semestre="{semestre_auto}">\n'
                    ligne += f'      <td>{name_clean}</td>\n'
                    ligne += f'      <td>{label}</td>\n'
                    ligne += f'      <td><a href="{dossier}/{filename}" target="_blank" class="btn-subject">Lire le PDF</a></td>\n'
                    ligne += f'    </tr>\n'
                    
                    f.write(ligne)
        else:
            print(f"Attention : Le dossier {dossier} n'existe pas.")

    f.write('  </tbody>\n</table>')

print(f"Terminé ! Le tableau affiche maintenant {dossiers} correctement.")