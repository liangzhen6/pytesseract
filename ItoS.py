# -*- coding: utf-8 -*-
try:
	import Image
except ImportError:
	from PIL import Image,ImageEnhance
import pytesseract
import PIL.ImageOps

rep={'O':'0', #替换列表
 'I':'1','L':'1', 'Z':'2', 'S':'8' };
def initTable(threshold=140): 
# 二值化函数
	table = []
	for i in range(256): 
		if i < threshold: 
			table.append(0) 
		else: 
			table.append(1) 
	
	return table


image = Image.open('zw08.jpeg')
w, h = image.size
print(w,h)
image = image.convert('L') #将彩色图片转换成灰度图片
# image = PIL.ImageOps.invert(image) #反转图片的值
image = ImageEnhance.Contrast(image) #增强对比度
contrast = 3.0
image = image.enhance(contrast)
# image = image.point(initTable(), '1') #3.降噪，图片二值化

image.show()
# image.save('thumbnail.jpg', 'jpeg')


# chi_sim 简体中文 chi_tra 繁体中文
print(pytesseract.image_to_string(image, lang='chi_sim+eng'))