# Aleph Alpha Integration

[![awesome plugin](https://custom-icon-badges.demolab.com/static/v1?label=&message=awesome+plugin&color=383938&style=for-the-badge&logo=cheshire_cat_ai)](https://)  

This plugin allows you to use [Aleph Alpha embeddings](https://docs.aleph-alpha.com/docs/tasks/semantic_embed/) in Cheshire Cat.
To use it, you must have an [API Key Aleph Alpha](https://docs.aleph-alpha.com/docs/account/).

## Parameters

* aleph_alpha_api_key: API key for Aleph Alpha API.
* compress_to_size: Should the returned embeddings come back as an original 5120-dim vector, or should it be compressed to 128-dim.
* model_name: Model name to use.
* normalize: Should returned embeddings be normalized.

### Aleph Alpha’s asymmetric semantic embedding.

AA provides you with an endpoint to embed a document and a query. The models were optimized to make the embeddings of documents and the query for a document as similar as possible.

### Aleph Alpha’s symmetric semantic embedding.

Symmetric version of the Aleph Alpha’s semantic embeddings.

The main difference is that here, both the documents and queries are embedded with a SemanticRepresentation.Symmetric