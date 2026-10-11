---
title: "transformers下载模型"
description: "公开模型下载（bert-base-chinese）最好的下载方法1）下载代码2）下载模型，以 bert-base-chinese 库为例 https://huggingface.co/bert-base-chinese/tree/main"
date: "2026-10-11"
category: "NLP与大模型"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\大模型\\ku_export\\transformers下载模型\\transformers下载模型.md"
---
# transformers下载模型
最新更新：

公开模型下载（bert-base-chinese）最好的下载方法1）下载代码2）下载模型，以 bert-base-chinese 库为例 https://huggingface.co/bert-base-chinese/tree/main

GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/bert-base-chinese  # GIT_LFS_SKIP_SMUDGE=1表示跳过lfs模型大文件 不加LFS_SKIP的话模型太大就会断掉sudo wget https://huggingface.co/bert-base-chinese/resolve/main/pytorch_model.bin  # 再单独下载每个lfs文件(一个个下载lfs，注意是每个lfs文件嗷) 虽然慢但是稳稳地注意：*.h5和*.msgpack是tensorflow框架和flax框架产出的模型权重，pytorch只要*.bin文件。这里的模型下载地址只是把模型地址https://huggingface.co/bert-base-chinese/blob/main/pytorch_model.bin 的blob换成resolve非公开模型下载（Llama-2-7b-hf）先申请，等待通过后模型页面能看到具体的文件列表，看不到的话就先申请一下

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=20edb21a0cb74a9c8921b0e4341b8f11&docGuid=Bw1OeIvG15q4YL)

name、pw为huggingface自己的账户密码，比如我的是Jie19

GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/meta-llama/Llama-2-7b-hf  # GIT_LFS_SKIP_SMUDGE=1表示跳过lfs模型大文件，注：这里需要输入账号密码 不加LFS_SKIP的话模型太大就会断掉sudo wget https://name:pw@huggingface.co/meta-llama/Llama-2-7b-hf/resolve/main/pytorch_model-00001-of-00002.bin  # 再单独下载每个lfs文件(一个个下载lfs，注意是每个lfs文件嗷) 虽然慢但是稳稳地注意：*.h5、*.msgpack是tensorflow框架和flax框架产出的模型权重，pytorch只要*.bin文件。这里的模型下载地址只是把模型地址https://huggingface.co/meta-llama/Llama-2-7b-hf/blob/main/pytorch_model-00001-of-00002.bin 的blob换成resolve![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9a5e9e671fb149cca3d1c05622e6c593&docGuid=Bw1OeIvG15q4YL)

最新更新20230814![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d76e727b1ee64fdfacaa894b8dcf465c&docGuid=Bw1OeIvG15q4YL)

新建一个可用token

wget --header="Authorization: Bearer token" https://huggingface.co/meta-llama/Llama-2-7b-hf/resolve/main/model-00001-of-00002.safetensors![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4dd45655da63429ab5331b4a79123b39&docGuid=Bw1OeIvG15q4YL)

下面不用再看了。。。。都是弟弟😓一、模型缓存地址配置1、默认下载地址 ~/.cache/huggingface/hubmac transformers的预训练模型下载到本地特定位置，默认是在~/.cache/huggingface/hub

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=be6072aef7194b95886647ae7ba1b865&docGuid=Bw1OeIvG15q4YL)

2、修改下载地址两种方式：

1）修改环境变量 HF_HOME2）使用时指定下载地址 cache_dirAutoModel.from_pretrained('bert-base-chinese', cache_dir='./')比较建议在工程下面新建一个文件夹专门放模型文件，推荐用二里的脚本手动下载

二、优雅的下载huggingface-transformers模型三种方式：

Git LFS 模型下载方案（优雅，但不够灵活，全部下载，若有pytorch、tf多个版本模型会全部下载太大了。。）Hugging Face Hub 模型下载方案（优雅，强烈推荐， 可选择部分下载，如可过滤tf版本的模型）自行实现的模型下载方案（历史版本，自以为的优雅中透露着没好好看文档的尴尬，直接用地址下载）最推荐Hugging Face Hub 模型下载方案，该方案原文：https://huggingface.co/docs/huggingface_hub/v0.13.3/guides/download

Git LFS 模型下载方案以下载THUDM/chatglm-6b为例

1、安装：

