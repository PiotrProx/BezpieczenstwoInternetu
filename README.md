Autorzy: Piotr Potomski oraz Otabil Ankomah
# Szyfrator-deszyfrator 

### Opis
Skrypt stworzony na kurs Bezpieczeństwo Internetu. Ukrywa wiadomości w obrazach oraz plikach wav oraz posiada możliwośc och późniejszego odszyfrowania. 
Skrypt daje możliwość ukrywania wiadomości w obrazie 3 różnymi algorymami (2 bez klucza, 1 z kluczem) oraz wspiera jeden algorytm ukrywania wiadomości w plikach wav.
Dodatkowo skypt pozwala na generowanie 32-bitowych kluczy. 


### Użycie
1. Skypt należy uruchomić uruchamiając *App_gui.py*. <br>Strona startowa:
![Alt text](E:\Szyfrator-Deszyfrator\apliakacja1.PNG?raw=true "Title")
   
W powyższym pliku znajdują sie wszystkie funkcje i elementy odpowiedzialne za intergejs programu. <br><br>
Kolejno w plikach *EncryptMessage.py* oraz *DecryptMessage.py* zaimplementowane zostały metody szyfrujące oraz deszyfrujące wiadomość z obrazu/dźwięku.<br>

Wygenerowane klucze zapisują się w folderze *Gui* pod nazwą *key*. Pliki z zakodowaną wiadomością zapisują się z dopiską  *_hidden*