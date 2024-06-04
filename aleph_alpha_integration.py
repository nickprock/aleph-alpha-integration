from typing import Type, List

from cat.mad_hatter.decorators import tool, hook, plugin
from cat.factory.embedder import EmbedderSettings
from langchain_community.embeddings import AlephAlphaAsymmetricSemanticEmbedding, AlephAlphaSymmetricSemanticEmbedding
from pydantic import ConfigDict


class AlephAlphaAsymmetricEmbedderConfig(EmbedderSettings):
    aleph_alpha_api_key: str
    compress_to_size: int = 128
    model_name: str='luminous-base'
    normalize: bool = True
    _pyclass: Type = AlephAlphaAsymmetricSemanticEmbedding

    model_config = ConfigDict(
        json_schema_extra = {
            "humanReadableName": "Aleph Alpha Asymmetric embedder",
            "description": "Aleph Alpha Asymmetric embedder",
            "link": "https://aleph-alpha.com/",
        }
    )

class AlephAlphaSymmetricEmbedderConfig(EmbedderSettings):
    aleph_alpha_api_key: str
    compress_to_size: int = 128
    model_name: str='luminous-base'
    normalize: bool = True
    _pyclass: Type = AlephAlphaSymmetricSemanticEmbedding

    model_config = ConfigDict(
        json_schema_extra = {
            "humanReadableName": "Aleph Alpha Symmetric embedder",
            "description": "Aleph Alpha Symmetric embedder",
            "link": "https://aleph-alpha.com/",
        }
    )


@hook
def factory_allowed_embedders(allowed, cat) -> List:
    allowed.append(AlephAlphaAsymmetricEmbedderConfig)
    allowed.append(AlephAlphaSymmetricEmbedderConfig)
    return allowed