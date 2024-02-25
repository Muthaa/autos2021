#color schemes
black = (0, 0, 0)
white = (255, 255, 255)
lightgray = (128, 128, 128)
light_gray = (170, 170, 170)
gray = (120, 120, 120)
dark_gray= (50, 50, 50)
neonblue = (0, 255, 255)
blue = (0, 128, 128)
green = (0, 255, 0)
gold = (212, 175, 55)

def draw_grid(clicks, beat, actives):
	#window division for menu and column
	left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 165], 5)
	bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT - 170, WIDTH, 200], 5)

	boxes = []
	colors = [gray, white, gray]

	#draw instrument nav bar
	hi_hat_text = label_font.render('Hi Hat', True, colors[actives[0]])
	screen.blit(hi_hat_text, (30, 30))
	snare_text = label_font.render('Snare', True, colors[actives[1]])
	screen.blit(snare_text, (30, 110))
	kick_text = label_font.render('Kick Drum', True, colors[actives[2]])
	screen.blit(kick_text, (30, 190))
	bass_text = label_font.render('Bass', True, colors[actives[3]])
	screen.blit(bass_text, (30, 270))
	clap_text = label_font.render('Clap', True, colors[actives[4]])
	screen.blit(clap_text, (30, 350))
	floor_text = label_font.render('Floor Tom', True, colors[actives[5]])
	screen.blit(floor_text, (30, 430))

	for i in range(instruments):
		pygame.draw.line(screen, gray, (0, (i * 80) + 80), (200, (i * 80) + 80), 3)

	#beats side division
	for i in range(beats):
		for j in range(instruments):
			if clicks[j][i] == -1:
				color = gray
			else:
				if actives[j] == 1:
					color = blue
				else:
					color = dark_gray

			rect = pygame.draw.rect(screen, color, [i * ((WIDTH - 200) // beats) + 200, (j * 80) + 5, 
				((WIDTH- 200) // beats) - 10, ((HEIGHT - 155) // instruments) - 10], 0, 3)

			pygame.draw.rect(screen, gold, [i * ((WIDTH - 200) // beats) + 200, (j * 80), 
				((WIDTH- 200) // beats), ((HEIGHT - 155) // instruments)], 5, 5)

			pygame.draw.rect(screen, black, [i * ((WIDTH - 200) // beats) + 200, (j * 80), 
				((WIDTH- 200) // beats), ((HEIGHT - 155) // instruments)], 2, 5)
			boxes.append((rect, (i, j)))

		#beat point scroller
		active = pygame.draw.rect(screen, neonblue, [beat * ((WIDTH - 200) // beats) + 200, 0,
		 ((WIDTH -200) // beats), instruments * 80], 5, 3)
	return boxes