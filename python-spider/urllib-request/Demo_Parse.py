from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, urljoin, parse_qs, parse_qsl, urlencode, quote, unquote

# urlparse 示例
result = urlparse('https://docs.python.org/zh-cn/3.7/library/urllib.parse.html#module-urllib.parse')
print(type(result))
print(result)

print(result.netloc)

print(result[1])

result1 = urlparse('docs.python.org/zh-cn/3.7/library/urllib.parse.html#module-urllib.parse', scheme = "https", allow_fragments = False)
print(result1)

# urlunparse 示例
params = ('https', 'www.geekdigging.com', 'index.html', 'people', 'a=1', 'geekdigging')
print(urlunparse(params))

# urlsplit 示例
result_urlsplit = urlsplit("https://www.geekdigging.com/index.html;people?a=1#geekdigging")
print(type(result_urlsplit))
print(result_urlsplit)

print(result_urlsplit.netloc)
print(result_urlsplit[1])

# urlunsplit 示例
params_urlunsplit = ('https', 'www.geekdigging.com', 'index.html;people', 'a=1', 'geekdigging')
print(urlunsplit(params_urlunsplit))

# urljoin 示例
print(urljoin("https://www.geekdigging.com/", "index.html"))
print(urljoin("https://www.geekdigging.com/", "https://www.geekdigging.com/index.html"))
print(urljoin("https://www.geekdigging.com/", "?a=aa"))
print(urljoin("https://www.geekdigging.com/#geekdigging", "https://docs.python.org/zh-cn/3.7/library/urllib.parse.html"))

# parse_qs 示例
print(parse_qs("ie=UTF-8&wd=python"))

# parse_qsl 示例
print(parse_qsl("ie=UTF-8&wd=python"))

# urlencode 示例
dict = {
    "name": "极客挖掘机",
    "age": 18
}
print("https://www.geekdigging.com/" + urlencode(dict))

# quote 示例
print(quote("极客挖掘机"))

# unquote 示例
print(unquote("%E6%9E%81%E5%AE%A2%E6%8C%96%E6%8E%98%E6%9C%BA"))