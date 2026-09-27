import sys
from pathlib import Path
from scanner import PhotoScanner

def main():
    # Chemins à adapter selon l'emplacement de vos dossiers
    dossier_source = Path(r"C:\Chemin\Vers\Photos_Source")
    dossier_destination = Path(r"C:\Chemin\Vers\Photos_Destination_Propre")
    
    print("Démarrage de PhotoVault v0.2 (Production)...")
    print(f"Source : {dossier_source}")
    print(f"Destination : {dossier_destination}\n")
    
    if not dossier_source.exists():
        print(f"Erreur : Le dossier source n'existe pas. Vérifiez le chemin.")
        sys.exit(1)
        
    scanner = PhotoScanner(str(dossier_source), str(dossier_destination))
    scanner.executer()

if __name__ == "__main__":
    main()
