# ベースイメージを指定
FROM python:3.9

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコピー
COPY . .

# 必要なパッケージをインストール
RUN pip install requests schedule

# コンテナ起動時に実行するコマンドを指定
CMD [ "python", "main.py" ]