#include <stdlib.h>
#include <ctype.h>
#include <stdio.h>
#include <assert.h>
#include <stdint.h>

int main(){
	
	FILE * fp = fopen("input", "r");
	char line[200];
	void * success;
	line[199] = 0;

	uint32_t first, last;
	uint64_t old = 0;
	uint64_t solution = 0;
		
	success = fgets(line, 199, fp);
	printf("success is %x", success);

	while(success != NULL){
		old = solution;
		
		first = -1;
		last  = -1;

		char *c = line;
		printf("line is %s\n", line);
		while(*c != 0){
			printf("%c ", *c);
			if( isdigit(*c) ){
				if(first == -1) first = *c - '0';
				last = *c - '0';
			}
			printf("first: %d - last: %d\n", first, last);
			c++;
		}

		first = first*10 + last;
		solution += first;
		printf("solution was %ld, then we summed %d and now it is %d\n", old, first, solution);
		assert(solution >= old);
		success = fgets(line, 199, fp);
	}

	printf("Solution is %ld\n", solution);
	return 0;
}
