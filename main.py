#Setup Game
info.player1.set_score(0)
info.player1.set_life(3)
#Create Character
running_man = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . f f f f f f . . . . .
    . . . . f 1 1 1 1 1 1 f . . . .
    . . . b f 1 1 f 1 f 1 f b . . .
    . . b . f 1 1 f 1 f 1 f . b . .
    . . b . f 1 1 1 1 1 1 f . b . .
    . . . b b f f f f f f . . b . .
    . . b b b f 2 2 2 2 f . f b f f
    . . b b b f 2 2 2 2 f f c c c c
    . . c c c f 2 2 2 2 f f c f f f
    . . . c c f 2 2 2 2 f f c f . .
    . . . . c f f f f f f . f . . .
    . . . . . f . . . . f . . . . .
    . . . . . f . . . . f . . . . .
    . . . . . f . . . . f . . . . .
    . . . . . f . . . . f . . . . .
"""))
running_man.ay = 200
scene.camera_follow_sprite(running_man)

#create tileset
tiles.set_tilemap(tilemap("""level"""))
scene.set_background_color(6)
#create gravity and jump
canDoublejump = True
controller.move_sprite(running_man ,50, 0) 
def on_jump():
   global canDoublejump
   if running_man.is_hitting_tile(CollisionDirection.BOTTOM) or canDoublejump:
       running_man.vy = -100
       canDoublejump = running_man.is_hitting_tile(CollisionDirection.BOTTOM)
controller.player1.on_button_event(ControllerButton.A,ControllerButtonEvent.PRESSED,on_jump)
#Create enemies

#Create projectiles




