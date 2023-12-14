#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <ctype.h>
#include <assert.h>
#include <string.h>

int main(){
	FILE *fp = fopen("input", "r");

	char GREEN_STR[10] = "green", BLUE_STR[10] = "blue", RED_STR[10] = "red";
	
	// We implement a FSM
	enum state {Game, ID, number, color} state = Game;
	/* We start at state.
	 *
	 * The possible transitions are 
	 * Game -> ID -> number -> color -> number
	 * 			    `-> Game
	 *
	 * */
	enum COLORS{NONE, RED, GREEN, BLUE} COLORS;
	int max_red = 12, max_green = 13, max_blue = 14;
	int current_red = 0, current_green = 0, current_blue = 0;

	uint64_t solution = 0;

	int c, current_ID = 0, current_number = 0, current_color = 0;
	char color_string[20], col_str_len = 0;
	int current_game_possible = 1;
	while(!feof(fp)){
		c = fgetc(fp);

		current_color = NONE;
//		printf("%c - %d\n", c, state);
		switch(state){
			case Game:
				// nothing to do
				printf("%c\n", c);
				if(c == ' ') state = ID;
				break;
			case ID:
				// We read numbers until the end
				if(isdigit(c)) current_ID = current_ID * 10 + (c - '0');
				if(c == ':') state = number;
				break;
			case number:
				// We read numbers until the end
				if(isdigit(c)){
					current_number = current_number * 10 + (c-'0');
				}
				if(c == ' ' && current_number != 0){
					printf("Game ID is %d - %d ", current_ID, current_number);
					state = color;
				}
				break;
			case color:
				// we form a word reading character by character until 
				if(c == ','){
					color_string[col_str_len++] = 0;
					printf("\n%s\n", color_string);
					if(strcmp(color_string, BLUE_STR) == 0){
						current_blue += current_number;
					}else if(strcmp(color_string, RED_STR) == 0){
						current_red += current_number;
					}else if(strcmp(color_string, GREEN_STR) == 0){
						current_green += current_number;
					}
					printf("added %d cubes of color %s\n", current_number, color_string);
					col_str_len = 0;
					current_number = 0;
					state = number;
				}
				else if(c == ';'){
					color_string[col_str_len++] = 0;
					printf("%s cubes\n", color_string);
					// we read a whole word, so we go ahead and check whether this is possible
					if(strcmp(color_string, BLUE_STR) == 0){
						current_blue += current_number;
					}else if(strcmp(color_string, RED_STR) == 0){
						current_red += current_number;
					}else if(strcmp(color_string, GREEN_STR) == 0){
						current_green += current_number;
					}
					printf("added %d cubes of color %s\n", current_number, color_string);

					printf("%d %d %d\n", current_red, current_blue, current_green);
					if(current_red > max_red || current_blue > max_blue || current_green > max_green){
						current_game_possible = 0;
					}

					printf("new set is coming\n");
					current_red = current_blue = current_green = 0;

					state = number;
					current_number = 0;
					col_str_len = 0;
				}
				else if(c == '\n'){
					color_string[col_str_len++] = 0;
					printf("%s cubes.", color_string);
					// we read a whole word, so we go ahead and check whether this is possible
					if(strcmp(color_string, BLUE_STR) == 0){
						current_blue += current_number;
					}else if(strcmp(color_string, RED_STR) == 0){
						current_red += current_number;
					}else if(strcmp(color_string, GREEN_STR) == 0){
						current_green += current_number;
					}

					if(current_red > max_red || current_blue > max_blue || current_green > max_green)
						current_game_possible = 0;
					
					current_red = current_blue = current_green = 0;

					state = number;
					current_number = 0;
					printf(" This game has finished.\n");

					int64_t old = solution;

					if(current_game_possible) solution += current_ID;
					else printf("\tNevertheless, it is not possible \n");
					
					printf("============== old solution was %ld - new is %ld\n", old, solution);

					current_game_possible = 1;
					state = Game;
					current_number = 0;
					col_str_len = 0;
					current_ID = 0;
				}
				else color_string[col_str_len++] = c;	
				break;
			default:
				break;
		}
		if(!current_game_possible) state = color;
	}
	printf("solution is %ld\n", solution);
	return 0;
}
