dic={
    1:".",
    11:",",
    111:"?",

    2:"a",
    22:"b",
    222:"c",

    3:"d",
    33:"e",
    333:"f",

    4: "g",
    44:"h",
    444:"i",

    5:"j",
    55:"k",
    555:"l",

    6:"m",
    66:"n",
    666:"o",
    78:"",
    7:"p",
    77:"q",
    777:"r",
    7777:"s",

    8:"t",
    88:"u",
    888:"v",

    9:"w",
    99:"x",
    999:"y",
    9999:"z"
}
mykey=list(dic.keys()) # 111 22 33 55 777
myvalue=list(dic.values()) # a b c d e


def sifreyapici(sifre):
    listex = [] # şifrenin tutulduğu liste
    listem = list(sifre)  # şifremiz

    for harf in listem:
        positon = myvalue.index(harf)
        listex.append(str(mykey[positon]) + "0")
        print(mykey[positon], end="0")
def sifrecozucu(cozulecekSifre):

  # gelen şifreyi önce sıfırlardan arındıralım
    cozulmusSifreSayilari = cozulecekSifre.split("0")
    for temp in cozulmusSifreSayilari:
        if (temp != ""):
            konum = mykey.index(int(temp))
            print(myvalue[konum], end="")

sifreyapici("merhababugunpazartesi")
print()
#sifrecozucu("60330777044020220202208804088066070209999020777080330777704440")

