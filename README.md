# DSA Cryptographic Signing Application

## Description

Cette application permet de signer un message à l'aide de l'algorithme **Digital Signature Algorithm (DSA)**. Elle génère une paire de clés publique et privée, et permet de signer un message, ainsi que de vérifier la signature d'un message en utilisant la clé publique correspondante. L'interface est construite à l'aide de **PyQt5** pour la gestion graphique de l'application.

## Fonctionnalités

- **Génération de clés** : Génère une paire de clés DSA publique et privée.
- **Signature de message** : Permet de signer un message à l'aide de la clé privée.
- **Vérification de signature** : Permet de vérifier si la signature d'un message est valide en utilisant la clé publique.
- **Gestion des fichiers** : Ouvre des fichiers pour charger le message, la clé publique et la signature.
- **Sauvegarde des données** : Sauvegarde les clés générées et la signature dans des fichiers texte.

## Prérequis

Pour faire fonctionner cette application, assurez-vous d'avoir installé les modules suivants :

- **cryptography**
- **PyQt5**
- **sys**
- **os**
- **datetime**

Vous pouvez installer ces modules via pip :

bash
pip install cryptography PyQt5

Installation

    Clonez ou téléchargez ce projet sur votre machine.
    Installez les dépendances avec pip.
    Lancez l'application avec la commande suivante :

python DSA_main.py

Utilisation

    Générer les clés : Cliquez sur le bouton "Générer les clés" pour générer une paire de clés publique et privée.
    Signer un message : Saisissez le message dans le champ prévu à cet effet et cliquez sur "Signer". La signature sera affichée dans l'interface.
    Vérifier une signature : Chargez un fichier contenant la clé publique, un fichier contenant la signature et un fichier contenant le message à vérifier, puis cliquez sur "Vérifier". L'application affichera si la signature est valide ou non.

Fichiers générés

    Clé publique : Le fichier contenant la clé publique générée.
    Clé privée : Le fichier contenant la clé privée générée.
    Signature : Le fichier contenant la signature générée.
    Message : Le fichier contenant le message signé.

Tous ces fichiers sont enregistrés dans un dossier DSA data avec des sous-dossiers pour organiser les différents types de fichiers.

Exemple de workflow

    Générez les clés.
    Signez un message en saisissant le texte dans le champ approprié.
    Sauvegardez les fichiers générés : la clé publique, la clé privée, la signature, et le message.
    Ouvrez ces fichiers avec l'explorateur de fichiers de l'application pour vérifier la signature.

Interface utilisateur

L'application utilise une interface graphique simple avec des champs de texte pour saisir et afficher les messages et signatures. Elle comprend également des boutons pour générer des clés, signer des messages, et vérifier les signatures.

Auteurs

    TAKAM TCHEUTCHOUA JUNIOR
    Contributeurs : Si tu souhaites contribuer à cette application, n'hésite pas à soumettre des pull requests ou à ouvrir des issues pour toute amélioration ou problème rencontré.

Licence

Distribué sous la licence MIT.
