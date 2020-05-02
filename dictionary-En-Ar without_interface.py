#by www.angle47.com
dicEnAr={"good":"جيد",
         "hello":"مرحبا",
         "today":"اليوم",
         "angle":"زاوية",
         "Mosque":"مسجد"
}
word = input("أدخل الكلمة التي تريد ترجمتها: ")
try:
    print("ترجمة كلمة {} للعربية هي : {}".format(word, dicEnAr[word]))
except:
    print("عذرا، لم نجد الكلمة التي تبحث عنها في قاموسنا")
