# 使用官方 Python 3.12 基础镜像
FROM python:3.12

# 设定工作目录
WORKDIR /QQMusicSpiders

# 请将 'YOUR_REPOSITORY_URL' 替换为你的 GitHub 仓库地址
RUN git clone https://github.com/xxx/QQMusicSpiders.git

# 进入工作目录
WORKDIR /QQMusicSpiders/v2/api

# 安装 Flask 和 gunicorn
RUN pip install Flask gunicorn

# 安装 requirements.txt 中指定的其他依赖
RUN pip install -r requirements.txt

# 设置 Flask 应用程序的名称
ENV NAME=qq

# 暴露 Flask 应用程序的默认端口 8888
EXPOSE 8888

# 定义应用程序的入口点
ENTRYPOINT ["gunicorn"]
CMD ["-b", "0.0.0.0:8888", "$NAME:app"]