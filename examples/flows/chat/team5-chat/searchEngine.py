from promptflow import tool
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input_str: str) -> str:
    # 쉼표로 문자열을 분리하고 공백 제거
    keywords = [keyword.strip() for keyword in input_str.split(',')]

    endpoint = "https://team5.search.windows.net"
    admin_key = "CCefw1LqUUHbCJ9fGHnGvi7LsGOCSW74w4K8SVFVtOAzSeAll29Y"
    index = "info1"
    search_client = SearchClient(endpoint=endpoint,
                      index_name=index,
                      api_version="2021-04-30-Preview",
                      credential=AzureKeyCredential(admin_key))

    information = {}

    # 각 키워드에 대해 검색 수행
    for keyword in keywords:
        results = search_client.search(search_text=keyword, top=3, include_total_count=True)

        # 검색 결과에서 원하는 정보 추출 (여기서는 'chunk' 필드를 사용한다고 가정)
        output = [result["chunk"] for result in results]

        # 결과 문자열을 공백으로 연결
        intermediate_output = " ".join(output)

        # 딕셔너리에 저장
        information[keyword] = intermediate_output
        
    print("A------------------")
    print(str(keywords))
    print(str(information) )

    return str(information) 
