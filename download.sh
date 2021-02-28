#!/usr/bin/env bash
set -ef

# Download Talk of Norway data
mkdir -p ./data/raw/
wget http://ltr.uio.no/ton/ton.data.101.tgz -O ./data/raw/ton.tgz
tar -xzf ./data/raw/ton.tgz -C ./data/raw/
rm ./data/raw/ton.tgz
