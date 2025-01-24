#importation des modules pour la cryptographie
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# importation des differents modules de PyQt5
from PyQt5 import QtCore, QtWidgets, QtGui, uic, Qt
from PyQt5.uic import loadUi
from PyQt5.QtGui import QTextCursor, QFontMetrics, QFont, QIcon
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QSize
from functools import partial  # pour envoyer un parametre à une fonction avec connect()

# importation des differents modules de communication, parallelisme
import sys,os
from datetime import *

class DSA_main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("dsa.ui", self)

        #        ________             la partie accueil            __________

        self.pushButton_ouvrir_fichier_clair.clicked.connect(self.ouvrir_l_explorateur)
        self.fichier_selectionne = ""
        self.fichier_selectionne_ = ""

        self.pushButton_generer_cle.clicked.connect(self.generate_keys)

        self.private_key_value = None
        self.public_key_value = None

        self.pushButton_afficher_cle_publique.clicked.connect(self.afficher_cle_publique)
        self.pushButton_afficher_cle_prive.clicked.connect(self.afficher_cle_privee)

        self.pushButton_signer.clicked.connect(self.signer_message)

        self.signature = None

        self.pushButton_ouvrir_cle_publique.clicked.connect(self.ouvrir_cle_publique)
        self.pushButton_ouvrir_signature.clicked.connect(self.ouvrir_signature)
        self.pushButton_ouvrir_message.clicked.connect(self.ouvrir_message)

        self.pushButton_verifier.clicked.connect(self.verifier_message)


    # fonction pour calculer la clé publique et privée
    def generate_keys(self, ):
        # Génération d'une paire de clés DSA

        self.private_key = dsa.generate_private_key(
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

        # Affichage de la clé publique
        public_key_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        self.public_key_value = public_key_pem.decode()

        # Affichage de la clé privée
        private_key_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        self.private_key_value = private_key_pem.decode()





        self.notification("Clés publique et privée générées avec succès")

    def afficher_cle_publique(self):

        self.notification("Clé publique:\n " +str(self.public_key_value))

    def afficher_cle_privee(self):
        self.notification("Clé privée:\n " +str(self.private_key_value))

    def signer_message(self):
        message = b"Exemple de message a signer"
        a = "bon"
        self.plaintext_chiff = self.textEdit_entrer_texte.toPlainText()
        # Signature du message
        self.signature = self.private_key.sign(
            self.plaintext_chiff.encode('utf-8'),
            hashes.SHA256()
        )




        #creation des dossiers
        if not os.path.exists("DSA data"):
            os.makedirs("DSA data")
        if not os.path.exists("DSA data/data sign"):
            os.makedirs("DSA data/data sign")

        if not os.path.exists("DSA data/data sign/public key"):
            os.makedirs("DSA data/data sign/public key")
        if not os.path.exists("DSA data/data sign/private key"):
            os.makedirs("DSA data/data sign/private key")
        if not os.path.exists("DSA data/data sign/signature"):
            os.makedirs("DSA data/data sign/signature")
        if not os.path.exists("DSA data/data sign/message"):
            os.makedirs("DSA data/data sign/message")


        public_file = "DSA data/data sign/public key/public_key "+str(datetime.now())+".txt"
        public_file = public_file.replace("-","_")
        public_file = public_file.replace(":", "_")
        file = open(public_file, "w+")
        file.write(str(self.public_key_value))
        file.close()

        private_file = "DSA data/data sign/private key/private_key " + str(datetime.now()) + ".txt"
        private_file = private_file.replace("-", "_")
        private_file = private_file.replace(":", "_")
        file = open(private_file, "w+")
        file.write(str(self.private_key_value))
        file.close()

        signature_file = "DSA data/data sign/signature/signature " + str(datetime.now()) + ".txt"
        signature_file = signature_file.replace("-", "_")
        signature_file = signature_file.replace(":", "_")
        file = open(signature_file, "w+")
        file.write(str(self.signature))
        file.close()

        message_file = "DSA data/data sign/message/message " + str(datetime.now()) + ".txt"
        message_file = message_file.replace("-", "_")
        message_file = message_file.replace(":", "_")
        file = open(message_file, "w+")
        file.write(self.plaintext_chiff)
        file.close()


        self.textBrowser_signature.setText(str(self.signature))
        self.notification("Signature effectuée avec succès")

    def ouvrir_cle_publique(self):
        # Explorateur de fichier
        self.fileDialog = QtWidgets.QFileDialog()

        self.fileDialog.setFileMode(self.fileDialog.AnyFile)
        self.fileDialog.setNameFilter("[Text files (*.txt)]")

        if self.fileDialog.exec_():
            filepath = self.fileDialog.selectedFiles()
            self.fichier_selectionne = filepath[0]

            with open(self.fichier_selectionne, 'r', encoding='utf-8') as f:  # Recup de la clé
                self.cle_publique_verify = f.read()
                self.lineEdit_fichier_cle_publique.setText(self.fichier_selectionne)

    def ouvrir_signature(self):
        # Explorateur de fichier
        self.fileDialog = QtWidgets.QFileDialog()

        self.fileDialog.setFileMode(self.fileDialog.AnyFile)
        self.fileDialog.setNameFilter("[Text files (*.txt)]")

        if self.fileDialog.exec_():
            filepath = self.fileDialog.selectedFiles()
            self.fichier_selectionne = filepath[0]

            with open(self.fichier_selectionne, 'r', encoding='utf-8') as f:  # Recup de la clé
                self.signature_verify = f.read()
                self.lineEdit_fichier_signature.setText(self.fichier_selectionne)

    def ouvrir_message(self):
        # Explorateur de fichier
        self.fileDialog = QtWidgets.QFileDialog()

        self.fileDialog.setFileMode(self.fileDialog.AnyFile)
        self.fileDialog.setNameFilter("[Text files (*.txt)]")

        if self.fileDialog.exec_():
            filepath = self.fileDialog.selectedFiles()
            self.fichier_selectionne = filepath[0]

            with open(self.fichier_selectionne, 'r', encoding='utf-8') as f:  # Recup de la clé
                self.message_verify = f.read()
                self.label_fichier_message.setText(self.fichier_selectionne)



    def verifier_message(self):
        if self.cle_publique_verify == self.public_key_value:
            try:
                self.public_key.verify(
                    eval(self.signature_verify),
                    self.message_verify.encode('utf-8'),
                    hashes.SHA256()
                )
                self.textBrowser_resultat.setText("Signature valide")
            except:
                self.textBrowser_resultat.setText("Signature invalide")


    def ouvrir_l_explorateur(self):
        # Explorateur de fichier
        self.fileDialog = QtWidgets.QFileDialog()

        self.fileDialog.setFileMode(self.fileDialog.AnyFile)
        self.fileDialog.setNameFilter("[Text files (*.txt)]")

        if self.fileDialog.exec_():
            filepath = self.fileDialog.selectedFiles()
            self.fichier_selectionne = filepath[0]

            with open(self.fichier_selectionne, 'r', encoding='utf-8') as f:  # Recup de la clé
                self.plaintext_chiff = f.read()
                self.textEdit_entrer_texte.setText(self.plaintext_chiff)


    def notification(self, msg):

        self.fenetre_notification = QtWidgets.QMainWindow()

        self.fenetre_notification.setGeometry(
            QtCore.QRect(self.x() + int(self.width() / 2) - 130 - 15, self.y() + int(self.height() / 2)-50, 200, 147))
        loadUi("notification.ui", self.fenetre_notification)

        # rend modale la 2ème fenêtre (la 1ère fenêtre sera inactive)
        self.fenetre_notification.setWindowModality(QtCore.Qt.ApplicationModal)
        self.fenetre_notification.label_erreur.setText(msg)

        # affiche la 2ème fenêtre
        self.fenetre_notification.show()


# """
app = QtWidgets.QApplication(sys.argv)
mainWindow = DSA_main()
mainWindow.show()
sys.exit(app.exec_())
# """
