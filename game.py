import pygame  #Nhập thư viện
import sys
import random
import winsound
import math

pygame.init() #Khởi tạo thư viện
pygame.display.set_caption("Lái tàu vũ trụ")    #Cài title
screen = pygame.display.set_mode((480,360))     #Cài kích thước cửa sổ

Ship_img= pygame.image.load("img/rocketship.png") #Tải hình ảnh 
pygame.display.set_icon(Ship_img)  #Thiết lập hình ảnh làm icon cửa sô

bg_galaxy = pygame.image.load("img/bg_galaxy.png") #Tải ảnh nền

meteoroid = pygame.image.load("img/meteoroid.png") #Tải ảnh thiên thạch lên


#Thiết lập tọa độ ban đầu cho tàu vũ trụ
ship_x=220
ship_y=280

#Theo dõi sự thay đổi tọa độ x khi tàu di chuyển
x_change=0

#Lấy chiều rộng của con tàu
ship_withd =Ship_img.get_width()

#Lấy chiều rộng thiên thạch
meteoroid_withd=meteoroid.get_width()

#Thiết lập tọa độ cho thiên thạch
meteoroid_x=random.randint(0,480 - meteoroid_withd )
meteoroid_y=0

#Tạo biến điểm
score=0
score_text=pygame.font.SysFont("Arial",24)

#Tạo biến game over
Over_text=pygame.font.SysFont("Arial",38)

game_over=False

#Hàm reset game
def reset_game():
    global ship_x,ship_y,x_change,meteoroid_x,meteoroid_y,score,game_over
    ship_x = 220
    ship_y = 280
    x_change = 0
    meteoroid_x = random.randint(0,480 - meteoroid_withd)
    meteoroid_y = 0
    score=0
    game_over = False
    
 
while True:
    for event in pygame.event.get():    #Dùng for để duyệt qua các event nhận được
        if event.type == pygame.QUIT: #kiểm tra nếu envent là type QUIT
            pygame.quit() #Thoát chương trình
            sys.exit()
            
        if event.type == pygame.KEYDOWN: #Nếu nhận event phím được ấn xuống
            if event.key == pygame.K_LEFT: #Nếu là phím mũi tên trái
                x_change -=3 #x_change giảm 5 để tàu dịch chuyển sang trái 
            elif event.key == pygame.K_RIGHT:
                x_change +=3  #x_change tăng lên 5 để tàu dịch chuyển sang phải
                
        if event.type == pygame.KEYUP: #Nếu không ấn phím nữa
            x_change = 0 #x_change nhận giá trị 0, con tàu không dịch chuyển
        
    if not game_over:
        ship_x+=x_change #Liện tục cập nhật tọa độ x của tàu
        meteoroid_y+=1.7 #Thiết lập tốc độ rơi của thiên thạch
    
        if ship_x<0: #giới hạn vị trí của tàu ở biên trái của cửa sổ.
            ship_x=0 
            
        elif ship_x > 480 - ship_withd: #giới hạn vị trí của tàu ở biên phải của cửa sổ (kích thước cửa sổ trừ đi chiều rộng của tàu).
            ship_x=480 - ship_withd
    
        if meteoroid_x>480 - meteoroid_withd: #Kiểm tra nếu thiên thạch random ở tọa độ lớn hơn 480 - độ rộng thiên thạch
            meteoroid_x=480 - meteoroid_withd
        
        if meteoroid_y>360: #Kiểm tra nếu thiên thạch đã chạy hết tọa độ y
            meteoroid_y=0   #Đặt lại tọa độ
            meteoroid_x = random.randint(0, 480) #Thiết lập vị trí ngẫu nhiên của thiên thạch trên trục tọa độ x
            score+=1 #Tăng điểm lên 1
            winsound.PlaySound("sound/Magic Spell.wav",winsound.SND_ASYNC) #Them sound mỗi lần tăng điểm
    
        distance = math.sqrt((ship_x -  meteoroid_x)**2 + (ship_y - meteoroid_y)**2) #Tính khoảng cách giữa 2 điểm trên tọa độ
        
        if distance < 40: #Kiểm tra khoảng cách của 2 điểm nếu nhỏ hơn 40 thì kết thúc game
            winsound.PlaySound("sound/explosion.wav", winsound.SND_ASYNC)
            game_over = True
            
    else:
        screen.fill((0,0,0)) #Reset lại màn hình và hiển thị thông báo game over
        over_render = Over_text.render("Game Over. Press R to continue.",True,(255,0,0))
        screen.blit(over_render,(15,140))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_r]:
            reset_game()
        continue
          
    screen.blit(bg_galaxy, (0,0)) #Vẽ ảnh nền tại tọa độ 0,0
    
   
    screen.blit(Ship_img, (ship_x,ship_y)) #Vẽ ảnh tàu vũ trụ
    #Hiển thị điểm số
    score_render = score_text.render("Score: "+str(score),True,(255,255,255))
    screen.blit(score_render,(5,0)) #Vẽ ảnh điểm số 
    
    screen.blit(meteoroid,(meteoroid_x,meteoroid_y)) #vẽ ảnh thiên thạch
    pygame.display.update() #Cập nhật màn hình để hiển thị thay đổi

