from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchIndexClient

# Substitua pelo seu endpoint do Azure Search
endpoint = "<seu_endpoint_azure_search>"  
credential = DefaultAzureCredential()

try:
    client = SearchIndexClient(endpoint=endpoint, credential=credential)
    indices = client.list_index_names()
    print("Índices disponíveis:", list(indices))
except Exception as e:
    print(f"Erro ao listar índices: {e}")
