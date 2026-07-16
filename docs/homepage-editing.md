# Homepage Editing Guide

这个首页现在主要靠一个文件维护：

- `/_data/homepage.yml`

如果你以后要更新内容，优先只改这个文件。绝大多数情况下，你不需要改 HTML、CSS 或 Jekyll 模板。

## 你以后修改首页，最推荐的实际流程

每次都按下面做：

1. 打开 `/_data/homepage.yml`
2. 修改你要更新的文字、链接、论文或新闻
3. 如果有新图片，把图片放进 `/images/`
4. 运行本地预览：

```bash
./scripts/preview-local.sh
```

6. 打开 `http://127.0.0.1:4000/` 检查页面
7. 如果效果正确，再提交或推送到 GitHub

如果你只是更新内容，通常不需要改这些文件：

- `/_includes/homepage.html`
- `/_layouts/homepage.html`
- `scripts/preview-local.sh`

## 最常见的更新

### 1. 改个人简介

找到：

```yml
about:
  paragraphs:
    - "第一段"
    - "第二段"
```

直接修改引号里的文字即可。一段就是一行 `- "..."`。

### 2. 改邮箱、GitHub、Google Scholar

找到：

```yml
hero:
  socials:
```

把对应的 `href` 改掉即可。

### 2.1 改首页姓名和单位信息

找到：

```yml
hero:
  name: "Li Hao"
  role_en: "..."
```

这 2 个字段分别控制：

- `name`：首页显示的姓名
- `role_en`：英文单位行

### 3. 新增一条新闻

找到：

```yml
news:
  items:
```

照着已有格式复制一条：

```yml
    - date: "2026.03"
      text: "你的新消息写在这里。"
```

如果新消息属于一个此前没有出现过的年份，也要在 `news.years` 最上方加上该年份，例如：

```yml
news:
  years:
    - "2027"
    - "2026"
```

### 3.1 修改研究方向

找到：

```yml
research:
  items:
```

每个研究方向由一个标题和一段说明组成：

```yml
    - title: "Research topic"
      description: "A concise description of this research direction."
```

### 4. 新增一篇论文

找到：

```yml
publications:
  items:
```

复制一篇已有论文，改这些字段：

```yml
    - year: "2026"
      category: "llm"
      title: "论文标题"
      venue: "会议或期刊"
      tags:
        - "标签1"
        - "标签2"
      links:
        - label: "Paper"
          href: "https://..."
      image: "/images/你的图片文件名.jpg"
```

默认首页先显示前 4 篇论文，点击 `More` 会展开全部。论文栏目只保留顶会论文；每篇论文需要一张配图。你不需要填写 `category` 或 `tags`。

如果你以后想改默认显示数量，修改：

```yml
publications:
  initial_visible: 4
```

如果你想修改 `More / Less` 按钮文案，改这里：

```yml
publications:
  more_label: "More"
  less_label: "Less"
```

## 图片怎么换

头像和论文配图放在：

- `/images/`

然后在 `/_data/homepage.yml` 里填写对应路径。头像使用 `hero.photo`：

- `/images/xxx.jpg`

例如：

```yml
hero:
  photo: "/images/profile.jpg"
```

论文配图使用每篇论文中的 `image`：

```yml
image: "/images/your-paper-figure.jpg"
```

## 哪些内容已经被隐藏

这次首页里已经去掉了：

- `Teaching`
- `Join Us`
- 首屏里的招生按钮
- 教学版块
- 招生版块

如果以后你想重新启用，不建议自己改模板，直接告诉我加回去会更稳。

## 一个最简单的维护原则

以后优先只做这两件事：

1. 改 `/_data/homepage.yml`
2. 把新图片放到 `/images/`

只要不碰 `/_includes/homepage.html`，页面样式基本不会坏。

## 本地预览

如果你想在浏览器里先看效果，再决定是否提交，运行：

```bash
./scripts/preview-local.sh
```

然后打开：

```text
http://127.0.0.1:4000/
```

说明：

- 这个脚本会把当前站点同步到 `/tmp/lihaogx-preview-copy`
- 会自动安装本地预览需要的 Ruby 依赖
- 会在无空格目录里启动 Jekyll，避免本机 Ruby gem 编译踩路径问题

如果你想换端口，比如 `4001`：

```bash
./scripts/preview-local.sh 4001
```

## 如果你想发布到线上

本地看起来没问题后，通常只需要：

```bash
git add .
git commit -m "update homepage content"
git push
```

如果你的 GitHub Pages 已经连接这个仓库，推送后会自动发布。
