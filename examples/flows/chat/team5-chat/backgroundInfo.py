from promptflow import tool
import openai
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

openai.api_type = "azure"
openai.api_version = "2023-06-01-preview"
openai.api_key = "CCefw1LqUUHbCJ9fGHnGvi7LsGOCSW74w4K8SVFVtOAzSeAll29Y"
openai.api_base = "https://team5.search.windows.net"


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool() -> str:
    st = {
  "name": "빅토리아 아일랜드",
  "type": "continent",
  "description": "메이플 월드의 거대한 섬으로, 중앙의 슬리피우드를 중심으로 네 개의 마을과 두 개의 항구가 있다. 각 마을의 장로들은 전직 교관 역할을 한다.",
  "childs": [
    {
      "name": "리스항구",
      "type": "town",
      "description": "빅토리아 아일랜드의 항구 마을",
      "childs": [],
      "parents": ["빅토리아 아일랜드"],
      "npc": [],
      "monster": []
    },
    {
      "name": "헤네시스",
      "type": "town",
      "description": "빅토리아 아일랜드의 중요 마을 중 하나",
      "childs": [],
      "parents": ["빅토리아 아일랜드"],
      "npc": [],
      "monster": []
    },
    {
      "name": "에우렐",
      "type": "town",
      "description": "빅토리아 아일랜드에 위치한 작은 마을",
      "childs": [],
      "parents": ["빅토리아 아일랜드"],
      "npc": [],
      "monster": []
    },
    {
      "name": "엘리니아",
      "type": "town",
      "description": "엘린숲으로 이어지는 빅토리아 아일랜드의 중요한 마을",
      "childs": [],
      "parents": ["빅토리아 아일랜드"],
      "npc": [],
      "monster": []
    },
    {
      "name": "파르템",
      "type": "town",
      "description": "고대 유적지로 이어지는 빅토리아 아일랜드의 마을",
      "childs": [],
      "parents": ["빅토리아 아일랜드"],
      "npc": [],
      "monster": []
    },
    {
      "name": "커닝시티",
      "type": "town",
      "description": "빅토리아 아일랜드 내의 번화한 마을",
      "childs": [],
      "parents": ["빅토리아 아일랜드"],
      "npc": [],
      "monster": []
    },
    {
      "name": "페리온",
      "type": "town",
      "description": "빅토리아 아일랜드의 전사 마을",
      "childs": [],
      "parents": ["빅토리아 아일랜드"],
      "npc": [],
      "monster": []
    },
    {
      "name": "슬리피우드",
      "type": "town",
      "description": "빅토리아 아일랜드 중앙에 위치한 마을",
      "childs": [],
      "parents": ["빅토리아 아일랜드"],
      "npc": [],
      "monster": []
    },
    {
      "name": "노틸러스",
      "type": "town",
      "description": "빅토리아 아일랜드의 해상 마을",
      "childs": [],
      "parents": ["빅토리아 아일랜드"],
      "npc": [],
      "monster": []
    },
    {
      "name": "플로리나 비치",
      "type": "town",
      "description": "빅토리아 아일랜드의 해변 지역",
      "childs": [],
      "parents": ["빅토리아 아일랜드"],
      "npc": [],
      "monster": []
    }
  ]
}

    return st
