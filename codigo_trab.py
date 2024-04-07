{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/GiuliaRomas/Deep/blob/main/codigo_trab.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Instala pacotes\n",
        "\n",
        "- Langchain - https://www.langchain.com/\n",
        "- Weaviate - https://weaviate.io/\n"
      ],
      "metadata": {
        "id": "B78sQmvhiIjX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "%pip install langchain openai weaviate-client wikipedia tiktoken langchain-openai\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A725D3O3h-jU",
        "outputId": "aaece402-d6cc-4c06-e6b3-de92ba1cbb5d"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: langchain in /usr/local/lib/python3.10/dist-packages (0.1.14)\n",
            "Requirement already satisfied: openai in /usr/local/lib/python3.10/dist-packages (1.16.2)\n",
            "Requirement already satisfied: weaviate-client in /usr/local/lib/python3.10/dist-packages (4.5.5)\n",
            "Collecting wikipedia\n",
            "  Downloading wikipedia-1.4.0.tar.gz (27 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: tiktoken in /usr/local/lib/python3.10/dist-packages (0.6.0)\n",
            "Requirement already satisfied: langchain-openai in /usr/local/lib/python3.10/dist-packages (0.1.1)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.10/dist-packages (from langchain) (6.0.1)\n",
            "Requirement already satisfied: SQLAlchemy<3,>=1.4 in /usr/local/lib/python3.10/dist-packages (from langchain) (2.0.29)\n",
            "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /usr/local/lib/python3.10/dist-packages (from langchain) (3.9.3)\n",
            "Requirement already satisfied: async-timeout<5.0.0,>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from langchain) (4.0.3)\n",
            "Requirement already satisfied: dataclasses-json<0.7,>=0.5.7 in /usr/local/lib/python3.10/dist-packages (from langchain) (0.6.4)\n",
            "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.10/dist-packages (from langchain) (1.33)\n",
            "Requirement already satisfied: langchain-community<0.1,>=0.0.30 in /usr/local/lib/python3.10/dist-packages (from langchain) (0.0.31)\n",
            "Requirement already satisfied: langchain-core<0.2.0,>=0.1.37 in /usr/local/lib/python3.10/dist-packages (from langchain) (0.1.40)\n",
            "Requirement already satisfied: langchain-text-splitters<0.1,>=0.0.1 in /usr/local/lib/python3.10/dist-packages (from langchain) (0.0.1)\n",
            "Requirement already satisfied: langsmith<0.2.0,>=0.1.17 in /usr/local/lib/python3.10/dist-packages (from langchain) (0.1.40)\n",
            "Requirement already satisfied: numpy<2,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain) (1.25.2)\n",
            "Requirement already satisfied: pydantic<3,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain) (2.6.4)\n",
            "Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.10/dist-packages (from langchain) (2.31.0)\n",
            "Requirement already satisfied: tenacity<9.0.0,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from langchain) (8.2.3)\n",
            "Requirement already satisfied: anyio<5,>=3.5.0 in /usr/local/lib/python3.10/dist-packages (from openai) (3.7.1)\n",
            "Requirement already satisfied: distro<2,>=1.7.0 in /usr/lib/python3/dist-packages (from openai) (1.7.0)\n",
            "Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.10/dist-packages (from openai) (0.27.0)\n",
            "Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from openai) (1.3.1)\n",
            "Requirement already satisfied: tqdm>4 in /usr/local/lib/python3.10/dist-packages (from openai) (4.66.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.7 in /usr/local/lib/python3.10/dist-packages (from openai) (4.10.0)\n",
            "Requirement already satisfied: validators==0.22.0 in /usr/local/lib/python3.10/dist-packages (from weaviate-client) (0.22.0)\n",
            "Requirement already satisfied: authlib<2.0.0,>=1.2.1 in /usr/local/lib/python3.10/dist-packages (from weaviate-client) (1.3.0)\n",
            "Requirement already satisfied: grpcio<2.0.0,>=1.57.0 in /usr/local/lib/python3.10/dist-packages (from weaviate-client) (1.62.1)\n",
            "Requirement already satisfied: grpcio-tools<2.0.0,>=1.57.0 in /usr/local/lib/python3.10/dist-packages (from weaviate-client) (1.62.1)\n",
            "Requirement already satisfied: grpcio-health-checking<2.0.0,>=1.57.0 in /usr/local/lib/python3.10/dist-packages (from weaviate-client) (1.62.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->openai) (2024.2.2)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->openai) (1.0.5)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->openai) (3.6)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.10/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai) (0.14.0)\n",
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from wikipedia) (4.12.3)\n",
            "Requirement already satisfied: regex>=2022.1.18 in /usr/local/lib/python3.10/dist-packages (from tiktoken) (2023.12.25)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.3.1)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (23.2.0)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.4.1)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (6.0.5)\n",
            "Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.9.4)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.5.0->openai) (1.2.0)\n",
            "Requirement already satisfied: cryptography in /usr/local/lib/python3.10/dist-packages (from authlib<2.0.0,>=1.2.1->weaviate-client) (42.0.5)\n",
            "Requirement already satisfied: marshmallow<4.0.0,>=3.18.0 in /usr/local/lib/python3.10/dist-packages (from dataclasses-json<0.7,>=0.5.7->langchain) (3.21.1)\n",
            "Requirement already satisfied: typing-inspect<1,>=0.4.0 in /usr/local/lib/python3.10/dist-packages (from dataclasses-json<0.7,>=0.5.7->langchain) (0.9.0)\n",
            "Requirement already satisfied: protobuf>=4.21.6 in /usr/local/lib/python3.10/dist-packages (from grpcio-health-checking<2.0.0,>=1.57.0->weaviate-client) (4.25.3)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.10/dist-packages (from grpcio-tools<2.0.0,>=1.57.0->weaviate-client) (67.7.2)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.10/dist-packages (from jsonpatch<2.0,>=1.33->langchain) (2.4)\n",
            "Requirement already satisfied: packaging<24.0,>=23.2 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2.0,>=0.1.37->langchain) (23.2)\n",
            "Requirement already satisfied: orjson<4.0.0,>=3.9.14 in /usr/local/lib/python3.10/dist-packages (from langsmith<0.2.0,>=0.1.17->langchain) (3.10.0)\n",
            "Requirement already satisfied: annotated-types>=0.4.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1->langchain) (0.6.0)\n",
            "Requirement already satisfied: pydantic-core==2.16.3 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1->langchain) (2.16.3)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain) (3.3.2)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain) (2.0.7)\n",
            "Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from SQLAlchemy<3,>=1.4->langchain) (3.0.3)\n",
            "Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->wikipedia) (2.5)\n",
            "Requirement already satisfied: mypy-extensions>=0.3.0 in /usr/local/lib/python3.10/dist-packages (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7,>=0.5.7->langchain) (1.0.0)\n",
            "Requirement already satisfied: cffi>=1.12 in /usr/local/lib/python3.10/dist-packages (from cryptography->authlib<2.0.0,>=1.2.1->weaviate-client) (1.16.0)\n",
            "Requirement already satisfied: pycparser in /usr/local/lib/python3.10/dist-packages (from cffi>=1.12->cryptography->authlib<2.0.0,>=1.2.1->weaviate-client) (2.22)\n",
            "Building wheels for collected packages: wikipedia\n",
            "  Building wheel for wikipedia (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for wikipedia: filename=wikipedia-1.4.0-py3-none-any.whl size=11680 sha256=5b133140f868b642a54b6d9dd8c96398803143b20154dbac831cf8e086234595\n",
            "  Stored in directory: /root/.cache/pip/wheels/5e/b6/c5/93f3dec388ae76edc830cb42901bb0232504dfc0df02fc50de\n",
            "Successfully built wikipedia\n",
            "Installing collected packages: wikipedia\n",
            "Successfully installed wikipedia-1.4.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Registra API_KEY para acessar APi da OpenAI\n",
        "\n",
        "https://platform.openai.com/api-keys"
      ],
      "metadata": {
        "id": "75iXoy0riLbC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "openai_api_key = os.getenv(\"OPENAI_API_KEY\", \"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\")"
      ],
      "metadata": {
        "id": "d_yfFEiPpZOT"
      },
      "execution_count": 31,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Baixar maior artigo da Wikipedia em português\n",
        "\n",
        "https://pt.wikipedia.org/wiki/Hist%C3%B3ria_do_mundo"
      ],
      "metadata": {
        "id": "7z75Gp2hRAOo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import wikipedia\n",
        "\n",
        "wikipedia.set_lang('pt')\n",
        "page = wikipedia.page('História do Mundo')\n",
        "print(page.content[:1000])\n",
        "\n",
        "with open(\"wiki.txt\", \"w\") as text_file:\n",
        "    text_file.write(page.content)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6fV-tUoXobMI",
        "outputId": "d224c626-b94b-4df3-9ab5-71460f601b65"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A história do mundo descreve a história da humanidade como determinada pelos estudos arqueológicos e registros históricos. História registrada antiga começa com a invenção da escrita.\n",
            "\n",
            "\n",
            "== Pré-História ==\n",
            "\n",
            "Há certas dúvidas sobre quais foram exatamente os nossos antepassados mais remotos. Os seres humanos modernos só surgiram há cerca de 200 mil anos. Os humanos são primatas e surgiram na África; duas espécies que pertenceram aos primórdios da evolução dos hominídeos foram o Sahelanthropus tchadensis, com um misto de características humanas e símias, e o Orrorin tugenensis, já bípede, mas não se sabe o tamanho do cérebro, que no Sahelanthropus era de 320–380 cm cúbicos. Ambos existiam há mais de 6 milhões de anos. Os hominídeos da época habitavam a África subsariana, a Etiópia e Tanzânia, ou seja na África Oriental. Seguiram-se a esses primeiros hominídeos os Ardipithecus e mais tarde (há 4,3 milhões de anos até há 2,4 milhões) os Australopithecus, descendentes dos Ardipithecus. Tinham\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive/')"
      ],
      "metadata": {
        "id": "1S7VvUXGBIFq",
        "outputId": "5ae98574-dc72-4489-8f76-bc6b6d5311d5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive/\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "from langchain.document_loaders import TextLoader\n",
        "\n",
        "# Caminho da pasta no Google Drive onde estão os arquivos\n",
        "caminho_da_pasta = '/content/drive/MyDrive/deep/docs'\n",
        "\n",
        "# Lista para armazenar os documentos\n",
        "documents_list = []\n",
        "\n",
        "# Percorrer os diretórios e carregar os arquivos\n",
        "for root, dirs, files in os.walk(caminho_da_pasta):\n",
        "    for nome_arquivo in files:\n",
        "        if nome_arquivo.endswith('.txt'):  # Verificar se o arquivo é um arquivo de texto\n",
        "            caminho_completo = os.path.join(root, nome_arquivo)\n",
        "            print(f'caminho = {caminho_completo}')\n",
        "\n",
        "            try:\n",
        "                loader = TextLoader(caminho_completo, autodetect_encoding=True)\n",
        "                documents = loader.load()\n",
        "\n",
        "                # Adicionar o documento à lista de documentos\n",
        "                documents_list.extend(documents)\n",
        "            except Exception as e:\n",
        "                print(f\"Erro ao carregar o conteúdo do arquivo {nome_arquivo}: {e}\")\n",
        "\n",
        "# Agora, documents_list contém todos os documentos carregados\n"
      ],
      "metadata": {
        "id": "RSrWlK0EjVCn",
        "outputId": "92221a55-b578-484a-dcc1-f26aae643dd6",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "caminho = /content/drive/MyDrive/deep/docs/codigos/tributario.txt\n",
            "caminho = /content/drive/MyDrive/deep/docs/codigos/civil.txt\n",
            "caminho = /content/drive/MyDrive/deep/docs/codigos/eleitoral.txt\n",
            "caminho = /content/drive/MyDrive/deep/docs/codigos/florestal.txt\n",
            "caminho = /content/drive/MyDrive/deep/docs/codigos/consumidor.txt\n",
            "caminho = /content/drive/MyDrive/deep/docs/estatutos/estatuto da crianca e do adolescente.txt\n",
            "caminho = /content/drive/MyDrive/deep/docs/estatutos/estatuto do idoso.txt\n",
            "caminho = /content/drive/MyDrive/deep/docs/estatutos/estatuto da juventude.txt\n",
            "caminho = /content/drive/MyDrive/deep/docs/estatutos/estatuto da igualdade racial.txt\n",
            "caminho = /content/drive/MyDrive/deep/docs/estatutos/estatuto da cidade.txt\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "É preciso quebrar a base de informação em documentos menores que possam fornecer contexto para o LLM ao responder perguntas"
      ],
      "metadata": {
        "id": "vHNFTAvvjhQ0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain.text_splitter import CharacterTextSplitter\n",
        "\n",
        "#Chunks de 500 palavras\n",
        "text_splitter = CharacterTextSplitter(chunk_size=500)\n",
        "chunks = text_splitter.split_documents(documents_list)\n"
      ],
      "metadata": {
        "id": "yN7r_ooJjgVk",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "25199694-c2d6-4147-8950-a48b442de7f5"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:langchain_text_splitters.base:Created a chunk of size 570, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 550, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 506, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 612, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 563, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 576, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 579, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 503, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 526, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 550, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 632, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 640, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 513, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 504, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 523, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 522, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 555, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 512, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 539, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 627, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 666, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 506, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 575, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 510, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 502, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 533, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 779, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 648, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 602, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 599, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 556, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 504, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 502, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 598, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 551, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 517, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 517, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 527, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 583, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 520, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 554, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 620, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 504, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 608, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 567, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 562, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 515, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 534, which is longer than the specified 500\n",
            "WARNING:langchain_text_splitters.base:Created a chunk of size 798, which is longer than the specified 500\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "chunks[0:20]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zthnLqiMjrc8",
        "outputId": "a0064476-bc8b-4fce-a5d5-26c6cead19fa"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[Document(page_content='LEI Nº 5.172, DE 25 DE OUTUBRO DE 1966.\\n\\nTexto compilado\\nDenominado Código Tributário Nacional\\nVigência\\n\\n(Vide Decreto-lei nº 82, de 1966)\\n(Vide Decreto nº 6.306, de 2007)\\n\\nDispõe sobre o Sistema Tributário Nacional e institui normas gerais de direito tributário aplicáveis à União, Estados e Municípios.\\n\\nO PRESIDENTE DA REPÚBLICA Faço saber que o Congresso Nacional decreta e eu sanciono a seguinte lei:\\n\\nDISPOSIÇÃO PRELIMINAR', metadata={'source': '/content/drive/MyDrive/deep/docs/codigos/tributario.txt'}),\n",
              " Document(page_content='DISPOSIÇÃO PRELIMINAR\\n\\n Art. 1º Esta Lei regula, com fundamento na Emenda Constitucional nº 18, de 1º de dezembro de 1965, o sistema tributário nacional e estabelece, com fundamento no artigo 5º, inciso XV, alínea b, da Constituição Federal, as normas gerais de direito tributário aplicáveis à União, aos Estados, ao Distrito Federal e aos Municípios, sem prejuízo da respectiva legislação complementar, supletiva ou regulamentar.\\n\\nLIVRO PRIMEIRO\\n\\nSISTEMA TRIBUTÁRIO NACIONAL\\n\\nTÍTULO I', metadata={'source': '/content/drive/MyDrive/deep/docs/codigos/tributario.txt'}),\n",
              " Document(page_content='LIVRO PRIMEIRO\\n\\nSISTEMA TRIBUTÁRIO NACIONAL\\n\\nTÍTULO I\\n\\nDisposições Gerais\\n\\n Art. 2º O sistema tributário nacional é regido pelo disposto na Emenda Constitucional nº 18, de 1º de dezembro de 1965, em leis complementares, em resoluções do Senado Federal e, nos limites das respectivas competências, em leis federais, nas Constituições e em leis estaduais, e em leis municipais.', metadata={'source': '/content/drive/MyDrive/deep/docs/codigos/tributario.txt'})]"
            ]
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(len(chunks))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oL79FcVDpli3",
        "outputId": "754db584-2335-46c2-b58c-5ba42eee546e"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4927\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Vamos usar o Weaviate como o Vector Database\n",
        "\n",
        "A ideia é criar os embeddings dos chunks e manter isso em uma base onde possa ser feita a busca por similaridade dos embeddings"
      ],
      "metadata": {
        "id": "_6PQu-_9UQuo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain.embeddings import OpenAIEmbeddings\n",
        "from langchain.vectorstores import Weaviate\n",
        "import weaviate\n",
        "from weaviate.embedded import EmbeddedOptions\n",
        "\n",
        "client = weaviate.Client(\n",
        "  embedded_options = EmbeddedOptions()\n",
        ")\n",
        "\n",
        "vectorstore = Weaviate.from_documents(\n",
        "    client = client,\n",
        "    documents = chunks,\n",
        "    embedding = OpenAIEmbeddings(model=\"text-embedding-3-small\", openai_api_key=openai_api_key),  #text-embedding-3-small usado para criar os embeddings\n",
        "    by_text = False\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cspolFn0jyJ1",
        "outputId": "a425cbed-0681-49e6-a9ab-6837622e4d61"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "embedded weaviate is already listening on port 8079\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "retriever = vectorstore.as_retriever()"
      ],
      "metadata": {
        "id": "-ZhLIoBXkJW2"
      },
      "execution_count": 33,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Langchain permite criar templates de prompts para serem usados de forma recorrente\n",
        "\n",
        "Aqui o template dá o contexto da tarefa a ser realizada (responder perguntas), define a pergunta e contexto textual e pede pela resposta."
      ],
      "metadata": {
        "id": "c4b0EMfcU7Xc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain.prompts import ChatPromptTemplate\n",
        "\n",
        "template = \"\"\"Você é um assistente que irá responder retornando artigos e leis que podem ser aplicados no contexto fornecido.\n",
        "Sempre especifique o nome da lei ou do estatuto em que os artigos se encontram.\n",
        "Forneça explicação geral dos artigos e leis, considerando o contexto.\n",
        "Não invente.\n",
        "Use as seguintes peças de texto para responder a pergunta.\n",
        "Se não souber a resposta, apenas responda que não sabe a resposta.\n",
        "Use no máximo sete sentenças e mantenha a resposta concisa.\n",
        "Pergunta: {question}\n",
        "Contexto: {context}\n",
        "Resposta:/\n",
        "\"\"\"\n",
        "prompt = ChatPromptTemplate.from_template(template)\n",
        "\n",
        "print(prompt)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jx-gi7-0opqG",
        "outputId": "4d087d8a-39f6-4b85-b28a-9f218730d50a"
      },
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "input_variables=['context', 'question'] messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['context', 'question'], template='Você é um assistente que irá responder retornando artigos e leis que podem ser aplicados no contexto fornecido.\\nSempre especifique o nome da lei ou do estatuto em que os artigos se encontram.\\nForneça explicação geral dos artigos e leis, considerando o contexto.\\nNão invente.\\nUse as seguintes peças de texto para responder a pergunta.\\nSe não souber a resposta, apenas responda que não sabe a resposta.\\nUse no máximo sete sentenças e mantenha a resposta concisa.\\nPergunta: {question}\\nContexto: {context}\\nResposta:/\\n'))]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Aqui é criada uma chain onde o Langchain vai sempre executar o pipeline completo\n",
        "\n",
        "recebe pergunta -> retriver busca por contexto -> constrói prompt a partir do template -> llm -> Parser para resposta"
      ],
      "metadata": {
        "id": "832Uo00TVTLo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_openai import ChatOpenAI\n",
        "from langchain.schema.runnable import RunnablePassthrough\n",
        "from langchain.schema.output_parser import StrOutputParser\n",
        "\n",
        "llm = ChatOpenAI(model_name=\"gpt-3.5-turbo\", temperature=0.0, openai_api_key=openai_api_key)\n",
        "\n",
        "rag_chain = (\n",
        "    {\"context\": retriever,  \"question\": RunnablePassthrough()}\n",
        "    | prompt\n",
        "    | llm\n",
        "    | StrOutputParser()\n",
        ")\n",
        "\n",
        "def gerar_resposta(query):\n",
        "#  query = \"Contexto: Uma criança estava sofrendo maus tratos dos pais, quais artigos eu poderia utilizar para defender a criança?\"\n",
        "  return rag_chain.invoke(query)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 87
        },
        "id": "O7os9eSqlXgl",
        "outputId": "e2f46beb-246f-47d7-90cf-fb07abb8a907"
      },
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Os artigos que podem ser utilizados para defender a criança que está sofrendo maus tratos dos pais são o artigo 130 e o artigo 18-A do Estatuto da Criança e do Adolescente. O artigo 130 prevê a possibilidade de afastamento do agressor da moradia comum em casos de maus-tratos, opressão ou abuso sexual. Já o artigo 18-A estabelece o direito da criança e do adolescente de serem educados sem o uso de castigo físico ou tratamento cruel. Ambos os artigos visam proteger a integridade física e emocional da criança em situações de violência.'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 58
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "T8sSDi9Aps3P"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}