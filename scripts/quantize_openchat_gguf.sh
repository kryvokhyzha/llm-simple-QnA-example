#!/bin/bash

# select quantization method:
# https://github.com/ggerganov/llama.cpp/discussions/406

# go to the weights folder
cd weights || exit

# clone repository with models
git lfs install
git clone https://huggingface.co/openchat/openchat_3.5

# clone llama.cpp and open it
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp || exit

# build quantization tool using `make` or `cmake`
make
# or using `cmake`, see: https://github.com/ggerganov/llama.cpp

## install python requirements
#pip install -r requirements.txt

# convert models to gguf format
python3 convert.py ../openchat_3.5/  --outfile openchat_3.5-f16.gguf

# run quantization to 5 bits
./quantize openchat_3.5-f16.gguf openchat_3.5-q5_K_M.gguf q5_K_M
