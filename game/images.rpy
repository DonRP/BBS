# Gui
image icon ann = "/icon_ann.webp"
image icon jenny = "/icon_jenny.webp"
image icon liza = "/icon_liza.webp"
image icon lucy = "/icon_lucy.webp"

# Emo
image side annemo 00 = "/emo/Anna00.webp"
image side annemo 01 = "/emo/Anna01.webp"
image side annemo 02 = "/emo/Anna02.webp"
image side annemo 03 = "/emo/Anna03.webp"
image side annemo 04 = "/emo/Anna04.webp"
image side mcemo 00 = "/emo/Bobby00.webp"
image side mcemo 01 = "/emo/Bobby01.webp"
image side mcemo 02 = "/emo/Bobby02.webp"
image side mcemo 03 = "/emo/Bobby03.webp"
image side mcemo 04 = "/emo/Bobby04.webp"
image side mcemo 05 = "/emo/Bobby05.webp"
image side mcemo 06 = "/emo/Bobby06.webp"
image side mcemo 07 = "/emo/Bobby07.webp"
image side mcemo 08 = "/emo/Bobby08.webp"
image side mcemo 09 = "/emo/Bobby09.webp"
image side mcemo 10 = "/emo/Bobby10.webp"
image side mcemo 11 = "/emo/Bobby11.webp"
image side mcemo 12 = "/emo/Bobby12.webp"
image side mcemo 13 = "/emo/Bobby13.webp"
image side lizemo 00 = "/emo/Liza00.webp"
image side lizemo 01 = "/emo/Liza01.webp"
image side lizemo 02 = "/emo/Liza02.webp"
image side lizemo 03 = "/emo/Liza03.webp"
image side lizemo 04 = "/emo/Liza04.webp"
image side lizemo 05 = "/emo/Liza05.webp"
image side lizemo 06 = "/emo/Liza06.webp"
image side lizemo 07 = "/emo/Liza07.webp"
image side lizemo 08 = "/emo/Liza08.webp"
image side lizemo 09 = "/emo/Liza09.webp"
image side lcyemo 00 = "/emo/Lucy00.webp"
image side lcyemo 01 = "/emo/Lucy01.webp"
image side lcyemo 02 = "/emo/Lucy02.webp"
image side lcyemo 03 = "/emo/Lucy03.webp"
image side lcyemo 04 = "/emo/Lucy04.webp"
image side lcyemo 05 = "/emo/Lucy05.webp"
image side lcyemo 06 = "/emo/Lucy06.webp"
image side lcyemo 07 = "/emo/Lucy07.webp"

## Icon
# location
image icon mcroom = "location/mcroom-icon.webp"
image icon lizaroom = "location/lizaroom-icon.webp"
image icon livingroom = "location/livingroom-icon.webp"
image icon kitchen = "location/kitchen-icon.webp"

image icon mcroom a = im.MatrixColor("location/mcroom-icon.webp", im.matrix.brightness(-0.5))
image icon lizaroom a = im.MatrixColor("location/lizaroom-icon.webp", im.matrix.brightness(-0.5))
image icon livingroom a = im.MatrixColor("location/livingroom-icon.webp", im.matrix.brightness(-0.5))
image icon kitchen a = im.MatrixColor("location/kitchen-icon.webp", im.matrix.brightness(-0.5))

## Background
# location
image bg mcroom = "location/mcroom-[tm.image_time].webp"
image bg lizaroom = "location/lizaroom-[tm.image_time].webp"
image bg lizaroom 0 blur = im.Blur("location/lizaroom-0.webp", 7)
image bg livingroom = "location/livingroom-[tm.image_time].webp"
image bg kitchen = "location/kitchen-[tm.image_time].webp"

