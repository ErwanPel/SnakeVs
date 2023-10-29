if event.type == pygame.KEYDOWN:
    if event.key == K_UP:
        snake.direction = "TOP"
    if event.key == K_DOWN:
        snake.direction = "DOWN"
    if event.key == K_RIGHT:
        snake.direction = "RIGHT"
    if event.key == K_LEFT:
        snake.direction = "LEFT"


