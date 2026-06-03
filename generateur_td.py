import os

# Liste de tes dossiers (ne pas oublier le 'td_')
dossiers = ['td_l1_s1', 'td_l1_s2', 'td_l2_s1', 'td_l2_s2']
fichier_sortie = 'resultat_td.html'

with open(fichier_sortie, 'w', encoding='utf-8') as f:
    f.write('<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">\n')

    for dossier in dossiers:
        if os.path.exists(dossier):
            d_nom = dossier.lower()
            
            # Détermination du Niveau et du Semestre (S1 à S4)
            if d_nom == 'td_l1_s1':
                niv, sem_affiche = "L1", "S1"
            elif d_nom == 'td_l1_s2':
                niv, sem_affiche = "L1", "S2"
            elif d_nom == 'td_l2_s1':
                niv, sem_affiche = "L2", "S3"
            elif d_nom == 'td_l2_s2':
                niv, sem_affiche = "L2", "S4"
            else:
                niv, sem_affiche = "Inconnu", "Inconnu"

            for filename in os.listdir(dossier):
                if filename.endswith(".pdf"):
                    name_display = os.path.splitext(filename)[0].replace('_', ' ')
                    
                    # --- GENERATION DE LA CARD ---
                    card = f'    <div class="glass-card" data-licence="{niv}" data-semestre="{sem_affiche}">\n'
                    # Titre forcé en BLANC
                    card += f'        <h4 style="color: white; margin:0;">{name_display}</h4>\n'
                    # Sous-texte forcé en BLEU CLAIR (#ade8f4)
                    card += f'        <p style="font-size: 0.8rem; margin: 10px 0; color: #ade8f4;">Niveau : {niv} - Semestre : {sem_affiche}</p>\n'
                    # Bouton standard
                    card += f'        <a href="{dossier}/{filename}" target="_blank" class="btn-subject" style="display:block; text-align:center;">Ouvrir le TD</a>\n'
                    card += f'    </div>\n\n'
                    f.write(card)
        else:
            print(f"Dossier '{dossier}' non trouvé.")

    f.write('</div>')

print(f"Fait ! Les cartes ont été générées dans {fichier_sortie}")