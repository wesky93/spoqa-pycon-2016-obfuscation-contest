import sys
"""
 프로그램명 : 훈〮민져ᇰ〮ᅙᅳᆷ
 부제 : 計發者誤音 / 개발자가 계산기를 만들때 해선 알될 짓

 해설(나랏말씀이 예약어와 달라 백성이 이해지 못하므로 따로 설명을 합니다, ~사실 저도 못알아먹겠어요..~)

     eval() = 훈〮민져ᇰ〮ᅙᅳᆷ()
     "" = _
     lambda x,y : y(x) = 솅〮조ᇰ(x,y)
     '"".join([chr(x) for x in {}])'.formet(x) = 나랏〮말〯ᄊᆞ미(x)
     print() = 듀ᇰ귁〮에〮달아〮()
     eval(eval('"".join([chr(x) for x in {}])'.formet(x))) = 문ᄍᆞᆼ〮와〮로〮서르ᄉᆞᄆᆞᆺ디〮아니〮ᄒᆞᆯᄊᆡ〮
     sys.argv[1] = 이〮런젼ᄎᆞ〮로〮어린〮ᄇᆡᆨ셔ᇰ〮이〮니르고〮져〮호ᇙ〮배〮이셔〮도〮
     유니코드'훈민정음:' = 내〮이〮ᄅᆞᆯ〮윙〮ᄒᆞ〮야〮어〯엿비〮너겨
     유니코드'잘못된 문자가 잇노리' = 새〮로〮스〮믈〮여듧〮ᄍᆞᆼ〮ᄅᆞᆯ〮ᄆᆡᇰᄀᆞ〮노니
     1443 = 사〯ᄅᆞᆷ마〯다〮ᄒᆡ〯ᅇᅧ〮수〯ᄫᅵ〮니겨〮날〮로〮ᄡᅮ〮메〮뼌安ᅙᅡᆫ킈〮ᄒᆞ고〮져〮ᄒᆞᇙᄯᆞᄅᆞ미〮니라

"""
훈〮민져ᇰ〮ᅙᅳᆷ = lambda x : eval(x);_ = "";
솅〮조ᇰ = lambda x,y,z : "lambda {0} : {1}{0}{2}".format(x,y,z)


나랏〮말〯ᄊᆞ미〮 = lambda x : '\"\".join([chr(x) for x in {}])'.format(x)
듀ᇰ귁〮에〮달아〮 = 훈〮민져ᇰ〮ᅙᅳᆷ( 솅〮조ᇰ('임금',훈〮민져ᇰ〮ᅙᅳᆷ(나랏〮말〯ᄊᆞ미〮([112, 114, 105, 110, 116, 40])),')'))
문ᄍᆞᆼ〮와〮로〮서르ᄉᆞᄆᆞᆺ디〮아니〮ᄒᆞᆯᄊᆡ〮 = 훈〮민져ᇰ〮ᅙᅳᆷ( 솅〮조ᇰ('衮職','훈〮민져ᇰ〮ᅙᅳᆷ(훈〮민져ᇰ〮ᅙᅳᆷ(나랏〮말〯ᄊᆞ미〮(',")))"))
이〮런젼ᄎᆞ〮로〮어린〮ᄇᆡᆨ셔ᇰ〮이〮니르고〮져〮호ᇙ〮배〮이셔〮도〮 = 문ᄍᆞᆼ〮와〮로〮서르ᄉᆞᄆᆞᆺ디〮아니〮ᄒᆞᆯᄊᆡ〮([115, 121, 115, 46, 97, 114, 103, 118, 91, 49, 93])
ᄆᆞᄎᆞᆷ〮내〯제ᄠᅳ〮들〮시러〮펴디〮몯〯ᄒᆞᇙ노〮미〮하니〮라 = [int(str(x).replace('0','4')) for x in ['50980', '08120', '0360', '0055', '0592', '12330', '0001', '0067', '0535','58']]
내〮이〮ᄅᆞᆯ〮윙〮ᄒᆞ〮야〮어〯엿비〮너겨 = [int(str(x).replace('0','4')) for x in ['50980', '08120', '0360', '0055', '0592', '12330', '0001', '0067', '0535','58']]
새〮로〮스〮믈〮여듧〮ᄍᆞᆼ〮ᄅᆞᆯ〮ᄆᆡᇰᄀᆞ〮노니 = [51096, 47803, 46108, 32, 47928, 4365, 4510, 4540, 12334, 50752, 12334, 32, 51079, 45432, 45768, 12334]
사〯ᄅᆞᆷ마〯다〮ᄒᆡ〯ᅇᅧ〮수〯ᄫᅵ〮니겨〮날〮로〮ᄡᅮ〮메〮뼌安ᅙᅡᆫ킈〮ᄒᆞ고〮져〮ᄒᆞᇙᄯᆞᄅᆞ미〮니라 = 1443
나갸 = 훈〮민져ᇰ〮ᅙᅳᆷ(나랏〮말〯ᄊᆞ미〮([115, 121, 115, 46, 101, 120, 105, 116, 40, 41]))


try:
    듀ᇰ귁〮에〮달아〮(훈〮민져ᇰ〮ᅙᅳᆷ(이〮런젼ᄎᆞ〮로〮어린〮ᄇᆡᆨ셔ᇰ〮이〮니르고〮져〮호ᇙ〮배〮이셔〮도〮))
except:
    import warnings as 젼ᄎᆞ
    듀ᇰ귁〮에〮달아〮(사〯ᄅᆞᆷ마〯다〮ᄒᆡ〯ᅇᅧ〮수〯ᄫᅵ〮니겨〮날〮로〮ᄡᅮ〮메〮뼌安ᅙᅡᆫ킈〮ᄒᆞ고〮져〮ᄒᆞᇙᄯᆞᄅᆞ미〮니라);문ᄍᆞᆼ〮와〮로〮서르ᄉᆞᄆᆞᆺ디〮아니〮ᄒᆞᆯᄊᆡ〮([45208, 46991, 12334, 47568, 12335, 4362, 4510, 48120]).warn(훈〮민져ᇰ〮ᅙᅳᆷ(나랏〮말〯ᄊᆞ미〮(내〮이〮ᄅᆞᆯ〮윙〮ᄒᆞ〮야〮어〯엿비〮너겨 + 새〮로〮스〮믈〮여듧〮ᄍᆞᆼ〮ᄅᆞᆯ〮ᄆᆡᇰᄀᆞ〮노니)))
finally:
    훈〮민져ᇰ〮ᅙᅳᆷ(나갸)
