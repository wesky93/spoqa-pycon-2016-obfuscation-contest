"""
훈민정음 유니코드
    난독 코드를 만들기 위한 유니코드 추출기 및 추출된 유니코드 입니다.
    코드 해독시 사전처럼 참고하시면 유용합니다.
"""
# 유니코드 추출 위한 코드
def 유니코드추출기(a):
    훈민정음 = []
    for i in a:
        훈민정음.append(ord(i))
    return "''.join([chr(x) for x in "+str(훈민정음)+"])"


# 솅〮조ᇰ
''.join([chr(x) for x in [49541, 12334, 51312, 4592]])

# 훈〮민져ᇰ〮ᅙᅳᆷ
''.join([chr(x) for x in [4355, 54984, 12334, 48124, 51256, 4592, 12334, 4441, 4467, 4535]])
''.join([chr(x) for x in [int(str(x).replace('0','4')) for x in ['50980', '08120', '0360', '0055', '0592', '12330', '0001', '0067', '0535']]])

# 훈〮민져ᇰ〮ᅙᅳᆷ:
''.join([chr(x) for x in [4355, 54984, 12334, 48124, 51256, 4592, 12334, 4441, 4467, 4535, 58]])
''.join([chr(x) for x in [int(str(x).replace('0','4')) for x in ['50980', '08120', '0360', '0055', '0592', '12330', '0001', '0067', '0535','58']]])
# 잘못된 문자가 있노리
''.join([chr(x) for x in [51096, 47803, 46108, 32, 47928, 4365, 4510, 4540, 12334, 50752, 12334, 32, 51079, 45432, 45768, 12334]])

# 훈민정음:문자가 있노리
''.join([chr(x) for x in [int(str(x).replace('0','4')) for x in ['50980', '08120', '0360', '0055', '0592', '12330', '0001', '0067', '0535','58']]+[47928, 4365, 4510, 4540, 12334, 50752, 12334, 32, 51079, 45432, 45768, 12334]])

# 나랏〮말〯ᄊᆞ미〮
''.join([chr(x) for x in [45208, 46991, 12334, 47568, 12335, 4362, 4510, 48120]])

# 젼ᄎᆞ / '까닭'의 옛말
''.join([chr(x) for x in [45208, 46991, 12334, 47568, 12335, 4362, 4510, 48120]])


# 듀ᇰ귁〮에〮달아〮
''.join([chr(x) for x in [4355, 4466, 4592, 44481, 12334, 50640, 12334, 45804, 50500, 12334]])
# 문ᄍᆞᆼ〮와〮로〮서르ᄉᆞᄆᆞᆺ디〮아니〮ᄒᆞᆯᄊᆡ〮
''.join([chr(x) for x in [47928, 4365, 4510, 4540, 12334, 50752, 12334, 47196, 12334, 49436, 47476, 4361, 4510, 4358, 4510, 4538, 46356, 12334, 50500, 45768, 12334, 4370, 4510, 4527, 4362, 4513, 12334]])
# 이〮런젼ᄎᆞ〮로〮어린〮ᄇᆡᆨ셔ᇰ〮이〮니르고〮져〮호ᇙ〮배〮이셔〮도〮
# ᄆᆞᄎᆞᆷ〮내〯제ᄠᅳ〮들〮시러〮펴디〮몯〯ᄒᆞᇙ노〮미〮하니〮라〮
# 내〮이〮ᄅᆞᆯ〮윙〮ᄒᆞ〮야〮어〯엿비〮너겨〮
# 새〮로〮스〮믈〮여듧〮ᄍᆞᆼ〮ᄅᆞᆯ〮ᄆᆡᇰᄀᆞ〮노니〮
# 사〯ᄅᆞᆷ마〯다〮ᄒᆡ〯ᅇᅧ〮수〯ᄫᅵ〮니겨〮날〮로〮ᄡᅮ〮메〮뼌安ᅙᅡᆫ킈〮ᄒᆞ고〮져〮ᄒᆞᇙᄯᆞᄅᆞ미〮니라〮

# print(
''.join([chr(x) for x in [112, 114, 105, 110, 116, 40]])

# ''.join
''.join([chr(x) for x in [34, 34, 46, 106, 111, 105, 110]])

# format
''.join([chr(x) for x in [102, 111, 114, 109, 97, 116]])

# lambda
''.join([chr(x) for x in [108, 97, 109, 98, 100, 97]])

# sys.exit()
''.join([chr(x) for x in [115, 121, 115, 46, 101, 120, 105, 116, 40, 41]])

# sys.argv[1]
''.join([chr(x) for x in [115, 121, 115, 46, 97, 114, 103, 118, 91, 49, 93]])

# try:
''.join([chr(x) for x in [116, 114, 121, 58]])

# except:
''.join([chr(x) for x in [101, 120, 99, 101, 112, 116, 58]])

# 1443
''.join([chr(x) for x in [49, 52, 52, 51]])
