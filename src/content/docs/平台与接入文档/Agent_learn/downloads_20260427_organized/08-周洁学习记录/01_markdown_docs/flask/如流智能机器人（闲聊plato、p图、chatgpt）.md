---
title: "url 校验"
description: "如流智能机器人（闲聊plato、p图、chatgpt）"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\flask\\如流智能机器人（闲聊plato、p图、chatgpt）.md"
---
如流智能机器人（闲聊plato、p图、chatgpt）

### 一、申请机器人
[https://qy.baidu.com/doc/index.html#/inner_serverapi/robot?id=添加机器人](https://qy.baidu.com/doc/index.html#/inner_serverapi/robot?id=添加机器人)

### 二、url 验证
python 3.7

安装库：

```
pip install flask
pip install pycryptodome
```
在开发机上运行 

python3 main.py

```
"""
智能机器人

"""
import base64
import json

from Crypto.Cipher import AES
from flask import Flask, request

app = Flask(__name__)


def base64_urlsafe_decode(s):
    """
    Base64URLSafe 解码
    """
    s = s.replace('-', '+').replace('_', '/') + '=' * (len(s) % 4)
    return base64.b64decode(s)


def AESdecrypt(msg):
    """
    AES解密

    加密算法：AES-128
    加密模式：ECB
    填充方式：PKCS5（PKCS7兼容）
    编码方式：Base64URLSafe（它不在末尾填充=号，并将标准Base64中的+和/分别改成了-和_）
    """
    EncodingAESKey = ''
    ciphertext = msg.decode('utf-8')
    cipher = AES.new(base64_urlsafe_decode(EncodingAESKey), AES.MODE_ECB)
    res = cipher.decrypt(base64_urlsafe_decode(ciphertext))
    return res[0:-res[-1]]


@app.route('/rob', methods=['POST'])
def get_data():
    try:
        echostr = request.form.get('echostr', None)
        if echostr:
            # url 校验
            return echostr
        else:
            # 获取 raw body
            msg_base64 = request.get_data()
            # 解密
            decrypted = AESdecrypt(msg_base64)
            msg_data = json.loads(decrypted)
            print('获取msg_data: %s' % msg_data)
            return 'ok'
    except:
        return 'fail'


if __name__ == '__main__':
    app.run(host='', port=8015) 

```
注：EncodingAESKey 、host、port 需改成自己的



填写回调地址为：http://{host}:{port}/rob，在如流点击保存，即可通过 url 验证。

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 三、闲聊服务 plato
##### 使用示例
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


#### 1、本地测试开放域对话模型
预训练模型加载很慢，需要一次加载多次处理对话。服务端socket_service.py保持运行，每次有新的对话任务运行socket_client.py，获取对话结果。

##### 服务端
```
import json
import socket

import paddle
from paddlenlp.transformers import (UnifiedTransformerLMHeadModel,
                                    UnifiedTransformerTokenizer)


def post_process_response(token_ids, tokenizer):
    """Post-process the decoded sequence. Truncate from the first <eos>."""
    eos_pos = len(token_ids)
    for i, tok_id in enumerate(token_ids):
        if tok_id == tokenizer.sep_token_id:
            eos_pos = i
            break
    token_ids = token_ids[:eos_pos]
    tokens = tokenizer.convert_ids_to_tokens(token_ids)
    tokens = tokenizer.merge_subword(tokens)
    return token_ids, tokens


def get_in_turn_repetition(pred, is_cn=False):
    """Get in-turn repetition."""
    if len(pred) == 0:
        return 1.0
    if isinstance(pred[0], str):
        pred = [tok.lower() for tok in pred]
        if is_cn:
            pred = "".join(pred)
    tri_grams = set()
    for i in range(len(pred) - 2):
        tri_gram = tuple(pred[i:i + 3])
        if tri_gram in tri_grams:
            return True
        tri_grams.add(tri_gram)
    return False


def select_response(ids, scores, tokenizer, max_dec_len=None, num_return_sequences=1, keep_space=True):
    results = []
    group = []
    tmp = []
    if scores is not None:
        ids = ids.numpy()
        scores = scores.numpy()

        if len(ids) != len(scores) or (len(ids) % num_return_sequences) != 0:
            raise ValueError(
                "the length of `ids` is {}, but the `num_return_sequences` is {}"
                .format(len(ids), num_return_sequences))

        for pred, score in zip(ids, scores):
            pred_token_ids, pred_tokens = post_process_response(pred, tokenizer)
            num_token = len(pred_token_ids)
            if keep_space:
                response = " ".join(pred_tokens)
            else:
                response = "".join(pred_tokens)

            in_turn_repetition = get_in_turn_repetition(
                pred_tokens, True) or get_in_turn_repetition(pred_token_ids)
            # not ending
            if max_dec_len is not None and num_token >= max_dec_len:
                score -= 1e3
            elif in_turn_repetition:
                score -= 1e3

            tmp.append([response, score])
            if len(tmp) == num_return_sequences:
                group.append(tmp)
                tmp = []

        for preds in group:
            preds = sorted(preds, key=lambda x: -x[1])
            results.append(preds[0][0])
    else:
        ids = ids.numpy()

        for pred in ids:
            pred_token_ids, pred_tokens = post_process_response(pred, tokenizer)
            num_token = len(pred_token_ids)
            if keep_space:
                response = " ".join(pred_tokens)
            else:
                response = "".join(pred_tokens)

            in_turn_repetition = get_in_turn_repetition(
                pred_tokens, True) or get_in_turn_repetition(pred_token_ids)

            last_pos = 0
            if (max_dec_len is not None
                    and num_token >= max_dec_len) or in_turn_repetition:
                tmp.append([response])
            else:
                tmp.insert(last_pos, [response])
                last_pos += 1

            if len(tmp) == num_return_sequences:
                group.append(tmp)
                tmp = []

        for preds in group:
            results.append(preds[0][0])
    return results


def interaction(model, tokenizer, history):
    inputs = tokenizer.dialogue_encode(history,
                                       add_start_token_as_response=True,
                                       return_tensors=True,
                                       is_split_into_words=False)
    inputs['input_ids'] = inputs['input_ids'].astype('int64')
    ids, scores = model.generate(
        input_ids=inputs['input_ids'],
        token_type_ids=inputs['token_type_ids'],
        position_ids=inputs['position_ids'],
        attention_mask=inputs['attention_mask'],
        max_length=30,
        min_length=0,
        decode_strategy='sampling',
        temperature=1.0,
        top_k=3,
        top_p=1.0,
        num_beams=0,
        length_penalty=1.0,
        early_stopping=False,
        num_return_sequences=5,
        use_faster=True)
    bot_response = select_response(ids, scores, tokenizer, 30, 5, keep_space=False)[0]
    return bot_response


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8016
    paddle.set_device('cpu')
    model_name = 'plato-mini'
    model = UnifiedTransformerLMHeadModel.from_pretrained(model_name)
    tokenizer = UnifiedTransformerTokenizer.from_pretrained(model_name)
    model.eval()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(20)

    while True:
        conn, addr = s.accept()
        request = conn.recv(1024)

        history = json.loads(request.decode())
        reply = interaction(model, tokenizer, history)

        conn.sendall(reply.encode())
        conn.close()
```
##### 客户端
```
import socket
import json

HOST = '127.0.0.1'
PORT = 8016


def main(history):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    s.sendall(history.encode())
    reply = s.recv(1024)

    # send 函数的参数和 recv 函数的返回值都是 bytes 类型
    print('reply is:', reply.decode())
    s.close()
    return reply.decode()


if __name__ == '__main__':
    history = ['你好啊~']
    main(json.dumps(history, ensure_ascii=False))
```
这两个文件的port需一致

运行：

运行socket_service.py，保持运行

![](/personal-site-mvp/img/doc-placeholder.svg "")
再运行socket_client.py

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 2、对话模型接入智能机器人
##### 功能
闲聊机器人

* 来聊天吧：聊天激活，超过一分钟没有互动会自动结束对话
* *任意内容：在聊天激活时会进行闲聊
* 结束聊天：结束对话
* 聊天记录：在聊天激活时，返回当前对话记录

##### 数据表hirobot
![](/personal-site-mvp/img/doc-placeholder.svg "")
```
"""
智能机器人

"""
import base64
import json
import time
import pymysql
import requests

from datetime import datetime
from dateutil.relativedelta import relativedelta
from Crypto.Cipher import AES
from flask import Flask, request

import socket_client


app = Flask(__name__)


def base64_urlsafe_decode(s):
    """
    Base64URLSafe 解码
    """
    s = s.replace('-', '+').replace('_', '/') + '=' * (len(s) % 4)
    return base64.b64decode(s)


def AESdecrypt(msg):
    """
    AES解密
    加密算法：AES-128
    加密模式：ECB
    填充方式：PKCS5（PKCS7兼容）
    编码方式：Base64URLSafe（它不在末尾填充=号，并将标准Base64中的+和/分别改成了-和_）
    """
    EncodingAESKey = ''
    ciphertext = msg.decode('utf-8')
    cipher = AES.new(base64_urlsafe_decode(EncodingAESKey), AES.MODE_ECB)
    res = cipher.decrypt(base64_urlsafe_decode(ciphertext))
    return res[0:-res[-1]]


def send_message(body, groupid):
    """
    发送信息到hi群
    """
    webhook = ''
    data = {
        "message": {
            "header": {
                "toid": [groupid]
            },
            "body": body
        }
    }
    headers = {"Content-Type": "application/json"}
    req = requests.post(webhook, data=json.dumps(data), headers=headers)
    req_dic = json.loads(req.content)
    print(req_dic)
    return req_dic


def get_history(username):
    """
    聊天记录
    """
    res = None
    sql = "select content from hirobot where usr = '%s'" % username
    my_sql = Mysql()
    sql_res = my_sql.query(sql)
    my_sql.close()
    for item in sql_res:
        content_json = item[0]
        try:
            res = json.loads(content_json)
        except:
            print('content err: %s' % sql_res)
    return res


def get_time():
    """
    获取聊天有效期限（1min） 格式：['2022-07-09 12:00:00', '2022-07-09 12:01:00]
    """
    NOW = datetime.now()
    delta = relativedelta(minutes=1)
    fmt = lambda dt: dt.strftime("%Y-%m-%d %H:%M:%S")
    day = (fmt(NOW + delta * i) for i in range(0, 2))
    day = list(day)
    return day


def chat(content, username):
    """
    聊天对话
    """
    act_res = None
    if chat_is_active(username):
        history = get_history(username)
        if content == '聊天记录':
            return process_font_color(history, username)
        if isinstance(history, list):
            print(history)
            history.append(content)
            res_talk = socket_client.main(json.dumps(history, ensure_ascii=False))
            print('reply is:', res_talk)
            act_res = [{"content": '[闲聊中]%s' % res_talk, "type": "TEXT"}]
            history.append(res_talk)
            starttime, lasttime = get_time()
            sql = "update hirobot set starttime = '%s', lasttime = '%s', content = '%s' where usr = '%s' " \
                  % (starttime, lasttime, json.dumps(history, ensure_ascii=False), username)
            my_sql = Mysql()
            my_sql.update(sql)
            my_sql.close()
    return act_res


def process_font_color(history, username):
    """
    处理聊天记录格式
    """
    content = '###### 聊天记录 \n'
    cur_color = 'green'
    cur = 'rob'
    for item in history:
        tmp = '%s: <font color=\"%s\">%s</font> \n' % (cur, cur_color, item)
        content += tmp
        if cur_color == 'green':
            cur_color = 'gray'
            cur = username
        else:
            cur_color = 'green'
            cur = 'rob'
    res = [{"content": '%s' % content, "type": "MD"}]
    return res


def chat_is_active(username):
    """
    聊天是否激活
    """
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    sql = "select usr from hirobot where is_active = 1 and usr = '%s' and starttime < '%s' and lasttime > '%s'" \
          % (username, now, now)
    my_sql = Mysql()
    res = my_sql.query(sql)
    my_sql.close()
    return len(res) > 0


def end_chat(username):
    """
    结束聊天
    """
    if has_usr(username):
        sql = "update hirobot set is_active = 0 where usr = '%s' " % username
        my_sql = Mysql()
        my_sql.update(sql)
        my_sql.close()


def start_chat(username):
    """
    开始聊天
    """
    starttime, lasttime = get_time()
    history = ['你好啊~']
    my_sql = Mysql()
    if has_usr(username):
        sql = "update hirobot set is_active = 1, starttime = '%s', lasttime = '%s', content = '%s' where usr = '%s' " \
              % (starttime, lasttime, json.dumps(history, ensure_ascii=False), username)
    else:
        sql = "insert into hirobot(usr,is_active,starttime,lasttime) values('%s',1,'%s','%s');" \
              % (username, starttime, lasttime)
    my_sql.update(sql)
    my_sql.close()


def has_usr(username):
    """
    用户是否存在
    """
    sql = "select usr from hirobot where usr = '%s'" % username
    my_sql = Mysql()
    res = my_sql.query(sql)
    my_sql.close()
    return len(res) > 0


class Mysql(object):
    """
    mysql 数据库操作类
    """
    def __init__(self):
        self.db = pymysql.connect(host='',
                                  port=,  # 不是字符串不需要加引号
                                  user='',
                                  password='',
                                  db='design-engine',
                                  charset='utf8'
                                  )
        self.cursor = self.db.cursor()

    def update(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def query(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except:
            return ()

    def close(self):
        self.db.close()


def hi_service(content, username, groupid):
    """
    处理内容
    """
    print(content, username, groupid)
    act_res = None
    if content == 'help':
        act_res = [{"content": '输入：@机器人 来聊天吧', "type": "TEXT"}]
    elif content == '来聊天吧':
        start_chat(username)
        act_res = [{"content": '[闲聊中]你好啊~ %s' % username, "type": "TEXT"}]
    elif content == '结束聊天':
        end_chat(username)
    else:
        act_res = chat(content, username)
    print('act_res: %s' % act_res)
    if act_res is not None:
        if act_res[0]['type'] == 'TEXT':
            act_res.append({"atuserids": [username], "type": "AT"})
        send_message(act_res, groupid)


@app.route('/rob', methods=['POST'])
def get_data():
    try:
        echostr = request.form.get('echostr', None)
        if echostr:
            # url 校验
            return echostr
        else:
            # 获取 raw body
            msg_base64 = request.get_data()
            # 解密
            decrypted = AESdecrypt(msg_base64)
            msg_data = json.loads(decrypted)
            print('获取msg_data: %s' % msg_data)
            groupid = msg_data['groupid']
            username = msg_data['message']['header']['fromuserid']
            body = msg_data['message']['body']
            # 只处理格式： @rob text
            if len(body) == 2:
                if 'content' in body[1]:
                    content = body[1]['content'].strip()
                    hi_service(content, username, groupid)
            return 'ok'
    except:
        return 'fail'


if __name__ == '__main__':
    app.run(host='', port=8015)

```
##### 项目构成
![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 运行
修改socket_client.py和socket_service.py中的开发机的 host、port， 这两个文件的port需一致，且与test.py的 port不同

修改test.py中的 机器人webhook、EncodingAESKey ，数据库的host、port、user、password，以及开发机的 host、port

后台运行（注意先后顺序）：

```
nohup python socket_service.py > log_socket_service.out 2>&1 &
nohup python test.py > log_python_test.out 2>&1 &
```
查看是否在后台运行：

![](/personal-site-mvp/img/doc-placeholder.svg "")
注意后台运行的程序别忘了实验结束后杀死进程

### 四、P图服务
##### 使用示例
![](/personal-site-mvp/img/doc-placeholder.svg "")


```
"""
智能机器人

"""
import base64
import json
import time
import pymysql
import requests

from datetime import datetime
from dateutil.relativedelta import relativedelta
from Crypto.Cipher import AES
from flask import Flask, request
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

import socket_client


app = Flask(__name__)


def base64_urlsafe_decode(s):
    """
    Base64URLSafe 解码
    """
    s = s.replace('-', '+').replace('_', '/') + '=' * (len(s) % 4)
    return base64.b64decode(s)


def AESdecrypt(msg):
    """
    AES解密
    加密算法：AES-128
    加密模式：ECB
    填充方式：PKCS5（PKCS7兼容）
    编码方式：Base64URLSafe（它不在末尾填充=号，并将标准Base64中的+和/分别改成了-和_）
    """
    EncodingAESKey = 'Iwc3lVvk439QCVPCQh6dYY'
    ciphertext = msg.decode('utf-8')
    cipher = AES.new(base64_urlsafe_decode(EncodingAESKey), AES.MODE_ECB)
    res = cipher.decrypt(base64_urlsafe_decode(ciphertext))
    return res[0:-res[-1]]


def send_message(body, groupid):
    """
    发送信息到hi群
    """
    webhook = ''
    data = {
        "message": {
            "header": {
                "toid": [groupid]
            },
            "body": body
        }
    }
    headers = {"Content-Type": "application/json"}
    req = requests.post(webhook, data=json.dumps(data), headers=headers)
    req_dic = json.loads(req.content)
    print(req_dic)
    return req_dic


def get_history(username):
    """
    聊天记录
    """
    res = None
    sql = "select content from hirobot where usr = '%s'" % username
    my_sql = Mysql()
    sql_res = my_sql.query(sql)
    my_sql.close()
    for item in sql_res:
        content_json = item[0]
        try:
            res = json.loads(content_json)
        except:
            print('content err: %s' % sql_res)
    return res


def get_time():
    """
    获取聊天有效期限（1min） 格式：['2022-07-09 12:00:00', '2022-07-09 12:01:00]
    """
    NOW = datetime.now()
    delta = relativedelta(minutes=1)
    fmt = lambda dt: dt.strftime("%Y-%m-%d %H:%M:%S")
    day = (fmt(NOW + delta * i) for i in range(0, 2))
    day = list(day)
    return day


def chat(content, username):
    """
    聊天对话
    """
    act_res = None
    if chat_is_active(username):
        history = get_history(username)
        if content == '聊天记录':
            return process_font_color(history, username)
        if isinstance(history, list):
            print(history)
            history.append(content)
            res_talk = socket_client.main(json.dumps(history, ensure_ascii=False))
            print('reply is:', res_talk)
            act_res = [{"content": '[闲聊中]%s' % res_talk, "type": "TEXT"}]
            history.append(res_talk)
            starttime, lasttime = get_time()
            sql = "update hirobot set starttime = '%s', lasttime = '%s', content = '%s' where usr = '%s' " \
                  % (starttime, lasttime, json.dumps(history, ensure_ascii=False), username)
            my_sql = Mysql()
            my_sql.update(sql)
            my_sql.close()
    return act_res


def process_font_color(history, username):
    """
    处理聊天记录格式
    """
    content = '###### 聊天记录 \n'
    cur_color = 'green'
    cur = 'rob'
    for item in history:
        tmp = '%s: <font color=\"%s\">%s</font> \n' % (cur, cur_color, item)
        content += tmp
        if cur_color == 'green':
            cur_color = 'gray'
            cur = username
        else:
            cur_color = 'green'
            cur = 'rob'
    res = [{"content": '%s' % content, "type": "MD"}]
    return res


def chat_is_active(username):
    """
    聊天是否激活
    """
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    sql = "select usr from hirobot where is_active = 1 and usr = '%s' and starttime < '%s' and lasttime > '%s'" \
          % (username, now, now)
    my_sql = Mysql()
    res = my_sql.query(sql)
    my_sql.close()
    return len(res) > 0


def end_chat(username):
    """
    结束聊天
    """
    if has_usr(username):
        sql = "update hirobot set is_active = 0 where usr = '%s' " % username
        my_sql = Mysql()
        my_sql.update(sql)
        my_sql.close()


def start_chat(username):
    """
    开始聊天
    """
    starttime, lasttime = get_time()
    history = ['你好啊~']
    my_sql = Mysql()
    if has_usr(username):
        sql = "update hirobot set is_active = 1, starttime = '%s', lasttime = '%s', content = '%s' where usr = '%s' " \
              % (starttime, lasttime, json.dumps(history, ensure_ascii=False), username)
    else:
        sql = "insert into hirobot(usr,is_active,starttime,lasttime) values('%s',1,'%s','%s');" \
              % (username, starttime, lasttime)
    my_sql.update(sql)
    my_sql.close()


def has_usr(username):
    """
    用户是否存在
    """
    sql = "select usr from hirobot where usr = '%s'" % username
    my_sql = Mysql()
    res = my_sql.query(sql)
    my_sql.close()
    return len(res) > 0


class Mysql(object):
    """
    mysql 数据库操作类
    """
    def __init__(self):
        self.db = pymysql.connect(host='',
                                  port=,  # 不是字符串不需要加引号
                                  user='',
                                  password='',
                                  db='',
                                  charset='utf8'
                                  )
        self.cursor = self.db.cursor()

    def update(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def query(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except:
            return ()

    def close(self):
        self.db.close()


IMG_INFO = {
    '粉丝': {
        'img': 'fans',
        'font_color': 'black',
        'hight': 65,
        'width': 24,
        'font_size': 13,
    },
    '鲁迅': {
        'img': 'luxun',
        'hight': 30,
        'width': 300,
        'font_size': 18,
        'font_color': 'white'
    }
}


def add_font_to_img(content):
    """
    P图服务
    """
    img_type = content[0:2]
    text = content.split(' ')[1].strip()
    # 加载配置
    draw_conf = {}
    for key in ['img', 'hight', 'width', 'font_size', 'font_color']:
        draw_conf[key] = None
        if key in IMG_INFO[img_type]:
            draw_conf[key] = IMG_INFO[img_type][key]
        else:
            return None
    # 部分字数限制&调整
    if img_type == '鲁迅':
        if len(text) > 10:
            return None
    elif img_type == '粉丝':
        if len(text) > 4 or len(text) == 1:
            return None
        elif len(text) == 3:
            draw_conf['hight'], draw_conf['font_size'] = 60, 12
        elif len(text) == 4:
            draw_conf['hight'], draw_conf['font_size'] = 54, 12
    # p图
    img_name = draw_conf['img']
    img = Image.open('img/%s.png' % img_name)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('img/msyh.ttf', draw_conf['font_size'])
    draw.text((draw_conf['hight'], draw_conf['width']), text, font=font, fill=draw_conf['font_color'])
    # 画面本来信息
    if img_type == '鲁迅':
        draw.text((200, 340), '—— 鲁迅', font=font, fill=draw_conf['font_color'])
    f = BytesIO()
    img.save(f, 'png')
    data = f.getvalue()
    img_code = str(base64.b64encode(data).decode())
    res = [{"content": img_code, "type": "IMAGE"}]
    f.close()
    return res


def hi_service(content, username, groupid):
    """
    处理内容
    """
    print(content, username, groupid)
    act_res = None
    if content == 'help':
        act_res = [{"content": '输入：@机器人 来聊天吧', "type": "TEXT"}]
    elif ' ' in content and len(content) > 3 and content[0:2] in IMG_INFO:
        act_res = add_font_to_img(content)
    elif content == '来聊天吧':
        start_chat(username)
        act_res = [{"content": '[闲聊中]你好啊~ %s' % username, "type": "TEXT"}]
    elif content == '结束聊天':
        end_chat(username)
    else:
        act_res = chat(content, username)
    print('act_res: %s' % act_res)
    if act_res is not None:
        if act_res[0]['type'] == 'TEXT':
            act_res.append({"atuserids": [username], "type": "AT"})
        send_message(act_res, groupid)


@app.route('/rob', methods=['POST'])
def get_data():
    try:
        echostr = request.form.get('echostr', None)
        if echostr:
            # url 校验
            return echostr
        else:
            # 获取 raw body
            msg_base64 = request.get_data()
            # 解密
            decrypted = AESdecrypt(msg_base64)
            msg_data = json.loads(decrypted)
            print('获取msg_data: %s' % msg_data)
            groupid = msg_data['groupid']
            username = msg_data['message']['header']['fromuserid']
            body = msg_data['message']['body']
            # 只处理格式： @rob text
            if len(body) == 2:
                if 'content' in body[1]:
                    content = body[1]['content'].strip()
                    hi_service(content, username, groupid)
            return 'ok'
    except:
        return 'fail'


if __name__ == '__main__':
    app.run(host='', port=8015)

```
##### 项目构成
[附件: img.zip | 8.9MB | application/zip | fileId=bdd66bf2e9aa4d06ae127880e94c42dd]
![](/personal-site-mvp/img/doc-placeholder.svg "")
运行不变

### 五、chatgpt
##### 使用示例
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 接口密钥获取
在 [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys) 新增一个api key

![](/personal-site-mvp/img/doc-placeholder.svg "")
用postman测试下

![](/personal-site-mvp/img/doc-placeholder.svg "")
对应py代码：

```
CHATGPT_API_KEY = 'xxx'
CHATGPT_API_URL = 'https://api.openai.com/v1/completions'

data = {
    "model": "text-davinci-003",
    "prompt": content,
    "max_tokens": 2048,
    "temperature": 0,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0.6,
    "stop": [
        " Human:",
        " AI:"
    ]
}
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer %s" % CHATGPT_API_KEY}
req = requests.post(CHATGPT_API_URL, data=json.dumps(data), headers=headers)
req_dic = json.loads(req.content)
```
##### 代码构成
在开发机上运行 python main.py

```
"""
智能机器人 chatgpt

"""
import base64
import json

import requests

from Crypto.Cipher import AES
from flask import Flask, request

app = Flask(__name__)

CHATGPT_API_URL = 'https://api.openai.com/v1/completions'
CHATGPT_API_KEY = ''
WEBHOOK = ''
ENCODEAESKey = ''


def base64_urlsafe_decode(s):
    """
    Base64URLSafe 解码
    """
    s = s.replace('-', '+').replace('_', '/') + '=' * (len(s) % 4)
    return base64.b64decode(s)


def AESdecrypt(msg):
    """
    AES解密

    加密算法：AES-128
    加密模式：ECB
    填充方式：PKCS5（PKCS7兼容）
    编码方式：Base64URLSafe（它不在末尾填充=号，并将标准Base64中的+和/分别改成了-和_）
    """
    EncodingAESKey = ENCODEAESKey
    ciphertext = msg.decode('utf-8')
    cipher = AES.new(base64_urlsafe_decode(EncodingAESKey), AES.MODE_ECB)
    res = cipher.decrypt(base64_urlsafe_decode(ciphertext))
    return res[0:-res[-1]]


def chatgpt_api(content):
    """
    处理内容
    """
    res = None
    data = {
        "model": "text-davinci-003",
        "prompt": content,
        "max_tokens": 2048,
        "temperature": 0,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0.6,
        "stop": [
            " Human:",
            " AI:"
        ]
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % CHATGPT_API_KEY}
    req = requests.post(CHATGPT_API_URL, data=json.dumps(data), headers=headers)
    req_dic = json.loads(req.content)
    print(req_dic)
    if 'choices' in req_dic and len(req_dic['choices']) > 0:
        text_group = req_dic['choices'][0]
        if 'text' in text_group:
            res = text_group['text']
            res = res.strip()
    return res


def send_message(body, groupid):
    """
    发送信息到hi群
    """
    webhook = WEBHOOK
    data = {
        "message": {
            "header": {
                "toid": [groupid]
            },
            "body": body
        }
    }
    headers = {"Content-Type": "application/json"}
    req = requests.post(webhook, data=json.dumps(data), headers=headers)
    req_dic = json.loads(req.content)
    print(req_dic)
    return req_dic


def chatgpt_hi_service(content, username, groupid):
    """
    处理内容
    """
    print(content, username, groupid)
    content_res = chatgpt_api(content)
    act_res = [{"content": content_res, "type": "TEXT"}]
    print('act_res: %s' % act_res)
    if content_res is not None:
        act_res.append({"atuserids": [username], "type": "AT"})
        send_message(act_res, groupid)


@app.route('/rob', methods=['POST'])
def get_data():
    try:
        echostr = request.form.get('echostr', None)
        if echostr:
            # url 校验
            return echostr
        else:
            # 获取 raw body
            msg_base64 = request.get_data()
            # 解密
            decrypted = AESdecrypt(msg_base64)
            msg_data = json.loads(decrypted)
            print('获取msg_data: %s' % msg_data)
            groupid = msg_data['groupid']
            username = msg_data['message']['header']['fromuserid']
            body = msg_data['message']['body']
            # 只处理格式： @rob text
            if len(body) == 2:
                if 'content' in body[1]:
                    content = body[1]['content'].strip()
                    chatgpt_hi_service(content, username, groupid)
            return 'ok'
    except:
        return 'fail'


if __name__ == '__main__':
    app.run(host='', port=8015)

```
注：api.openai.com被内网墙了，自己找个外网中转

##### **更新 解决**api.openai.com被墙的问题**：**
原理：机器人的后端是在内网机子上，调api的接口部署在外网上，内网去调外网的接口，外网去和chatgpt的api交互

只改一行代码，将

CHATGPT_API_URL = 'https://api.openai.com/v1/completions'

改为

CHATGPT_API_URL = 'http://43.137.46.199:8015/'

自己做个外网中转，参考[云服务器简单部署flask（chatgpt）](./如流智能机器人（闲聊plato、p图、chatgpt）_引用文档/云服务器简单部署flask（chatgpt）.md)



### **一些可能的报错：**
1、python TypeError: the JSON object must be str, not 'bytes'

原因：python版本太低，3.6以下，改一下json.loads相关代码

```
# msg_data = json.loads(decrypted)
msg_data = json.loads(decrypted.decode('utf-8'))  # python3.6以下
```
2、'latin-1' codec can't encode characters in position

原因：机子太破了编码有问题，改一下print相关代码

```
# print(req_res) # req_res为dic
print(str(req_res).encode("utf-8").decode("latin1"))  # 编码报错
```
![](/personal-site-mvp/img/doc-placeholder.svg "")

