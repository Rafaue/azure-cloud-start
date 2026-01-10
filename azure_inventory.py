import os
# Import biblioteki do logowania się do Azure
from azure.identity import DefaultAzureCredential
# Importujemy bibliotekę do zarządzania zasobami
from azure.mgmt.resource import ResourceManagementClient

def main():
    print("łączenie z Azure...")

    # KROK 1: Uwierzytelnienie
    credential = DefaultAzureCredential()

    # KROK 2: ID Subskrypcji

    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID", "TWOJE_ID_SUBSKRYPCJI_WPISZ_TUTAJ")

    resource_client = ResourceManagementClient(credential, subscription_id)

    print(f"✅ Połączono z subskrypcją: {subscription_id}")
    print("-" * 30)
    print("📦 Lista Twoich grup zasobów (Resource Groups):")

    # KROK 3: Pobranie listy i wyświetlenie
    rg_list = resource_client.resource_groups.list()
    
    found = False
    for rg in rg_list:
        print(f" -> Nazwa: {rg.name} | Lokalizacja: {rg.location}")
        found = True
    
    if not found:
        print(" -> Nie znaleziono żadnych grup zasobów. Stwórz coś w portalu!")

if __name__ == "__main__":
    main()