# Anna
image bg AnnaDream A01 = Movie(play="/Anna-Dream/A01.webm", loop=True, size=(gui.width, gui.height))
image bg AnnaDream A02A animated:
    "/Anna-Dream/A02C.webp" with dissolve
    pause 1
    "/Anna-Dream/A02A.webp" with dissolve
    pause 1
    "/Anna-Dream/A02B.webp" with dissolve
    pause 1
    "/Anna-Dream/A02A.webp" with dissolve
    pause 1
    "/Anna-Dream/A02B.webp" with dissolve
    pause 1
    "/Anna-Dream/A02A.webp" with dissolve
    pause 1
    "/Anna-Dream/A02B.webp" with dissolve
    pause 1
    "/Anna-Dream/A02A.webp" with dissolve
    pause 1
    "/Anna-Dream/A02B.webp" with dissolve
    pause 1
    "/Anna-Dream/A02A.webp" with dissolve
    pause 1
    "/Anna-Dream/A02B.webp" with dissolve
    pause 1
    "/Anna-Dream/A02A.webp" with dissolve
    pause 1
    "/Anna-Dream/A02B.webp" with dissolve
    pause 1
    "/Anna-Dream/A02A.webp" with dissolve
    pause 1
    repeat
image bg AnnaDream A02B animated:
    "/Anna-Dream/A02A.webp" with dissolve
    pause 0.7
    "/Anna-Dream/A02B.webp" with dissolve
    pause 0.7
    repeat
image bg AnnaDream A02C = "/Anna-Dream/A02C.webp"
image bg AnnaMCRoom A01A = "/Anna-MCRoom/A01A.webp"
image bg AnnaMCRoom A01B = "/Anna-MCRoom/A01B.webp"
image bg AnnaMCRoom A01C = "/Anna-MCRoom/A01C.webp"
image bg AnnaMCRoom A01D = "/Anna-MCRoom/A01D.webp"
image bg AnnaMCRoom A02A = "/Anna-MCRoom/A02A.webp"
image bg AnnaMCRoom A02B = "/Anna-MCRoom/A02B.webp"
image bg AnnaMCRoom A02C = "/Anna-MCRoom/A02C.webp"
image bg AnnaMCRoom A03A = "/Anna-MCRoom/A03A.webp"
image bg AnnaMCRoom A03B = "/Anna-MCRoom/A03B.webp"
image bg AnnaMCRoom A03C = "/Anna-MCRoom/A03C.webp"
image bg AnnaMCRoom A03D = "/Anna-MCRoom/A03D.webp"
image bg AnnaMCRoom A04A = "/Anna-MCRoom/A04A.webp"
image bg AnnaMCRoom A04B = "/Anna-MCRoom/A04B.webp"
image bg AnnaMCRoom A04C = "/Anna-MCRoom/A04C.webp"
# Booby
image bg Bobby A00 = "/Bobby/A00.webp"
image bg Bobby A01 = "/Bobby/A01.webp"
image bg Bobby A02 = "/Bobby/A02.webp"
image bg Bobby A03 = "/Bobby/A03.webp"
image bg Bobby A04 = "/Bobby/A04.webp"
image bg Bobby A05 = "/Bobby/A05.webp"
image smartphone bobby liza = "/Bobby/smartphone_liza.webp"
# Liza
image bg LizaKitchen A00 = "/Liza-Kitchen/A00.webp"
image bg LizaKitchen A01 = "/Liza-Kitchen/A01.webp"
image bg LizaKitchen A01B = "/Liza-Kitchen/A01B.webp"
image bg LizaKitchen A02 = "/Liza-Kitchen/A02.webp"
image bg LizaKitchen A03 = "/Liza-Kitchen/A03.webp"
image bg LizaKitchen A04A = "/Liza-Kitchen/A04A.webp"
image bg LizaKitchen A04B = "/Liza-Kitchen/A04B.webp"
image bg LizaKitchen A05 = "/Liza-Kitchen/A05.webp"
image bg LizaKitchen A07 = "/Liza-Kitchen/A07.webp"
image bg LizaKitchen A08A = "/Liza-Kitchen/A08A.webp"
image bg LizaKitchen A08B = "/Liza-Kitchen/A08B.webp"
image bg LizaKitchen A08C = "/Liza-Kitchen/A08C.webp"
image bg LizaKitchen A08D = "/Liza-Kitchen/A08D.webp"
image bg LizaKitchen A08E = "/Liza-Kitchen/A08E.webp"
image bg LizaKitchen A08F = "/Liza-Kitchen/A08F.webp"
image bg LizaKitchen A08G = "/Liza-Kitchen/A08G.webp"
image bg LizaKitchen A09 = "/Liza-Kitchen/A09.webp"
image item LizaKitchen B banana = "/Liza-Kitchen/B0C.webp"
image item LizaKitchen B ananas = "/Liza-Kitchen/B0B.webp"
image item LizaKitchen B kiwi = "/Liza-Kitchen/B0A.webp"
image bg LizaLizaRoom A00 = "/Liza-LizaRoom/A0[fable_minigame_score].webp"
image bg LizaLizaRoom A04 = "/Liza-LizaRoom/A04.webp"
image bg LizaLizaRoom A05 = "/Liza-LizaRoom/A05.webp"
image bg LizaLizaRoom A06 = "/Liza-LizaRoom/A06.webp"
image bg LizaLizaRoom B01A = "/Liza-LizaRoom/B01A.webp"
image bg LizaLizaRoom B01 animated:
    "/Liza-LizaRoom/B01B.webp" with dissolve
    pause 1
    "/Liza-LizaRoom/B01C.webp" with dissolve
    pause 1
    repeat
