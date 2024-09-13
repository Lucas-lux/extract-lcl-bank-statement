import tabula
import pandas as pd
import os

# Chemin vers le dossier contenant les fichiers PDF et le dossier Excel
folder_path = "./pdf-file"
excel_folder_path = "./excel-file"

# Parcours de tous les fichiers du dossier
for file_name in os.listdir(folder_path):
    if file_name.endswith(".pdf"):
        # Construction du chemin complet vers chaque fichier PDF
        pdf_path = os.path.join(folder_path, file_name)

        # Extraction des tableaux depuis le PDF
        tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

        # Combinaison des tableaux dans un DataFrame unique
        df_total = pd.concat(tables)

        # Création du nom de fichier Excel basé sur le nom du fichier PDF
        excel_name = os.path.splitext(file_name)[0] + ".xlsx"
        excel_path = os.path.join(excel_folder_path, excel_name)

        # Exportation des données vers un fichier Excel
        df_total.to_excel(excel_path, index=False)

        print(f"Le fichier {excel_name} a été sauvegardé sous le nom : {excel_path}")