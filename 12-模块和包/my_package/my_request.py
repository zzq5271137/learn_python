def get_request(url):
    data = {'body': 'abc'}
    print('您的GET请求%s已经下载下来了, 数据为: %s' % (url, data))
    return data


def post_request(url):
    data = {'body': 'abc'}
    print('您的POST请求%s已经下载下来了, 数据为: %s' % (url, data))
    return data
