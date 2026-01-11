# ☁️ Azure Cloud Automation - Moje początki

Cześć! To repozytorium dokumentuje moją drogę od Helpdesku do Architekta Chmury Azure.
Nie chcę być "klikaczem" w portalu, więc od razu uczę się zarządzać infrastrukturą przez kod (Infrastructure as Code).

To miejsce, gdzie wrzucam moje skrypty w Pythonie, testy i laby.

##  Co tu jest?
Na start wrzuciłem skrypt `azure_inventory.py`.
To proste narzędzie, które:
1. Bezpiecznie loguje się do mojego konta Azure (bez trzymania haseł w kodzie!).
2. Łączy się z API Azure Resource Manager.
3. Sprawdza i wypisuje w terminalu listę dostępnych Grup Zasobów (Resource Groups).

##  Technologie
Co zostało użyte:
* **Język:** Python 3.x
* **Biblioteki:** `azure-identity`, `azure-mgmt-resource`
* **Narzędzia:** VS Code, Azure CLI, Git

##  Jak to uruchomić?
Jeśli chcesz przetestować ten kod u siebie:

1. Zainstaluj zależności:
   
   pip install azure-identity azure-mgmt-resource

2.   Zaloguj się do swojego Azure w terminalu:
   
   az login

3. W pliku azure_inventory.py podmień subscription_id na swoje ID.

Odpal skrypt:

python azure_inventory.py


Czego się nauczyłem przy tym projekcie?
-Jak skonfigurować lokalne środowisko do pracy z chmurą (VS Code + Azure SDK).
-Dlaczego DefaultAzureCredential jest lepsze niż wpisywanie loginu i hasła na sztywno.
-Jak iterować po zasobach chmurowych za pomocą Pythona.