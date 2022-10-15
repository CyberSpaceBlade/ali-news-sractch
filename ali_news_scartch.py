import datetime
import re
import time

import requests
def download():
    url = "https://www.alibabagroup.com/news-and-resource"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "upgrade-insecure-requests": "1",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "max-age=0",
        "cookie": "_bl_uid=z8lqC9w874tz8Li85j35pjgdLnLU; ice_locale=zh-CN"}
    answer = requests.get(url, headers=headers)
    # print(answer.content)
    with open("source_code.txt", "wb") as f:
        f.write(answer.content)
    f.close()
    print("源代码下载完成！")

def select_date_and_source():
    with open("source_code.txt", "r", encoding="utf-8") as f:
        text = f.readline()
        date_res = []
        source_res = []
        while (text):
            a = r'documentPublishTimeLocal":"\d{4}年\d{1,}月\d{1,}日"'
            b = r'categoryName":"\w{1,}"'
            s1 = re.findall(a, text)
            s2 = re.findall(b, text)
            if s1:  # 查找到日期
                temp1 = ("".join(s1))
                temp1 = temp1.split('"')
                i = 2
                while (i < len(temp1)):
                    date_res.append(temp1[i])
                    # print(temp1[i])
                    i = i + 3
                text = f.readline()
            else:
                text = f.readline()

            if s2:  # 查找到来源
                temp2 = ("".join(s2))
                temp2 = temp2.split('"')
                j = 2
                while (j < len(temp2)):
                    source_res.append(temp2[j])
                    #print(temp2[j])
                    j = j + 3

                text = f.readline()
            else:
                text = f.readline()
    f.close()

    with open ("date_and_source.txt","w") as f:
        for i in date_res:
            f.write(i+" ")
        f.write("\n")
        for i in source_res:
            f.write(i+" ")
        f.write("\n")
    f.close()
    print("新闻来源和日期获取完成！")

def select_title_and_id():
    with open("source_code.txt", "r", encoding="utf-8") as f:
        text = f.readline()
        title_res = []
        id_res = []
        while (text):
            a = r'documentTitle"(.*?)","documentCover'
            b = r'documentId":"\d{5,}"'
            s1 = re.findall(a, text)
            s2 = re.findall(b, text)
            if s1:  # 新闻标题
                temp1 = ("".join(s1))
                temp1 = temp1.split(':"')
                i = len(temp1) - 20
                while i < len(temp1):
                    title_res.append(temp1[i])
                    # print(temp1[i]+"\n")
                    i = i + 1
            text = f.readline()

            if s2:  # 新闻网址
                temp2 = ("".join(s2))
                temp2 = temp2.split('"')
                j = 2
                while (j < len(temp2)):
                    temp2[j] = "https://www.alibabagroup.com/document-" + temp2[j]
                    id_res.append(temp2[j])
                    # print(temp2[j])
                    j = j + 3
            text = f.readline()
    f.close()

    with open("title_and_id.txt", "w") as f:
        for i in range(0, 20):
            f.write(title_res[i] + " " + id_res[i])
            f.write("\n")
    f.close()
    print("新闻网址和标题获取完成！")