2、下载：点击右上角有一个Use in Transformers的按钮，按照弹出的指令下载

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0fa5bced80cb4a49a87c2aa5ce273bf8&docGuid=Bw1OeIvG15q4YL)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a92aac586a0642d0a6b4af7a98351cf8&docGuid=Bw1OeIvG15q4YL)

git clone https://huggingface.co/THUDM/chatglm-6b执行后模型会下载所有文件到当前文件夹。

这种方案也存在着一定的问题，即会下载仓库中的所有文件，会大大延长模型下载的时间。

Hugging Face Hub 模型下载方案(强烈推荐)如果想实现模型精确下载，可以借助Hugging Face Hub，以 bert-base-uncased 为例

1、安装

pip install huggingface_hub2、下载

在snaphot_download方法中，提供了allow_patterns和ignore_patterns两个参数，简单来说前者是对指定的匹配项进行下载，后者是忽略指定的匹配项，下载其余部分。

在目录中包含着flax_model.msgpack、tf_model.h5和pytorch_model.bin三个不同框架模型文件，在bert-base-uncased的版本中，还存在着rust版本的rust_model.ot模型，如果我们只想要pytorch版本的模型文件：

from huggingface_hub import snapshot_download# 第一种：库下载 全部下载 与Git LFS下载的内容是一样的# snapshot_download(repo_id="bert-base-chinese")  # 第二种：库下载 过滤下载snapshot_download(repo_id="distilbert-base-uncased", ignore_patterns=["*.h5", "*.ot", "*.msgpack"], cache_dir='./models/')# from huggingface_hub import hf_hub_download# 第三种：单文件下载# hf_hub_download(repo_id="lysandre/arxiv-nlp", filename="config.json")# '/root/.cache/huggingface/hub/models--lysandre--arxiv-nlp/snapshots/894a9adde21d9a3e3843e6d5aeaaf01875c7fade/config.json'# hf_hub_download(repo_id="google/fleurs", filename="fleurs.py", repo_type="dataset")# '/root/.cache/huggingface/hub/datasets--google--fleurs/snapshots/199e4ae37915137c555b1765c01477c216287d34/fleurs.py'# hf_hub_download(repo_id="lllyasviel/ControlNet",subfolder="models",filename="control_sd15_canny.pth", local_dir=".") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=590f4e6d656e4ec89f250f68afaf504e&docGuid=Bw1OeIvG15q4YL)

https://huggingface.co/docs/huggingface_hub/main/en/package_reference/file_download

自行实现下载方案以 bert-base-uncased 为例，只想要vocab.txt、config.json、pytorch_model.bin文件

