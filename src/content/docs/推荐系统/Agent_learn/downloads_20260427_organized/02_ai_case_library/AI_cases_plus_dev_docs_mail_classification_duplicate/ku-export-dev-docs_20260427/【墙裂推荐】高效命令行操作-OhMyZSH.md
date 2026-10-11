---
title: "看看效果"
description: "【墙裂推荐】高效命令行操作-OhMyZSH"
date: "2026-04-28"
category: "推荐系统"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-dev-docs_20260427\\【墙裂推荐】高效命令行操作-OhMyZSH.md"
---
【墙裂推荐】高效命令行操作-OhMyZSH

帮助协助大家排查问题的时候，发现绝大部分同学，在命令行输入的时候极其低效：

* 一个一个字母慢慢敲，经常出现反复多次输入错误
* 在某个文档里面维护自己常用的命令，每次找到文档，复制粘贴过来过来用



在此推荐个人在用的比较方便的工具 OhMyZsh  [https://github.com/ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh)



**关于命令行IDE，Mac下，强烈推荐 iTerm**  [https://iterm2.com/](https://iterm2.com/)



# 看看效果
> 更多功能插件自行探索
命令输入过程中，根据常用命令自动提示(键盘右键自动填充)

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


命令语法提示(当前如果是正确的命令则绿色 否则红色)

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


# 自定义命令
基于自定义命令，可以将那些又臭又长的、但是使用频率又非常高的命令完成简化

> 注意，自定义命令的时候别和已存在的冲突了
> vim ~/.zshrc 写到~/.zshrc这个文件里面
## 快捷历史命令搜索
> alias hs='history | grep'
> 直接 hs xxxx 命令即可实现对历史输入过的包含关键字xxxx的命令的搜索（重复的太多了，基于函数可以实现去重）
```
# alias s="history | grep"
function hs(){
  grep -i "$1" ~/.zsh_history | sed 's/^[^;]*;//' | awk '!seen[$0]++'
}
```
![hs 'git reset'](/personal-site-mvp/img/doc-placeholder.svg "hs 'git reset'")
![hs conda](/personal-site-mvp/img/doc-placeholder.svg "hs conda")
![hs redis](/personal-site-mvp/img/doc-placeholder.svg "hs redis")
![hs ai-guyouda](/personal-site-mvp/img/doc-placeholder.svg "hs ai-guyouda")
## 连接数据库
> alias cnt_mysql='mysql -h127.0.0.1 -P8036 -uxxx -pxxxxx -Dxxx'
> alias cnt_redis='redis-cli -h 10.127.0.0.1 -p 8888'
> alias cnt_mongo='mongo --host 127.0.0.1 --port 8888 test'
* 直接cnt_mysql命令就连上Mysql数据库了
* 直接cnt_redis命令就连上Redis数据库了
* 直接cnt_mongo命令就连上Mongo数据库了

## git push
> vim ~/.zshrc
> 复杂命令可以基于函数实现复杂参数的传递
> push() { git push origin HEAD:refs/for/$1; }
* 直接push master命令就完成master分支的推送
* 直接push develop命令就完成develop分支的推送



更多玩法大家自行探索，复杂情况不会自定义的，可以问问ai



## ducc
比如我觉得文档全是文字太素了，不好看，日常经常需要找各种emoji

```
function emj() {
  ducc -p "$1 对应emoji用哪个最合适, 其他备选方案也给一下, 并说明推荐理由"
}
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
# Mac安装
打开命令行

```
# 1. 确认自己的Mac是否已经有zsh
which zsh
# 1.1 如果已经有，进入2； 否则执行下面命令安装
brew install zsh

# 2.修改默认为zsh, 后面是自己的zsh的路径
sudo  chsh -s /bin/zsh

# 3.安装oh-my-zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# 4.安装插件
git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting

# 5.配置插件, 找到 plugins=(git), 修改为  plugins=(git zsh-autosuggestions  zsh-syntax-highlighting)
vim ~/.zshrc

# 6.配置历史命令检索快捷指令
alias s="history | grep "

# 7.激活配置
source ~/.zshrc

```


# Linux安装
```
# 1. 确认自己的Mac是否已经有zsh
which zsh
# 1.1 如果已经有，进入2； 否则执行下面命令安装
sudo yum install zsh

# 2.修改默认为zsh, 后面是自己的zsh的路径
sudo  chsh -s /bin/zsh

# 3.安装oh-my-zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# 4.安装插件
git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting

# 5.配置插件, 找到 plugins=(git), 修改为  plugins=(git zsh-autosuggestions  zsh-syntax-highlighting)
vim ~/.zshrc

# 6.配置历史命令检索快捷指令
alias s="history | grep "

# 7.激活配置
source ~/.zshrc

```


# 最最重要的
**以上只是列举的两个最常用的插件，实际上有非常非常非常多优秀的各种其他插件，大家可以自行搜索安装使用**



![](/personal-site-mvp/img/doc-placeholder.svg "")

