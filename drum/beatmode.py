import pygame
from pygame import mixer
import grid


class win:
	pygame.init()
	#dimensions
	WIDTH = 1200
	HEIGHT = 650
	screen = pygame.display.set_mode([WIDTH, HEIGHT],pygame.RESIZABLE)
	pygame.display.set_caption('Beat Mode')
	label_font = pygame.font.Font('rambling.ttf', 32)
	medium_font = pygame.font.Font('rambling.ttf', 24)
	
	
	fps = 60
	index = 100
	beats = 8
	timer = pygame.time.Clock()
	instruments = 6
	boxes = []
	clicked = [[-1 for _ in range(beats)] for _ in range(instruments)] #checks all numbers of beats and instruments and sets them all -1 or off
	active_list = [1 for _ in range(instruments)]
	bpm = 240
	playing = True
	active_length = 0
	active_beat = 1
	beat_changed = True
	save_menu = False
	load_menu = False
	saved_beats = []
	file = open('log.txt', 'r')
	for line in file:
		saved_beats.append(line)

	beat_name = ''
	typing = False
	pygame.mixer.set_num_channels(instruments * 3)
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

	run = True
	while run:
		timer.tick(fps)
		screen.fill(black)

		boxes = draw_grid(clicked,  active_beat, active_list)
		#lower menu buttons
		play_pause = pygame.draw.rect(screen, gray, [30, HEIGHT -150, 180, 100], 0, 5)
		play_text = label_font.render('Play/Pause', True, white)
		screen.blit(play_text, (50, HEIGHT - 130))
		if playing:
			play_text2 = medium_font.render('Playing', True, dark_gray)
		else:
			play_text2 = medium_font.render('Paused', True, dark_gray)
		screen.blit(play_text2, (70, HEIGHT - 100))

		#bpm stuff
		bpm_rect = pygame.draw.rect(screen, gray, [240, HEIGHT - 150, 200, 100], 5, 5)
		bpm_text = medium_font.render('Beats Per Minute', True, white)
		screen.blit(bpm_text, (248, HEIGHT -130))
		bpm_text2 = label_font.render(f'{bpm}', True, white)
		screen.blit(bpm_text2, (310, HEIGHT -100))
		bpm_add_rect = pygame.draw.rect(screen, gray, [450, HEIGHT - 150, 48, 48], 0, 5)
		bpm_sub_rect = pygame.draw.rect(screen, gray, [450, HEIGHT - 100, 48, 48], 0, 5)
		add_text = medium_font.render('+5', True, white)
		sub_text = medium_font.render('-5', True, white)
		screen.blit(add_text, (460, HEIGHT - 140))
		screen.blit(sub_text, (460, HEIGHT - 90))

		#beats stuff
		beats_rect = pygame.draw.rect(screen, gray, [530, HEIGHT - 150, 180, 100], 5, 5)
		beats_text = medium_font.render('Beats In Loop', True, white)
		screen.blit(beats_text, (548, HEIGHT -130))
		beats_text2 = label_font.render(f'{beats}', True, white)
		screen.blit(beats_text2, (600, HEIGHT -100))
		beats_add_rect = pygame.draw.rect(screen, gray, [720, HEIGHT - 150, 48, 48], 0, 5)
		beats_sub_rect = pygame.draw.rect(screen, gray, [720, HEIGHT - 100, 48, 48], 0, 5)
		add_text2 = medium_font.render('+1', True, white)
		sub_text2 = medium_font.render('-1', True, white)
		screen.blit(add_text2, (730, HEIGHT - 140))
		screen.blit(sub_text2, (730, HEIGHT - 90))

		#instrument rects and select instrument
		instrument_rects = []
		for i in range(instruments):
			rect = pygame.rect.Rect((0, i * 80), (200, 100))
			instrument_rects.append(rect)

		#save and load files
		save_button = pygame.draw.rect(screen, gray, [790, HEIGHT - 150, 170, 48], 0, 5)
		save_text = label_font.render('Save Beat', True, white)
		screen.blit(save_text,(810, HEIGHT - 140))
		load_button = pygame.draw.rect(screen, gray, [790, HEIGHT - 100, 170, 48], 0, 5)
		load_text = label_font.render('Load Beat', True, white)
		screen.blit(load_text,(810, HEIGHT - 90))

		#clear board
		clear_button = pygame.draw.rect(screen, gray, [990, HEIGHT -150, 180, 100], 0, 5)
		clear_text = label_font.render('Clear Board', True, white)
		screen.blit(clear_text, (1000, HEIGHT-120))

		if save_menu:
			exit_button, saving_button, beat_name, entry_rect = draw_save_menu(beat_name, typing)
		if load_menu:
			exit_button, loading_button, entry_rect, delete_button, loaded_information = draw_load_menu(index)

		if beat_changed:
			play_notes()
			beat_changed = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN and not save_menu and not load_menu:
				for i in range(len(boxes)):
					if boxes[i][0].collidepoint(event.pos):
						coords = boxes[i][1]
						clicked[coords[1]][coords[0]] *= -1
			if event.type == pygame.MOUSEBUTTONUP and not save_menu and not load_menu:
				if play_pause.collidepoint(event.pos) :
					if playing:
						playing = False
					elif not playing:
						playing = True
				elif bpm_add_rect.collidepoint(event.pos):
					bpm += 5
				elif bpm_sub_rect.collidepoint(event.pos):
					bpm -= 5

				elif beats_add_rect.collidepoint(event.pos):
					beats += 1
					for i in range(len(clicked)):
						clicked[i].append(-1)

				elif beats_sub_rect.collidepoint(event.pos):
					beats -= 1
					for i in range(len(clicked)):
						clicked[i].pop(-1)
				elif clear_button.collidepoint(event.pos):
					clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]

				elif save_button.collidepoint(event.pos):
					save_menu = True
				elif load_button.collidepoint(event.pos):
					load_menu = True

				for i in range(len(instrument_rects)):
					if instrument_rects[i].collidepoint(event.pos):
						active_list[i] *= -1

			elif event.type == pygame.MOUSEBUTTONUP:
				if exit_button.collidepoint(event.pos):
					save_menu = False
					load_menu = False
					playing = True
					beat_name= ''
					typing = False
				if entry_rect.collidepoint(event.pos):
					if save_menu:
						if typing:
							typing = False
						else:
							typing = True
					if load_menu:
						index = (event.pos[1] - 100) // 50

				if save_menu:
					if saving_button.collidepoint(event.pos):
						file = open('log.txt', 'w')
						saved_beats.append(f'\nname: {beat_name}, beats: {beats}, bpm:{bpm}, selected:{clicked}')
						for i in range(len(saved_beats)):
							file.write(str(saved_beats[i]))
						file.close()
						save_menu = False
						load_menu = False
						typing = False
						beat_name = ''
				if load_menu:
					if delete_button.collidepoint(event.pos):
						if 0 <= index < len(saved_beats):
							saved_beats.pop(index)
					if loading_button.collidepoint(event.pos):
						if 0 <= index <len(saved_beats):
							beats = loaded_information[0]
							bpm = loaded_information[1]
							clicked = loaded_information[2]
							index = 100
							save_menu = False
							load_menu = False
							playing = True
							typing = False
				
			if event.type == pygame.TEXTINPUT and typing:
				beat_name += event.text 
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE and len(beat_name) > 0 and typing:
					beat_name = beat_name[:-1]

		beat_length = 3600 // bpm

		if playing:
			if active_length < beat_length:
				active_length += 1
			else:
				active_length = 0
				if active_beat < beats - 1:
					active_beat +=1
					beat_changed = True
				else:
					active_beat = 0
					beat_changed = True
		pygame.display.flip()

	pygame.quit()