import osimport sysimport jsonimport requestsfrom uuid import uuid4from tqdm import tqdmdef main(model_id, path='./', VOCAB_FILE="vocab.txt", CONFIG_FILE="config.json", MODEL_FILE="pytorch_model.bin",         ADD_FILES=None):    SESSIONID = uuid4().hex    BASE_URL = "https://huggingface.co/{}/resolve/main/{}"    headers = {'user-agent': 'transformers/4.8.2; python/3.8.5;  \                session_id/{}; torch/1.9.0; tensorflow/2.5.0; \                file_type/model; framework/pytorch; from_auto_class/False'.format(SESSIONID)}    # 创建模型对应的文件夹    model_dir = model_id.replace("/", "-")    model_dir = path + '/' + model_dir    if not os.path.exists(model_dir):        os.mkdir(model_dir)    else:        print('%s has exist' % model_dir)        return    # vocab 和 config 文件可以直接下载    r = requests.get(BASE_URL.format(model_id, VOCAB_FILE), headers=headers)    r.encoding = "utf-8"    with open(os.path.join(model_dir, VOCAB_FILE), "w", encoding="utf-8") as f:        if VOCAB_FILE[-4:] == 'json':            json.dump(r.json(), f, indent="\t")        else:            f.write(r.text)        print("{}词典文件{}下载完毕!".format(model_id, VOCAB_FILE))    r = requests.get(BASE_URL.format(model_id, CONFIG_FILE), headers=headers)    r.encoding = "utf-8"    with open(os.path.join(model_dir, CONFIG_FILE), "w", encoding="utf-8") as f:        json.dump(r.json(), f, indent="\t")        print("{}配置文件{}下载完毕!".format(model_id, CONFIG_FILE))    if ADD_FILES is not None:        download_files = ADD_FILES.split(',')        for file in download_files:            r = requests.get(BASE_URL.format(model_id, file), headers=headers)            r.encoding = "utf-8"            with open(os.path.join(model_dir, file), "w", encoding="utf-8") as f:                if file[-4:] == 'json':                    json.dump(r.json(), f, indent="\t")                else:                    f.write(r.text)                print("文件{}下载完毕!".format(file))    # 模型文件需要分两步进行    # Step1 获取模型下载的真实地址    r = requests.head(BASE_URL.format(model_id, MODEL_FILE), headers=headers)    r.raise_for_status()    url_to_download = None    if 300 <= r.status_code <= 399:        url_to_download = r.headers["Location"]    else:        exit(0)    # Step2 请求真实地址下载模型    r = requests.get(url_to_download, stream=True, proxies=None, headers=None)    r.raise_for_status()    # 这里的进度条是可选项，直接使用了transformers包中的代码    content_length = r.headers.get("Content-Length")    total = int(content_length) if content_length is not None else None    progress = tqdm(        unit="B",        unit_scale=True,        total=total,        initial=0,        desc="Downloading Model",    )    with open(os.path.join(model_dir, MODEL_FILE), "wb") as temp_file:        for chunk in r.iter_content(chunk_size=1024):            if chunk:  # filter out keep-alive new chunks                progress.update(len(chunk))                temp_file.write(chunk)    progress.close()    print("{}模型文件下载完毕!".format(model_id))def load_one_file(model_id, path, MODEL_FILE):    SESSIONID = uuid4().hex    BASE_URL = "https://huggingface.co/{}/resolve/main/{}"    headers = {'user-agent': 'transformers/4.8.2; python/3.8.5;  \                session_id/{}; torch/1.9.0; tensorflow/2.5.0; \                file_type/model; framework/pytorch; from_auto_class/False'.format(SESSIONID)}    # 模型文件需要分两步进行    # Step1 获取模型下载的真实地址    r = requests.head(BASE_URL.format(model_id, MODEL_FILE), headers=headers)    r.raise_for_status()    url_to_download = None    if 300 <= r.status_code <= 399:        url_to_download = r.headers["Location"]    else:        exit(0)    # Step2 请求真实地址下载模型    r = requests.get(url_to_download, stream=True, proxies=None, headers=None)    r.raise_for_status()    # 这里的进度条是可选项，直接使用了transformers包中的代码    content_length = r.headers.get("Content-Length")    total = int(content_length) if content_length is not None else None    progress = tqdm(        unit="B",        unit_scale=True,        total=total,        initial=0,        desc="Downloading Model",    )    with open(os.path.join(path, MODEL_FILE), "wb") as temp_file:        for chunk in r.iter_content(chunk_size=1024):            if chunk:  # filter out keep-alive new chunks                progress.update(len(chunk))                temp_file.write(chunk)    progress.close()    print("{}模型文件下载完毕!".format(MODEL_FILE))if __name__ == "__main__":    # model_id = "bert-base-chinese"    # main(model_id, path='./transformer_file')        # model_id = "microsoft/codebert-base"    # main(model_id, path='./transformer_file', VOCAB_FILE='vocab.json',    #      ADD_FILES='merges.txt,special_tokens_map.json,tokenizer_config.json,README.md')    # load_one_file('THUDM/chatglm-6b', './model/', 'pytorch_model-00005-of-00008.bin')        model_id = sys.argv[1]    path = sys.argv[2]    MODEL_FILE = sys.argv[3]    load_one_file(model_id, path, MODEL_FILE)![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=47e485a85af24db184692ceb9fe6ecc7&docGuid=Bw1OeIvG15q4YL)

三、一些经典模型![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b2ee5d6eaea24a73a67913d5a535039d&docGuid=Bw1OeIvG15q4YL)

四、模型下载报错1、Explicitly passing a `revision` is encouraged when loading a model with cust~/.cache/huggingface/hub/models--THUDM--chatglm-6b/snapshots![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=37e743f2c9214bd0a45549e7dbbb9ee8&docGuid=Bw1OeIvG15q4YL)

看下上次是哪个版本下一半了，指定revision

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4ee0a6ea9bbe47e0a34404dcb1b72e9e&docGuid=Bw1OeIvG15q4YL)

2、requests.exceptions.ConnectionError：(‘Connection aborted。’，ConnectionResetError(104用上面的脚本单独下载大文件吧

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=02a09827dfbe4b819fb0195ca4dae2c5&docGuid=Bw1OeIvG15q4YL)



