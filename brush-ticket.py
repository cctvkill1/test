# -*- coding: utf-8 -*-
import urllib2
import urllib 
from multiprocessing.dummy import Pool as ThreadPool
from threading import Thread
 

def postHttp(i): 
	name                 = urllib.quote('我日') 
	url                  = 'https://hd.ysfaisco.cn/ajax/hdgame_h.jsp?cmd=setMbPlayerVotes&aid=11590276&gameId=1&openId='+i+'&style=49&name='+name+'&playerId=10604&otherPlayerId=6860'
	header               = {}
	header['User-Agent'] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 MicroMessenger/5.0.1' 
	request              = urllib2.Request(url,headers=header)
	response             = urllib2.urlopen(request)
	result               = response.read()
	result               = result.strip()
	print result

if __name__ == '__main__':
	openid_list = ["oHRvawPnAW3RIxAElC8EKHtyCl1Y", "oHRvawA-pq-3dL3WkVAwOFM4y4Ss", "oHRvawLEo_hYamjiHGK_QFxr3vRU", "oHRvawBVAuoD1AqeK_ptmU9QqTU0", "oHRvawMGC7M97rHf-IS68odntdY8", "oHRvawE-wN6Ju7Qt9RWBOxWrogck", "oHRvawKHhGo8aNMRGd4HrF75x7bg", "oHRvawDQGSsGGjiCgvJCts0lXmQQ", "oHRvawG1jWXDaC5fNx4GOgroHepk", "oHRvawF-06-oX6yPOh65vWU0ORwM", "oHRvawByQkdkqcQdPjLT9TxXwXSc", "oHRvawDH1o82EfC_LFAt9W-l9olU", "oHRvawPfwBSC59WpDPlxIiGGVb6w", "oHRvawCPx4jbjrPi3jL2etQBMu7M", "oHRvawHgyW3DS8YNs44k0pCLspPk", "oHRvawDifKhMsHnWUiyrX6saAAdA", "oHRvawPyQbRCHNpQkFOn3_XLcc6E", "oHRvawNyKI-CSTeJP5o3G_46_Xww", "oHRvawOHjbl5xCJciA6fHNqmzQMo", "oHRvawEP6seYQw9C47gL6PHSFn0Q", "oHRvawI3summPXydFMLO46axcG-c", "oHRvawHhGSI-KvkagqOsztoxPfLc", "oHRvawCALKFm1_YgwpgrEaJ_Twq8", "oHRvawJwaHE__eV69PpS79-mAqEk", "oHRvawCRcdBEtG_0D6HHTUc6_X6k", "oHRvawOrvvdOjgVD9QSZ0trElJKM", "oHRvawPr0tPe7CTf2DXdaG_CDdv0", "oHRvawACRyrjIwC5THma5KBVhvA4", "oHRvawHsSLmvRslxC9PC6TX0FbPU", "oHRvawFNfDbRJM4DbIx4IDu6cngU", "oHRvawEX-eNOX44o7LT9zPMYJ9j0", "oHRvawPBnASXJnqY-2VVYpmnlMEU", "oHRvawKy-RW-8Q0sLcst5bY2kA_8", "oHRvawMaIy8Q4H0qBb7nP8Yy3olQ", "oHRvawI9btgFpo7S3Jqw31x-UeoQ", "oHRvawPLpqEFli7diR0QXCdbSR20", "oHRvawASK0KTR7venPHHsXbZJCJo", "oHRvawIT3HBMlY5ZH9oT2fjS7_e4", "oHRvawMaoaXJC5AlS_Rh59n9hlb8", "oHRvawODU7wOWORip_38sizUda_I", "oHRvawHfYM0eHTwieeVEOcoCgkXk", "oHRvawAqCBY5LBCL897-xVOGtEgw", "oHRvawHwu3ekeyrC9Y1GKixkNDqQ", "oHRvawJEjULKo711VQM7H_IG0Eo8", "oHRvawA5o_8Olo8tan5AEJv3SyDE", "oHRvawLHh_n-BTu9G-B0XOzi7eyA", "oHRvawFzkPfjbfX9P-sF04EDd4tc", "oHRvawAvcfeCNHHqi42cjkxwGQ_w", "oHRvawKGiht7E0ooJr1k1LowHesA", "oHRvawBEw0-33b8BJGWlzGQAbbGs", "oHRvawJhRz_VlsHK-SQzYcN05BXM", "oHRvawOPPgmNvjlxHkQ5RcIQRYts", "oHRvawFD2TRk1PAxIZ-mWlpjMKdM", "oHRvawMCd3Q_DSxGgbXYLeU76tTI", "oHRvawOxrhLb2O8Nav_Wu_i5B8g4", "oHRvawOLSfQKRn_zNowgdGD45mew", "oHRvawLgXcCrLQUj2qhuN-7EU4nA", "oHRvawPSsBuHNXiiff_R2jJHJ3xU", "oHRvawN0S5-9al2X70oBxjUjqRWY", "oHRvawKKFywMNfNURTfDcq2ec5wE", "oHRvawDAzdiZzZz5wYUSH27esKxU", "oHRvawCAVxf1u3i0rN62Webn4RKg", "oHRvawDW7htenhAyzVItYrZ6Idec", "oHRvawFZtr5qmR_-XXm2Fb8zkbIA", "oHRvawHCVPt-m9snFkzrQ4rQodh0", "oHRvawDYgh1_0snMXVKcaSYOqc6g", "oHRvawLXic5Qt3C6G-TuheoxturQ", "oHRvawLijvw8ILfQAw3utTy7ppOA", "oHRvawH2auViUvHdBRkL6D3bumpU", "oHRvawBLeZ0MGu2-uUUsAyElFCWE", "oHRvawPhr4x3Vp_A0DJ9k_XA9WV4", "oHRvawCqRp91-1_odIlEetc6m9L4", "oHRvawBsZffzjANt7JCR7NKB9hTM", "oHRvawAnKxvCxqLFl_Vjg5NqSxY0", "oHRvawPLEpkc-MoGFaSoEuVBNTyc", "oHRvawFHxKXFBOtKWIpiBf0qyXiA", "oHRvawLkC4KcghW1S950J2k6NDAQ", "oHRvawM9aahiJtRKkTMDvXb2d8sI", "oHRvawJ_1VBkCdXb8XlBdywOoDoU", "oHRvawITcJLg-pjkl1xRIZi-Iz_Q", "oHRvawDVhDGf2t50Qk-qh3Zd8Wgc"]  
	# postHttp()
	total = len(openid_list)
	page_pool = ThreadPool(total)  	 
	page_pool.map_async(postHttp, (openid_list))
	page_pool.close()
	page_pool.join() 