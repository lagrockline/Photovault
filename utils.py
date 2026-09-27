import hashlib
from pathlib import Path

def calculer_sha1(chemin_fichier: Path) -> str:
    """Calcule l'empreinte SHA-1 d'un fichier de manière optimisée."""
    hachage = hashlib.sha1()
    
    try:
        with open(chemin_fichier, 'rb') as f:
            for bloc in iter(lambda: f.read(65536), b''):
                hachage.update(bloc)
        return hachage.hexdigest()
    except (OSError, IOError) as e:
        print(f"Erreur lors de la lecture de {chemin_fichier.name} : {e}")
        return ""