image bg LizaLizaRoom B01B = "/Liza-LizaRoom/B01B.webp"
image bg LizaLizaRoom B01D = "/Liza-LizaRoom/B01D.webp"
image bg LizaLizaRoom B01E = "/Liza-LizaRoom/B01E.webp"
image bg LizaLizaRoom B02 animated:
    "/Liza-LizaRoom/B02A.webp" with dissolve
    pause 0.7
    "/Liza-LizaRoom/B02B.webp" with dissolve
    pause 0.7
    repeat
image bg LizaLizaRoom B02 fast animated:
    "/Liza-LizaRoom/B02A.webp" with dissolve
    pause 0.5
    "/Liza-LizaRoom/B02B.webp" with dissolve
    pause 0.5
    repeat
image bg LizaLizaRoom B02C = "/Liza-LizaRoom/B02C.webp"

# Lucy
image bg LucyLivingroom A01A = "/Lucy-Livingroom/A01A.webp"
image bg LucyLivingroom A01B = "/Lucy-Livingroom/A01B.webp"
image bg LucyLivingroom A01C = "/Lucy-Livingroom/A01C.webp"
image bg LucyLivingroom A02 = "/Lucy-Livingroom/A02.webp"
image bg LucyLivingroom A03 = "/Lucy-Livingroom/A03.webp"
image bg LucyLivingroom A04A = "/Lucy-Livingroom/A04A.webp"
image bg LucyLivingroom A04B = "/Lucy-Livingroom/A04B.webp"
image bg LucyLivingroom A05 = "/Lucy-Livingroom/A05.webp"
image bg LucyLivingroom A06 = "/Lucy-Livingroom/A06.webp"
image bg LucyLivingroom A07 = "/Lucy-Livingroom/A07.webp"
image bg LucyLivingroom A07A = "/Lucy-Livingroom/A07A.webp"
image bg LucyLivingroom A08 = "/Lucy-Livingroom/A08-[fable_minigame_score].webp"
image bg LucyLivingroom A08 2 = "/Lucy-Livingroom/A08-2.webp"
image bg LucyLivingroom A11 = "/Lucy-Livingroom/A11.webp"
image bg LucyLivingroom A12 = "/Lucy-Livingroom/A12.webp"
image bg LucyLivingroom A13A = "/Lucy-Livingroom/A13A.webp"
image bg LucyLivingroom A13B = "/Lucy-Livingroom/A13B.webp"
