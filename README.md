# LLM simple QnA example

[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This repository contains the example of the simple `QnA` system based on the
`LLM` and `LangChain`. As the vector search engine I have used `Qdrant`.

## Setup python environment

> [!NOTE]\
> This project is based on `Python 3.10` and uses `poetry` to manage dependencies.

1. Clone the repository using `git clone` command.
2. Open the terminal and go to the project directory using `cd` command.
3. Create virtual environment using `python -m venv venv` or
   `conda create -n venv python=3.10` command. We have used `Python 3.10` during
   development.
4. Activate virtual environment using `source venv/bin/activate` or
   `conda activate venv` command.
5. Install poetry using instructions from
   [here](https://python-poetry.org/docs/#installation). Use
   `with the official installer` section.
6. Set the following option to disable new virtualenv creation:
   ```bash
   poetry config virtualenvs.create false
   ```
7. Install dependencies using `poetry install --no-root` command. The
   `--no-root` flag is needed to avoid installing the package itself.
8. Setup `pre-commit` hooks using `pre-commit install` command. More information
   about `pre-commit` you can find [here](https://pre-commit.com/).
9. Run the test to check the correctness of the project work using following
   command:
   ```bash
   python -m unittest -b
   ```
10. After successful passing of the tests, you can work with the project!
11. If you want to add new dependencies, use `poetry add <package_name>`
    command. More information about `poetry` you can find
    [here](https://python-poetry.org/docs/basic-usage/).
12. If you want to add new tests, use `unittest` library. More information about
    `unittest` you can find
    [here](https://docs.python.org/3/library/unittest.html). All tests should be
    placed in the `tests` directory.
13. All commits should be checked by `pre-commit` hooks. If you want to skip
    this check, use `git commit --no-verify` command. But it is not recommended
    to do this.
14. Also, you can run `pre-commit` hooks manually using
    `pre-commit run --all-files` command.
15. More useful commands you can find in `Makefile`.

## Examples

> [!WARNING]\
> You should have `wget` to files and `docker` to run `Qdrant` and `Redis` services.

### How to start?

> [!IMPORTANT]\
> Knowledge base for `RAG` consists of two parts: `pdf files` and data from the `wikipedia`.
> First part will be downloaded manually by the script and second part will be downloaded
> from the code.

1. Run `make download_dataset` command to download the `pdf files`. Those files
   will be placed in the `data` directory and it only a one part of the full
   dataset that will be used.
2. Run `make run_qdrant` command to start the `Qdrant` service. It will be
   available on `http://localhost:6333` address.
3. Run `make run_redis` command to start the `Redis` service. It will be
   necessary to cache the `LLM` prompts and requests in `step 5`.
4. Run the notebook `notebooks/01-open-source-llms-langchain.ipynb` to download
   the full dataset, index it and run the `QnA` example with local `LLMs`. This
   notebook show only simple example of the `QnA` system.
5. Run the notebook `notebooks/02-open-ai-langchain-base.ipynb` to download the
   full dataset, index it and run the `QnA` example with `OpenAI LLMs`. This
   example is more complex and show how to evaluate the `QnA` system.
6. I can run `REST API` for `QnA` system using `make run_api` command. `Swagger`
   will be available on `http://localhost:8000/docs` address.

## Useful links

- [Mastering RAG: How To Architect An Enterprise RAG System](https://www.rungalileo.io/blog/mastering-rag-how-to-architect-an-enterprise-rag-system) -
  this article describes how to build the `RAG` system for enterprise and
  `7 Failure Points` of `RAG` systems.
- [Using langchain for Question Answering on Own Data](https://medium.com/@onkarmishra/using-langchain-for-question-answering-on-own-data-3af0a82789ed) -
  good introduction into the `LangChain` and `QnA` systems. Contains a lot of
  useful diagrams.
- [RAG: How to Talk to Your Data](https://towardsdatascience.com/rag-how-to-talk-to-your-data-eaf5469b83b0) -
  yet another good introduction into the `RAG` systems with useful examples.
- [HOW-TO: Build a ChatPDF App over millions of documents with LangChain and MyScale in 30 Minutes](https://github.com/myscale/ChatData/blob/main/docs/self-query.md) -
  just a quick example of how to build a `QnA` system using `LangChain`.
- [How LangChain Implements Self Querying](https://zilliz.com/blog/How-LangChain-Implements-Self-Querying) -
  into the details of how `LangChain` implements `self-querying`.
- [SPLADE: sparse neural search](https://github.com/naver/splade) - `SPLADE` is
  a sparse neural network for efficient vector search.
- [Weaviate Hybrid Search](https://python.langchain.com/docs/integrations/retrievers/weaviate-hybrid) -
  just a quick example hybrid search using `LangChain` and `Weaviate`.
- [Qdrant Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid.html) -
  just a quick example hybrid search using `LlamaIndex` and `Qdrant`.
- [Building an Ecommerce-Based Search Application Using Langchain and Qdrant’s Latest Pure Vector-Based Hybrid Search](https://nayakpplaban.medium.com/building-an-ecommerce-based-search-application-using-langchain-and-qdrants-latest-pure-a60df053066a) -
  yet another example of the `LangChain` and `Qdrant` hybrid search using
  `SPLADE`.
- [Azure OpenAI demos](https://github.com/retkowsky/Azure-OpenAI-demos/tree/main) -
  Azure OpenAI demos repository.
- [A complete Guide to LlamaIndex in 2024](https://nanonets.com/blog/llamaindex/) -
  `LlamaIndex` blog post.
- [Building LLM-based Application Using Langchain and OpenAI](https://www.linkedin.com/pulse/building-llm-based-application-using-langchain-openai-rodion-salnik/) -
  good text explanation of the `LangChain` and `OpenAI` integration.
- [LOTR (Merger Retriever) in LangChain](https://python.langchain.com/docs/integrations/retrievers/merger_retriever) -
  `Merger Retriever` is a `LangChain` retriever that merges results from
  multiple retrievers.
- [What is the difference between LOTR(Merger Retriever) and Ensemble Retriever](https://github.com/langchain-ai/langchain/issues/8677) -
  `LOTR` vs `Ensemble Retriever` issue.
- [TruLens](https://python.langchain.com/docs/integrations/providers/trulens) -
  `TruLens` is an open-source package that provides instrumentation and
  evaluation tools for `LLM` based applications.
- [Better RAG with Merger Retriever (LOTR) and Re-ranking Retriever (Long Context Reorder)](https://www.youtube.com/watch?v=uYZftCq2efg&ab_channel=AIAnytime)
- [Long-Context Reorder](https://python.langchain.com/docs/modules/data_connection/retrievers/long_context_reorder) -
  `LongContextReorder` is a retriever that re-ranks the results of another
  retriever.
- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) -
  `LLMs` and `long contexts` article.
- [MultiVector Retriever](https://python.langchain.com/docs/modules/data_connection/retrievers/multi_vector) -
  `MultiVectorRetriever` is a retriever that uses multiple vector stores to
  retrieve results.
- [Harnessing Retrieval Augmented Generation With Langchain](https://betterprogramming.pub/harnessing-retrieval-augmented-generation-with-langchain-2eae65926e82) -
  `RAG` with `LangChain` article. Contains example with good and simple chat
  application.
- [LangChain Interface methods](https://python.langchain.com/docs/expression_language/interface) -
  `LangChain` interface methods. How to stream the output, how to asynchronously
  run the query, etc.
- [Save time and money by caching OpenAI (and other LLM) API calls with Langchain](https://mikulskibartosz.name/cache-open-ai-calls-with-langchain) -
  `LLM` caching in `LangChain`.
- [LLM Caching integrations](https://python.langchain.com/docs/integrations/llms/llm_caching) -
  `LLM` caching in `LangChain`.
- [LLM Caching](https://python.langchain.com/docs/modules/model_io/llms/llm_caching) -
  `LLM` caching in `LangChain`.
- [Multi-Vector Retriever for RAG on tables, text, and images](https://blog.langchain.dev/semi-structured-multi-modal-rag/) -
  `Multi-Vector Retriever` for `RAG` on tables, text, and images.
- [LangChain Spark AI](https://github.com/sugarforever/LangChain-Tutorials/blob/main/LangChain_Spark_AI.ipynb) -
  `LangChain` and `Spark` integration.
- [Large Language Model for Table Processing: A Survey](https://arxiv.org/abs/2402.05121) -
  `LLM` for table processing survey.
- [Self-reflective RAG with LangGraph: Self-RAG and CRAG](https://www.youtube.com/watch?v=pbAd8O1Lvm4) -
  `Self-RAG` and `CRAG` with `LangGraph`.
- [Webinar "A Whirlwind Tour of ML Model Serving Strategies (Including LLMs)"](https://www.youtube.com/watch?v=VUsm0qO2ifg&ab_channel=DataPhoenixEvents)
- [Prompt-Engineering for Open-Source LLMs](https://www.youtube.com/watch?v=f32dc5M2Mn0&ab_channel=DeepLearningAI)
- [Mitigating LLM Hallucinations with a Metrics-First Evaluation Framework](https://www.youtube.com/watch?v=u1pNrsR1txA&ab_channel=DeepLearningAI)
- [Efficient Fine-Tuning for Llama-v2-7b on a Single GPU](https://www.youtube.com/watch?v=g68qlo9Izf0&ab_channel=DeepLearningAI)

## Courses

- [DeepLearning AI courses](https://learn.deeplearning.ai/) - that's a good
  courses to start with
- [Text book](https://aman.ai/primers/ai/) - articles on AI
  fundamentals/concepts
- [LLM Course](https://github.com/mlabonne/llm-course) - course with roadmaps
  and Colab notebooks.
- [Building LLM-Powered Apps](https://www.wandb.courses/courses/building-llm-powered-apps) -
  W&B course about `LLMs`.
- [Training and Fine-tuning Large Language Models (LLMs)](https://www.wandb.courses/courses/training-fine-tuning-LLMs) -
  W&B course about `LLMs`.
- [Large Language Models (LLMs): Foundation Models from the Ground Up](https://customer-academy.databricks.com/learn/course/internal/view/elearning/1804/large-language-models-llms-foundation-models-from-the-ground-up) -
  Databricks course about `LLMs`.
- [Large Language Models (LLMs): Application through Production](https://customer-academy.databricks.com/learn/course/internal/view/elearning/1749/large-language-models-llms-application-through-production) -
  Databricks course about `LLMs`.
- [Як створити спеціалізований чатбот. Детальний гайд на основі кейса клієнта](https://dou.ua/forums/topic/46902/?from=tg&utm_source=telegram&utm_medium=social) -
  article about `chatbots` in `Ukrainian`.
