import sys
from pathlib import Path
import shutil
from media import MediaFile
from utils import calculer_sha1

class PhotoScanner:
    def __init__(self, source_dir: str, dest_dir: str):
        self.source = Path(source_dir)
        self.destination = Path(dest_dir)
        self.stats = {
            "images_copiees": 0, 
            "live_ignorees": 0, 
            "videos_copiees": 0,
            "doublons_ignores": 0,
            "octets_gagnes": 0
        }

    def afficher_progression(self, actuel: int, total: int, message: str):
        """Affiche une barre de progression textuelle dynamique dans le terminal."""
        if total == 0:
            return
        taille_barre = 30
        progression = actuel / total
        blocs = int(taille_barre * progression)
        barre = "█" * blocs + "-" * (taille_barre - blocs)
        pourcentage = progression * 100
        sys.stdout.write(f"\r{message:<35} [{barre}] {pourcentage:.1f}% ({actuel}/{total})")
        sys.stdout.flush()

    def executer(self):
        self.destination.mkdir(exist_ok=True)
        
        fichiers_dest = [f for f in self.destination.iterdir() if f.is_file()]
        total_dest = len(fichiers_dest)
        sha1_existants = set()
        
        if total_dest > 0:
            for i, f in enumerate(fichiers_dest, 1):
                empreinte = calculer_sha1(f)
                if empreinte:
                    sha1_existants.add(empreinte)
                self.afficher_progression(i, total_dest, "Indexation de la destination")
            print()
        else:
            print("Indexation de la destination : Aucun fichier existant (Dossier propre).")
        
        tous_les_fichiers = [MediaFile(f) for f in self.source.iterdir() if f.is_file()]
        total_source = len(tous_les_fichiers)
        heic_stems = {f.stem for f in tous_les_fichiers if f.suffix == ".heic"}
        
        for i, media in enumerate(tous_les_fichiers, 1):
            self.afficher_progression(i, total_source, "Analyse et traitement de la source")
            
            if media.is_video() and media.stem in heic_stems:
                self.stats["live_ignorees"] += 1
                try:
                    self.stats["octets_gagnes"] += media.path.stat().st_size
                except OSError:
                    pass
                continue

            empreinte_source = calculer_sha1(media.path)
            
            if len(sha1_existants) > 0 and empreinte_source in sha1_existants:
                self.stats["doublons_ignores"] += 1
                try:
                    self.stats["octets_gagnes"] += media.path.stat().st_size
                except OSError:
                    pass
                continue

            if media.is_image():
                shutil.copy2(media.path, self.destination / media.name)
                self.stats["images_copiees"] += 1
                if empreinte_source:
                    sha1_existants.add(empreinte_source)
                
            elif media.is_video():
                shutil.copy2(media.path, self.destination / media.name)
                self.stats["videos_copiees"] += 1
                if empreinte_source:
                    sha1_existants.add(empreinte_source)
                    
        print()
        self.afficher_rapport()

    def formater_taille(self, octets: int) -> str:
        if octets >= 1024**3:
            return f"{octets / (1024**3):.2f} Go"
        return f"{octets / (1024**2):.2f} Mo"

    def afficher_rapport(self):
        espace_economise = self.formater_taille(self.stats["octets_gagnes"])
        print("\n--- RAPPORT PHOTOVAULT v0.2 (PROGRESSION SEULE) ---")
        print(f"Photos copiées (sans Live)           : {self.stats['images_copiees']}")
        print(f"Vraies vidéos préservées             : {self.stats['videos_copiees']}")
        print(f"Vidéos Live ignorées (écartées)     : {self.stats['live_ignorees']}")
        print(f"Doublons stricts ignorés (SHA-1)    : {self.stats['doublons_ignores']}")
        print("-" * 54)
        print(f"ESPACE TOTAL RÉCUPÉRÉ (GAGNÉ)       : {espace_economise}")
        print("-" * 54)
