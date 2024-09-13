# extract-lcl-bank-statement
convert pdf bank statement lcl to excel editable format

Ce projet utilise tabula-py pour extraire des données tabulaires de fichiers PDF et les convertir en fichiers Excel. Les fichiers PDF sont pris depuis un dossier source et les fichiers Excel générés sont sauvegardés dans un dossier cible avec des noms correspondant aux fichiers PDF d'origine.

## Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

Python 3.x
Java (Tabula repose sur Java pour fonctionner)
Les bibliothèques Python suivantes :
tabula-py : Pour extraire des tableaux depuis des fichiers PDF.
pandas : Pour manipuler et sauvegarder les données sous forme de DataFrame.
openpyxl : Pour écrire des fichiers Excel.

## Installation des dépendances
### Utilisez pip pour installer les bibliothèques nécessaires :

pip install tabula-py pandas openpyxl
Assurez-vous que Java est installé et que son chemin est ajouté à la variable d'environnement PATH.

## Structure du Dossier
Le projet est organisé comme suit :

project-directory/
│
├── pdf-file/         # Dossier contenant les fichiers PDF
├── excel-file/       # Dossier où seront sauvegardés les fichiers Excel
└── script.py         # Le script Python principal

## Remplir les Dossiers :
Placez tous vos fichiers PDF dans le dossier pdf-file/.
Le dossier excel-file/ sera automatiquement rempli avec les fichiers Excel générés.
Utilisation

## Configurer les dossiers : 
Assurez-vous que le chemin du dossier PDF source (folder_path) et le chemin du dossier Excel de sortie (excel_folder_path) dans le script sont corrects. 

Par défaut, ils sont définis comme suit :

folder_path = "./pdf-file"
excel_folder_path = "./excel-file"

## Exécuter le script : 

Lancez le script en exécutant la commande suivante dans votre terminal :

python script.py

Le script parcourra le dossier contenant les fichiers PDF, extraira les tableaux de chaque PDF et sauvegardera les données dans un fichier Excel correspondant dans le dossier de sortie.

## Explication du Code
tabula.read_pdf() : Cette fonction extrait les tableaux d'un fichier PDF spécifié.
pandas.concat() : Combine tous les tableaux extraits en un seul DataFrame.
df_total.to_excel() : Sauvegarde le DataFrame combiné dans un fichier Excel.

## Gestion des fichiers : 
Le script utilise os.listdir() et os.path pour gérer la lecture des fichiers dans un dossier et la création des chemins pour chaque fichier.

## Exemple d'exécution
Lorsque vous exécutez le script, vous verrez une sortie indiquant que chaque fichier Excel a été généré avec succès, par exemple :


Le fichier report1.xlsx a été sauvegardé sous le nom : ./excel-file/report1.xlsx
Le fichier report2.xlsx a été sauvegardé sous le nom : ./excel-file/report2.xlsx

## Dépannage
Si vous rencontrez des erreurs avec Java, assurez-vous que Java est installé et que son chemin est correctement configuré dans la variable d'environnement PATH.
Si le fichier Excel ne se génère pas correctement, vérifiez que le fichier PDF contient bien des tableaux valides et que le module tabula-py est capable de les lire.

## Licence
Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le distribuer.
