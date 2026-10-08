#!/bin/bash

count=0
batch=1

mkdir -p batch_001

find . -type f -name "*.md" | while read file
do

    # 跳过已经提交的文件
    if git log --all --name-only --pretty=format: | grep -qx "$file"; then
        echo "跳过已提交: $file"
        continue
    fi

    # 每50个换批次
    if [ $count -ge 50 ]; then
        batch=$((batch+1))
        count=0
        mkdir -p batch_$(printf "%03d" $batch)
    fi


    name=$(basename "$file" .md)

    cp "$file" batch_$(printf "%03d" $batch)/

    git add .

    git commit -m "$name"

    count=$((count+1))

done

git push