def news_and_report():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "BIDUPSID=B6EA7C9B05DAB3C37B715A2AB92BD08B; PSTM=1629100955; BD_UPN=12314753; __yjs_duid=1_bbe39be9ba12597a6659dac18a1b797c1629101225013; BDUSS=JHdnJDVTJnc1RTVkF-S1NmNkdST0o4MFJobFd5Ykt6aTVxYWQ2TUV2Z2h2YlZpSUFBQUFBJCQAAAAAAAAAAAEAAADK2ualc3VubnnJscbGwMcwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACEwjmIhMI5iR2; BDUSS_BFESS=JHdnJDVTJnc1RTVkF-S1NmNkdST0o4MFJobFd5Ykt6aTVxYWQ2TUV2Z2h2YlZpSUFBQUFBJCQAAAAAAAAAAAEAAADK2ualc3VubnnJscbGwMcwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACEwjmIhMI5iR2; H_WISE_SIDS_BFESS=107313_110085_127969_131861_168388_176398_177985_178384_178530_178605_179345_179448_180276_181106_181398_181588_181709_182000_182243_182531_182663_183030_183223_183328_183536_183611_184010_184246_184267_184319_184735_184809_184892_185029_185037_185268_185519_185726_185873_185879_186039_186206_186313_186317_186411_186446_186558_186597_186636_186644_186665_186841_186898_187022_187062_187086_187188_187214_187282_187292_187326_187356_187421_187488_187533_187643_187828_187912_187928_187965_188049_8000055_8000116_8000125_8000139_8000144_8000153_8000173_8000178_8000182_8000186; MCITY=-175%3A; BAIDUID=CBA8C0900DFE4F7D7EC6354456675F9B:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=2k0kag8480050g81218l2ed01hkkb0e1b; ZFY=6ZYqElvxkR3JrX:B1wjGFYSkEbLTgDbwRrsqc5uOBfU0:C; BAIDUID_BFESS=CBA8C0900DFE4F7D7EC6354456675F9B:FG=1; delPer=0; BD_CK_SAM=1; PSINO=1; COOKIE_SESSION=5_0_7_9_2_13_0_3_7_9_1_0_67403_0_0_0_1665804446_0_1665805326%7C9%231636_441_1665403138%7C9; shifen[1616972_91638]=1665805331; BDSFRCVID=M44OJexroG0uYe7jsm_qqhcaZyUIz7OTDYLEOwXPsp3LGJLVcW-mEG0Pt8lgCZubaxOJogKKL2OTHm_F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=M44OJexroG0uYe7jsm_qqhcaZyUIz7OTDYLEOwXPsp3LGJLVcW-mEG0Pt8lgCZubaxOJogKKL2OTHm_F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJAHVILKtK-3H48k-4QEbbQH-UnLqMo3bmOZ04n-ah02ffTNjP65hqRQKf725lT8Qm5E_h7m3UTdsq76Wh35K5tTQP6rLtJUHCj4KKJxbInSepOL5t5H2M4phUJiBMAHBan7Wx7IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_RD6A-j6J3eU5eetjK2CntsJOOaCkKDlQOy4oWK441DhokK6bB-Kjd5tjSKbjAJf5V26Jc3M04X-o9-hvT-54e2p3FBUQjST6zQft20b3bhMJmXJQaK6b9aJ7jWhvdhl72y-crQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCHJ5DOJJFe_Ivt-5rDHJTg5DTjhPrM5fjTWMT-MTryKKJayRKbj4OzBnOaM-t_WlrPBRIfBanRhlRNB-3iV-OxDUvnyxAZ-ntL2xQxtNRJVnRj0MchHRj9XU6obUPUXa59LUvLX2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtD8KbKLCDT83-RJH-xQ0KnLXKKOLVKnGHl7ketn4hUt25qF8jU6e2lRZ-Cb23xcXQlT0Mp72QhrdQf4WWb3ebTJr32Qr-JO6HR6psIJM557SbUtl5f5KhURZaKviah4-BMb1Df7DBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6jyDGAqtjtJfKresJoq2RbhKROvhjRYj50gyxoObtRxtTTk0C3_-b6rqtjd-PQA2qLP2GJ9LU3kBgT9LMnx--t58h3_Xhjj3IuDQttjQn0OaIvmht5tK4ncOR7TyURdDx47yMcd0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OuJRQ2QJ8BtC85hDQP; H_BDCLCKID_SF_BFESS=tJAHVILKtK-3H48k-4QEbbQH-UnLqMo3bmOZ04n-ah02ffTNjP65hqRQKf725lT8Qm5E_h7m3UTdsq76Wh35K5tTQP6rLtJUHCj4KKJxbInSepOL5t5H2M4phUJiBMAHBan7Wx7IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_RD6A-j6J3eU5eetjK2CntsJOOaCkKDlQOy4oWK441DhokK6bB-Kjd5tjSKbjAJf5V26Jc3M04X-o9-hvT-54e2p3FBUQjST6zQft20b3bhMJmXJQaK6b9aJ7jWhvdhl72y-crQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCHJ5DOJJFe_Ivt-5rDHJTg5DTjhPrM5fjTWMT-MTryKKJayRKbj4OzBnOaM-t_WlrPBRIfBanRhlRNB-3iV-OxDUvnyxAZ-ntL2xQxtNRJVnRj0MchHRj9XU6obUPUXa59LUvLX2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtD8KbKLCDT83-RJH-xQ0KnLXKKOLVKnGHl7ketn4hUt25qF8jU6e2lRZ-Cb23xcXQlT0Mp72QhrdQf4WWb3ebTJr32Qr-JO6HR6psIJM557SbUtl5f5KhURZaKviah4-BMb1Df7DBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6jyDGAqtjtJfKresJoq2RbhKROvhjRYj50gyxoObtRxtTTk0C3_-b6rqtjd-PQA2qLP2GJ9LU3kBgT9LMnx--t58h3_Xhjj3IuDQttjQn0OaIvmht5tK4ncOR7TyURdDx47yMcd0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OuJRQ2QJ8BtC85hDQP; BCLID=10948395599364217531; BCLID_BFESS=10948395599364217531; BDRCVFR[C0p6oIjvx-c]=mk3SLVN4HKm; ZD_ENTRY=baidu; ab_sr=1.0.1_ZjNlY2E0OGFkZDI2YTgzNDIxYzY4YjAyMzc0OTg4ZTQyOTA0Y2I1ODE1ODc4OGI3N2ViNWUwZjMxZDkzYTI4NjBkMTUzN2Q2YzAyZmNmMWYxZjU1ZjYxZmY5N2NkOWI1Y2VkMTkxZmQxZmI1MTBiNTk2ZGVlYjU2YWY0Yjk0NzUyZDQzMWQ3Mjg3NGQ3NzQxMjQzZTM4MjE4NzBjZDIzYjRkNzM4ZTM4MTljNGEyNTBjNWRkMWM0MThmMDk2NWMz; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=37543_36545_37551_37359_37395_37406_36789_37534_37497_26350_22158; H_PS_645EC=9f5caE30vB1jLqilvNexRNN9bOcbZcX%2FA1Xnz0HxDV%2BuoPEwp6V4y9zuqNV0%2F1fnjhZd",
        "Host": "www.baidu.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    url = 'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=阿里巴巴'
    res = requests.get(url, headers=headers).text

    p_href = '<h3 class="news-title_1YtI1 "><a href="(.*?)"'
    href = re.findall(p_href, res)  # 获取新闻链接
    p_title = '<h3 class="news-title_1YtI1 ">.*?><!--s-text-->(.*?)<!--/s-text--></a>'
    title = re.findall(p_title, res, re.S)  # 获取新闻标题
    p_date = '<span class="c-color-gray2 c-font-normal c-gap-right-xsmall" aria-label=".*?>(.*?)</span>'
    date = re.findall(p_date, res)  # 获取新闻时间
    p_source = '<span class="c-color-gray" aria-label=".*?>(.*?)</span>'
    source = re.findall(p_source, res)  # 获取新闻来源

    for i in range(len(title)):  # 获取到的标题因为有关键字标签标出，二次处理
        title[i] = title[i].replace('<em>', "")
        title[i] = title[i].replace('</em>', "")
        # print(title[i])

    now = datetime.datetime.now().strftime("%Y-%m-%d %H%M%S")
    name = "news_report " + str(now) + ".txt"
    with open(name, "w") as f:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write('报告生成与数据爬取时间：' + str(now))
        f.write("\n")
        for i in range(10):
            string_temp = str(i+1)+". "+title[i] + "    新闻来源:" + source[i] + "  发布时间:" + date[i] + "\n"+href[i]

            f.write(string_temp)
            f.write("\n")
    f.close()
    print("阿里巴巴百度新闻数据报告生成完成！")

