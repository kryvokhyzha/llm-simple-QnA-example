poetry_install_deps:
	poetry install --no-root
poetry_install_deps_compile:
	poetry install --no-root --compile --no-cache
poetry_get_lock:
	poetry lock
poetry_update_deps:
	poetry update
poetry_update_self:
	poetry self update
poetry_show_deps:
	poetry show
poetry_show_deps_tree:
	poetry show --tree
poetry_build:
	poetry build

pre_commit_install: .pre-commit-config.yaml
	pre-commit install
pre_commit_run: .pre-commit-config.yaml
	pre-commit run --all-files
pre_commit_rm_hooks:
	pre-commit --uninstall-hooks

nvsmi0:
	watch -n 0.1 nvidia-smi -i 0

run_qdrant:
	docker run --rm --name qdrant-docker -d -p 6333:6333 \
    -v /tmp/qdrant_storage:/qdrant/storage \
    qdrant/qdrant:latest
run_qdrant_rm:
	docker stop qdrant-docker; \
	rm -rf /tmp/qdrant_storage; \
	make run_qdrant
run_redis:
	docker run --rm --name redis-docker -d -p 6379:6379 \
	-v /tmp/redis_storage:/data \
	redis/redis-stack-server:latest
run_redis_rm:
	docker stop redis-docker; \
	rm -rf /tmp/redis_storage; \
	make run_redis

download_dataset:
	mkdir -p data/my_documents && \
	cd data && \
	wget https://cs229.stanford.edu/notes2020spring/cs229-notes1.pdf && \
	wget https://cs229.stanford.edu/section/cs229-linalg.pdf && \
	wget https://cs229.stanford.edu/notes2020spring/cs229-notes2.pdf && \
	wget https://cs229.stanford.edu/notes2019fall/cs229-notes3.pdf && \
	wget https://cs229.stanford.edu/notes2020spring/cs229-notes-deep_learning.pdf && \
	wget https://cs229.stanford.edu/notes2020spring/bias-variance-error-analysis.pdf && \
	wget https://sgp.fas.org/crs/misc/IF10244.pdf && \
	cd ..

quantize_openchat_gguf:
	chmod +x scripts/quantize_openchat_gguf.sh && scripts/quantize_openchat_gguf.sh

run_api:
	uvicorn src.api:app --host 0.0.0.0 --port 8000

run_app:
	streamlit run src/app.py
