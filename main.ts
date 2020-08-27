// Setup Game
info.player1.setScore(0)
info.player1.setLife(3)
// Create Character
let running_man = sprites.create(img`
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
`)
running_man.ay = 200
scene.cameraFollowSprite(running_man)
// create tileset
tiles.setTilemap(tilemap`level`)
scene.setBackgroundColor(0)
// create gravity and jump
let canDoublejump = true
controller.moveSprite(running_man, 50, 0)
controller.player1.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function on_jump() {
    
    if (running_man.isHittingTile(CollisionDirection.Bottom) || canDoublejump) {
        running_man.vy = -100
        canDoublejump = running_man.isHittingTile(CollisionDirection.Bottom)
    }
    
})
