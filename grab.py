import load
site = (900, 700)
print(load.confirm_color(site[0]-10,site[0]+10,site[1]))
print(load.get_color(site[0], site[1]))

site1 = (900, 400)
print(load.get_color(site1[0], site1[1]))

site2 = (250, 370)
print(load.get_color(site2[0], site2[1]))



'''import image
bound = (415, 495, 565, 535)
name = '芯片搜索二.png'
image.grab_image(bound).save('D:/明日方舟/脚本/pic/' + name)'''