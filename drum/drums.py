import pygame
from pygame import mixer

pygame.init()

#dimensions
WIDTH = 1200
HEIGHT = 650

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

screen = pygame.display.set_mode([WIDTH, HEIGHT],pygame.RESIZABLE)
pygame.display.set_caption('Beat Mode')
label_font = pygame.font.Font('rambling.ttf', 32)
medium_font = pygame.font.Font('rambling.ttf', 24)

fps = 60
index = 100
timer = pygame.time.Clock()
beats = 8
instruments = 6
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)] #checks all number of beats and instruments and sets them all-1 or off
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

#wav sounds import /beat notes
hi_hat = mixer.Sound('808Samples\hi hat.wav')
snare = mixer.Sound('808Samples\snare.wav')
kick = mixer.Sound('808Samples\kick.wav')
bass = mixer.Sound('808Samples\\bass.wav')
clap = mixer.Sound('808Samples\clap.wav')
tom = mixer.Sound('808Samples\\tom.wav')
cymbal = mixer.Sound('808Samples\cymbal.wav')

pygame.mixer.set_num_channels(instruments * 3)

#load beat notes
def play_notes():
	for i in range(len(clicked)):
		if clicked[i][active_beat] == 1 and active_list[i] == 1:
			if i == 0:
				hi_hat.play()
			if i == 1:
				snare.play()
			if i == 2:
				kick.play()
			if i == 3:
				bass.play()
			if i == 4:
				clap.play()
			if i == 5:
				tom.play()
		


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

def draw_save_menu(beat_name, typing):
	pygame.draw.rect(screen, black, [0, 0, WIDTH, HEIGHT])
	menu_text = label_font.render('SAVE MENU: Enter a Name for the Beat', True, white)
	saving_btn = pygame.draw.rect(screen, gray, [WIDTH // 2 - 150, HEIGHT * 0.75, 350, 100], 0, 5)
	saving_text = label_font.render('Save Beat', True, white)
	screen.blit(saving_text, (WIDTH // 2 -50, HEIGHT * 0.75 + 30))
	screen.blit(menu_text, (370, 40))
	exit_btn = pygame.draw.rect(screen, gray, [WIDTH - 180, HEIGHT - 100, 150, 90], 0, 5)
	exit_text = label_font.render('Close', True, white)
	screen.blit(exit_text, (WIDTH - 140, HEIGHT - 70))
	if typing:
		pygame.draw.rect(screen, dark_gray, [340, 200, 600, 200], 0, 5)
	entry_rect = pygame.draw.rect(screen, gray, [340, 200, 600, 200], 5, 5)
	entry_text = label_font.render(f'{beat_name}', True, white)
	screen.blit(entry_text, (370, 250))
	return exit_btn, saving_btn, beat_name, entry_rect

def draw_load_menu(index):
	loaded_clicked = []
	loaded_beats = 0
	loaded_bpm = 0
	pygame.draw.rect(screen, black, [0, 0, WIDTH, HEIGHT])
	menu_text = label_font.render('LOAD MENU: Select a Beat to Load', True, white)
	loading_btn = pygame.draw.rect(screen, gray, [WIDTH // 2 - 150, HEIGHT * 0.75, 350, 100], 0, 5)
	loading_text = label_font.render('Load Beat', True, white)
	screen.blit(loading_text, (WIDTH // 2 -50, HEIGHT * 0.75 + 30))
	delete_btn = pygame.draw.rect(screen, gray, [WIDTH//2 - 500, HEIGHT * .75, 200, 100], 0, 5)
	delete_text = label_font.render('Delete Beat', True, white)
	screen.blit(delete_text, ((WIDTH//2) - 485, HEIGHT *.75 + 30))
	screen.blit(menu_text, (370, 40))
	exit_btn = pygame.draw.rect(screen, gray, [WIDTH - 180, HEIGHT - 100, 150, 90], 0, 5)
	exit_text = label_font.render('Close', True, white)
	screen.blit(exit_text, (WIDTH - 140, HEIGHT - 70))
	
	if 0 <= index < len(saved_beats):
		pygame.draw.rect(screen, light_gray, [190, 100 + index * 50, 800, 50])
	for beat in range(len(saved_beats)):
		if beat < 10:
			beat_clicked = []
			row_text = medium_font.render(f'{beat + 1}', True, white)
			screen.blit(row_text, (200, 100 + beat * 50))
			name_index_start = saved_beats[beat].index('name: ') + 6
			name_index_end = saved_beats[beat].index(', beats:')
			name_text = medium_font.render(saved_beats[beat][name_index_start:name_index_end], True, white)
			screen.blit(name_text, (240, 100 + beat * 50))
		if 0 <= index < len(saved_beats) and beat == index:
			beats_index_end = saved_beats[beat].index(', bpm:')
			loaded_beats = int(saved_beats[beat][name_index_end + 8: beats_index_end])
			bpm_index_end = saved_beats[beat].index(', selected:')
			loaded_bpm = int(saved_beats[beat][beats_index_end + 6: bpm_index_end])
			loaded_clicks_string = saved_beats[beat][bpm_index_end + 14: -3]
			loaded_clicks_rows = list(loaded_clicks_string.split('], ['))
			for row in range(len(loaded_clicks_rows)):
				loaded_clicks_row = (loaded_clicks_rows[row].split(', '))
				for item in range(len(loaded_clicks_row)):
					if loaded_clicks_row[item] == '1' or loaded_clicks_row[item] == '-1':
						loaded_clicks_row[item] = int(loaded_clicks_row[item])
				beat_clicked.append(loaded_clicks_row)
				loaded_clicked = beat_clicked
	loaded_info = [loaded_beats, loaded_bpm, loaded_clicked]
	entry_rect = pygame.draw.rect(screen, gray, [190, 90, 800, 400], 5, 5)
	return exit_btn, loading_btn, entry_rect, delete_btn, loaded_info
#add a replace or not function to save a loaded file or save changes else save as a new file 

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

# file = open('saved_beats.txt', 'w')
# for i in range(len(saved_beats)):
# 	file.write(str(saved_beats[i]))
#file.close()
pygame.quit()