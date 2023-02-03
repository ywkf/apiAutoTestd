from tool.read_yaml import read_yaml

"""公共变量"""
# 请求域名
host = "http://localhost:9090"
# 请求信息头
headers = {"Content-Type": "application/json"}
# 文章id
article_id = None
# 读取文章
article = read_yaml("mp_article.yaml")
# 文章标题
article_title = article[0][0]
# 文章内容
article_content = article[0][1]
# 频道id
channel_id = article[0][2]
# 频道名称
channel = article[0][3]