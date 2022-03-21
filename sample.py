from googletrans import Translator
 
tr = Translator()
result = tr.translate("hello", src="en", dest="ja").text
print(result)