def Error_and_24():   #异常处理与24小时实时获取数据(1小时获取一次)
    while True:
        try:
            news_and_report()
            print("爬取成功，报告已生成！")
        except:
            print("爬取失败")
        time.sleep(3600)  #每一小时生成一份报告

def time_scratch():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "BIDUPSID=B6EA7C9B05DAB3C37B715A2AB92BD08B; PSTM=1629100955; BD_UPN=12314753; __yjs_duid=1_bbe39be9ba12597a6659dac18a1b797c1629101225013; BDUSS=JHdnJDVTJnc1RTVkF-S1NmNkdST0o4MFJobFd5Ykt6aTVxYWQ2TUV2Z2h2YlZpSUFBQUFBJCQAAAAAAAAAAAEAAADK2ualc3VubnnJscbGwMcwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACEwjmIhMI5iR2; BDUSS_BFESS=JHdnJDVTJnc1RTVkF-S1NmNkdST0o4MFJobFd5Ykt6aTVxYWQ2TUV2Z2h2YlZpSUFBQUFBJCQAAAAAAAAAAAEAAADK2ualc3VubnnJscbGwMcwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACEwjmIhMI5iR2; H_WISE_SIDS_BFESS=107313_110085_127969_131861_168388_176398_177985_178384_178530_178605_179345_179448_180276_181106_181398_181588_181709_182000_182243_182531_182663_183030_183223_183328_183536_183611_184010_184246_184267_184319_184735_184809_184892_185029_185037_185268_185519_185726_185873_185879_186039_186206_186313_186317_186411_186446_186558_186597_186636_186644_186665_186841_186898_187022_187062_187086_187188_187214_187282_187292_187326_187356_187421_187488_187533_187643_187828_187912_187928_187965_188049_8000055_8000116_8000125_8000139_8000144_8000153_8000173_8000178_8000182_8000186; MCITY=-175%3A; BAIDUID=CBA8C0900DFE4F7D7EC6354456675F9B:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=2k0kag8480050g81218l2ed01hkkb0e1b; ZFY=6ZYqElvxkR3JrX:B1wjGFYSkEbLTgDbwRrsqc5uOBfU0:C; BAIDUID_BFESS=CBA8C0900DFE4F7D7EC6354456675F9B:FG=1; delPer=0; BD_CK_SAM=1; PSINO=1; COOKIE_SESSION=5_0_7_9_2_13_0_3_7_9_1_0_67403_0_0_0_1665804446_0_1665805326%7C9%231636_441_1665403138%7C9; shifen[1616972_91638]=1665805331; BDSFRCVID=M44OJexroG0uYe7jsm_qqhcaZyUIz7OTDYLEOwXPsp3LGJLVcW-mEG0Pt8lgCZubaxOJogKKL2OTHm_F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=M44OJexroG0uYe7jsm_qqhcaZyUIz7OTDYLEOwXPsp3LGJLVcW-mEG0Pt8lgCZubaxOJogKKL2OTHm_F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJAHVILKtK-3H48k-4QEbbQH-UnLqMo3bmOZ04n-ah02ffTNjP65hqRQKf725lT8Qm5E_h7m3UTdsq76Wh35K5tTQP6rLtJUHCj4KKJxbInSepOL5t5H2M4phUJiBMAHBan7Wx7IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_RD6A-j6J3eU5eetjK2CntsJOOaCkKDlQOy4oWK441DhokK6bB-Kjd5tjSKbjAJf5V26Jc3M04X-o9-hvT-54e2p3FBUQjST6zQft20b3bhMJmXJQaK6b9aJ7jWhvdhl72y-crQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCHJ5DOJJFe_Ivt-5rDHJTg5DTjhPrM5fjTWMT-MTryKKJayRKbj4OzBnOaM-t_WlrPBRIfBanRhlRNB-3iV-OxDUvnyxAZ-ntL2xQxtNRJVnRj0MchHRj9XU6obUPUXa59LUvLX2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtD8KbKLCDT83-RJH-xQ0KnLXKKOLVKnGHl7ketn4hUt25qF8jU6e2lRZ-Cb23xcXQlT0Mp72QhrdQf4WWb3ebTJr32Qr-JO6HR6psIJM557SbUtl5f5KhURZaKviah4-BMb1Df7DBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6jyDGAqtjtJfKresJoq2RbhKROvhjRYj50gyxoObtRxtTTk0C3_-b6rqtjd-PQA2qLP2GJ9LU3kBgT9LMnx--t58h3_Xhjj3IuDQttjQn0OaIvmht5tK4ncOR7TyURdDx47yMcd0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OuJRQ2QJ8BtC85hDQP; H_BDCLCKID_SF_BFESS=tJAHVILKtK-3H48k-4QEbbQH-UnLqMo3bmOZ04n-ah02ffTNjP65hqRQKf725lT8Qm5E_h7m3UTdsq76Wh35K5tTQP6rLtJUHCj4KKJxbInSepOL5t5H2M4phUJiBMAHBan7Wx7IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_RD6A-j6J3eU5eetjK2CntsJOOaCkKDlQOy4oWK441DhokK6bB-Kjd5tjSKbjAJf5V26Jc3M04X-o9-hvT-54e2p3FBUQjST6zQft20b3bhMJmXJQaK6b9aJ7jWhvdhl72y-crQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCHJ5DOJJFe_Ivt-5rDHJTg5DTjhPrM5fjTWMT-MTryKKJayRKbj4OzBnOaM-t_WlrPBRIfBanRhlRNB-3iV-OxDUvnyxAZ-ntL2xQxtNRJVnRj0MchHRj9XU6obUPUXa59LUvLX2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtD8KbKLCDT83-RJH-xQ0KnLXKKOLVKnGHl7ketn4hUt25qF8jU6e2lRZ-Cb23xcXQlT0Mp72QhrdQf4WWb3ebTJr32Qr-JO6HR6psIJM557SbUtl5f5KhURZaKviah4-BMb1Df7DBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6jyDGAqtjtJfKresJoq2RbhKROvhjRYj50gyxoObtRxtTTk0C3_-b6rqtjd-PQA2qLP2GJ9LU3kBgT9LMnx--t58h3_Xhjj3IuDQttjQn0OaIvmht5tK4ncOR7TyURdDx47yMcd0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OuJRQ2QJ8BtC85hDQP; BCLID=10948395599364217531; BCLID_BFESS=10948395599364217531; BDRCVFR[C0p6oIjvx-c]=mk3SLVN4HKm; ZD_ENTRY=baidu; ab_sr=1.0.1_ZjNlY2E0OGFkZDI2YTgzNDIxYzY4YjAyMzc0OTg4ZTQyOTA0Y2I1ODE1ODc4OGI3N2ViNWUwZjMxZDkzYTI4NjBkMTUzN2Q2YzAyZmNmMWYxZjU1ZjYxZmY5N2NkOWI1Y2VkMTkxZmQxZmI1MTBiNTk2ZGVlYjU2YWY0Yjk0NzUyZDQzMWQ3Mjg3NGQ3NzQxMjQzZTM4MjE4NzBjZDIzYjRkNzM4ZTM4MTljNGEyNTBjNWRkMWM0MThmMDk2NWMz; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=37543_36545_37551_37359_37395_37406_36789_37534_37497_26350_22158; H_PS_645EC=9f5caE30vB1jLqilvNexRNN9bOcbZcX%2FA1Xnz0HxDV%2BuoPEwp6V4y9zuqNV0%2F1fnjhZd",
        "Host": "www.baidu.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    url = 'https://www.baidu.com/s?rtt=4&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word=阿里巴巴'
    res = requests.get(url, headers=headers).text

    p_href = '<h3 class="news-title_1YtI1 "><a href="(.*?)"'
    href = re.findall(p_href, res)  # 获取新闻链接
    p_title = '<h3 class="news-title_1YtI1 ">.*?><!--s-text-->(.*?)<!--/s-text--></a>'
    title = re.findall(p_title, res, re.S)  # 获取新闻标题
    p_date = '<span class="c-color-gray2 c-font-normal c-gap-right-xsmall" aria-label=".*?>(.*?)</span>'
    date = re.findall(p_date, res)  # 获取新闻时间
    p_source = '<span class="c-color-gray" aria-label=".*?>(.*?)</span>'
    source = re.findall(p_source, res)  # 获取新闻来源

    for i in range(len(title)):  # 获取到的标题因为有关键字标签标出，二次处理
        title[i] = title[i].replace('<em>', "")
        title[i] = title[i].replace('</em>', "")
        title[i] = title[i].replace('\u200b', "")
        # print(title[i])
    now = datetime.datetime.now().strftime("%Y-%m-%d %H%M%S")
    name = "news_report(按时间顺序) " + str(now) + ".txt"
    with open(name, "w") as f:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write('报告生成与数据爬取时间：' + str(now))
        f.write("\n")
        for i in range(10):
            string_temp = str(i + 1) + ". " + title[i] + "    新闻来源:" + source[i] + "\n" + \
                          href[i]

            f.write(string_temp)
            f.write("\n")
    f.close()
    print("按时间爬取百度新闻完成！")

def exact_page_scratch(page_num):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "BIDUPSID=B6EA7C9B05DAB3C37B715A2AB92BD08B; PSTM=1629100955; BD_UPN=12314753; __yjs_duid=1_bbe39be9ba12597a6659dac18a1b797c1629101225013; BDUSS=JHdnJDVTJnc1RTVkF-S1NmNkdST0o4MFJobFd5Ykt6aTVxYWQ2TUV2Z2h2YlZpSUFBQUFBJCQAAAAAAAAAAAEAAADK2ualc3VubnnJscbGwMcwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACEwjmIhMI5iR2; BDUSS_BFESS=JHdnJDVTJnc1RTVkF-S1NmNkdST0o4MFJobFd5Ykt6aTVxYWQ2TUV2Z2h2YlZpSUFBQUFBJCQAAAAAAAAAAAEAAADK2ualc3VubnnJscbGwMcwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACEwjmIhMI5iR2; H_WISE_SIDS_BFESS=107313_110085_127969_131861_168388_176398_177985_178384_178530_178605_179345_179448_180276_181106_181398_181588_181709_182000_182243_182531_182663_183030_183223_183328_183536_183611_184010_184246_184267_184319_184735_184809_184892_185029_185037_185268_185519_185726_185873_185879_186039_186206_186313_186317_186411_186446_186558_186597_186636_186644_186665_186841_186898_187022_187062_187086_187188_187214_187282_187292_187326_187356_187421_187488_187533_187643_187828_187912_187928_187965_188049_8000055_8000116_8000125_8000139_8000144_8000153_8000173_8000178_8000182_8000186; MCITY=-175%3A; BAIDUID=CBA8C0900DFE4F7D7EC6354456675F9B:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=2k0kag8480050g81218l2ed01hkkb0e1b; ZFY=6ZYqElvxkR3JrX:B1wjGFYSkEbLTgDbwRrsqc5uOBfU0:C; BAIDUID_BFESS=CBA8C0900DFE4F7D7EC6354456675F9B:FG=1; delPer=0; BD_CK_SAM=1; PSINO=1; COOKIE_SESSION=5_0_7_9_2_13_0_3_7_9_1_0_67403_0_0_0_1665804446_0_1665805326%7C9%231636_441_1665403138%7C9; shifen[1616972_91638]=1665805331; BDSFRCVID=M44OJexroG0uYe7jsm_qqhcaZyUIz7OTDYLEOwXPsp3LGJLVcW-mEG0Pt8lgCZubaxOJogKKL2OTHm_F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=M44OJexroG0uYe7jsm_qqhcaZyUIz7OTDYLEOwXPsp3LGJLVcW-mEG0Pt8lgCZubaxOJogKKL2OTHm_F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJAHVILKtK-3H48k-4QEbbQH-UnLqMo3bmOZ04n-ah02ffTNjP65hqRQKf725lT8Qm5E_h7m3UTdsq76Wh35K5tTQP6rLtJUHCj4KKJxbInSepOL5t5H2M4phUJiBMAHBan7Wx7IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_RD6A-j6J3eU5eetjK2CntsJOOaCkKDlQOy4oWK441DhokK6bB-Kjd5tjSKbjAJf5V26Jc3M04X-o9-hvT-54e2p3FBUQjST6zQft20b3bhMJmXJQaK6b9aJ7jWhvdhl72y-crQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCHJ5DOJJFe_Ivt-5rDHJTg5DTjhPrM5fjTWMT-MTryKKJayRKbj4OzBnOaM-t_WlrPBRIfBanRhlRNB-3iV-OxDUvnyxAZ-ntL2xQxtNRJVnRj0MchHRj9XU6obUPUXa59LUvLX2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtD8KbKLCDT83-RJH-xQ0KnLXKKOLVKnGHl7ketn4hUt25qF8jU6e2lRZ-Cb23xcXQlT0Mp72QhrdQf4WWb3ebTJr32Qr-JO6HR6psIJM557SbUtl5f5KhURZaKviah4-BMb1Df7DBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6jyDGAqtjtJfKresJoq2RbhKROvhjRYj50gyxoObtRxtTTk0C3_-b6rqtjd-PQA2qLP2GJ9LU3kBgT9LMnx--t58h3_Xhjj3IuDQttjQn0OaIvmht5tK4ncOR7TyURdDx47yMcd0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OuJRQ2QJ8BtC85hDQP; H_BDCLCKID_SF_BFESS=tJAHVILKtK-3H48k-4QEbbQH-UnLqMo3bmOZ04n-ah02ffTNjP65hqRQKf725lT8Qm5E_h7m3UTdsq76Wh35K5tTQP6rLtJUHCj4KKJxbInSepOL5t5H2M4phUJiBMAHBan7Wx7IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_RD6A-j6J3eU5eetjK2CntsJOOaCkKDlQOy4oWK441DhokK6bB-Kjd5tjSKbjAJf5V26Jc3M04X-o9-hvT-54e2p3FBUQjST6zQft20b3bhMJmXJQaK6b9aJ7jWhvdhl72y-crQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCHJ5DOJJFe_Ivt-5rDHJTg5DTjhPrM5fjTWMT-MTryKKJayRKbj4OzBnOaM-t_WlrPBRIfBanRhlRNB-3iV-OxDUvnyxAZ-ntL2xQxtNRJVnRj0MchHRj9XU6obUPUXa59LUvLX2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtD8KbKLCDT83-RJH-xQ0KnLXKKOLVKnGHl7ketn4hUt25qF8jU6e2lRZ-Cb23xcXQlT0Mp72QhrdQf4WWb3ebTJr32Qr-JO6HR6psIJM557SbUtl5f5KhURZaKviah4-BMb1Df7DBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6jyDGAqtjtJfKresJoq2RbhKROvhjRYj50gyxoObtRxtTTk0C3_-b6rqtjd-PQA2qLP2GJ9LU3kBgT9LMnx--t58h3_Xhjj3IuDQttjQn0OaIvmht5tK4ncOR7TyURdDx47yMcd0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OuJRQ2QJ8BtC85hDQP; BCLID=10948395599364217531; BCLID_BFESS=10948395599364217531; BDRCVFR[C0p6oIjvx-c]=mk3SLVN4HKm; ZD_ENTRY=baidu; ab_sr=1.0.1_ZjNlY2E0OGFkZDI2YTgzNDIxYzY4YjAyMzc0OTg4ZTQyOTA0Y2I1ODE1ODc4OGI3N2ViNWUwZjMxZDkzYTI4NjBkMTUzN2Q2YzAyZmNmMWYxZjU1ZjYxZmY5N2NkOWI1Y2VkMTkxZmQxZmI1MTBiNTk2ZGVlYjU2YWY0Yjk0NzUyZDQzMWQ3Mjg3NGQ3NzQxMjQzZTM4MjE4NzBjZDIzYjRkNzM4ZTM4MTljNGEyNTBjNWRkMWM0MThmMDk2NWMz; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=37543_36545_37551_37359_37395_37406_36789_37534_37497_26350_22158; H_PS_645EC=9f5caE30vB1jLqilvNexRNN9bOcbZcX%2FA1Xnz0HxDV%2BuoPEwp6V4y9zuqNV0%2F1fnjhZd",
        "Host": "www.baidu.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    temp_num = page_num * 10
    temp_num = str(temp_num)
    url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word=阿里巴巴&pn=' + temp_num
    res = requests.get(url, headers=headers,timeout=10).text

    p_href = '<h3 class="news-title_1YtI1 "><a href="(.*?)"'
    href = re.findall(p_href, res)  # 获取新闻链接
    p_title = '<h3 class="news-title_1YtI1 ">.*?><!--s-text-->(.*?)<!--/s-text--></a>'
    title = re.findall(p_title, res, re.S)  # 获取新闻标题
    p_date = '<span class="c-color-gray2 c-font-normal c-gap-right-xsmall" aria-label=".*?>(.*?)</span>'
    date = re.findall(p_date, res)  # 获取新闻时间
    p_source = '<span class="c-color-gray" aria-label=".*?>(.*?)</span>'
    source = re.findall(p_source, res)  # 获取新闻来源

    for i in range(len(title)):  # 获取到的标题因为有关键字标签标出，二次处理
        title[i] = title[i].replace('<em>', "")
        title[i] = title[i].replace('</em>', "")
        title[i] = title[i].replace('\u200b', "")
        # print(title[i])
    now = datetime.datetime.now().strftime("%Y-%m-%d %H%M%S")
    name = "news_report(多页爬取,第" + str(page_num+1) + "页) " + str(now) + ".txt"
    with open(name, "w") as f:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write('报告生成与数据爬取时间：' + str(now))
        f.write("\n")
        for i in range(10):
            string_temp = str(i + 1+page_num*10) + ". " + title[i] + "    新闻来源:" + source[i] + "\n" + \
                          href[i]

            f.write(string_temp)
            f.write("\n")
    f.close()
    print("阿里巴巴第"+str(page_num+1)+"页百度新闻获取完成！")

def multi_page_scartch(page_num):
    for i in range(page_num):
        exact_page_scratch(i)

def main():
    download()
    select_date_and_source()  #获取新闻时间和来源并写入文件
    select_title_and_id()     #获取新闻标题和网址并写入文件
    news_and_report()         #批量获取公司的百度新闻并生成报告
    #Error_and_24()            #异常处理与24小时实时获取新闻并生成报告
    time_scratch()            #按时间排序爬取百度新闻
    multi_page_scartch(2)     #爬取前两页，参数可自由设定,第10个设定超时时间已在代码中体现
    pass

if __name__ =="__main__":
    main()