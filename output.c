
//------------------------ Code in C ------------------------//

#include <stdio.h>
#include <stdlib.h>

typedef struct Check{
	int z;
} Check;

Check* Check_init(struct Check* self) {
	if (self == NULL) {
		self = (Check*) malloc(sizeof(Check));
	}
	
	self->z = 0;
	return self;
	return self;
}

void Check_not_test(struct Check* self, int x) {
	if (!(x > 5)) {
		printf("%d\n", 1);
	} else {
		printf("%d\n", 0);
	}
}

void Check_and_test(struct Check* self, int x, int y) {
	if ((x > 5 && y > 5)) {
		printf("%d\n", 1);
	} else {
		printf("%d\n", 0);
	}
}

void Check_or_test(struct Check* self, int x, int y) {
	if ((x > 5 || y > 5)) {
		printf("%d\n", 1);
	} else {
		printf("%d\n", 0);
	}
}

void Check_overloading_test(struct Check* self, int x) {
	printf("%d\n", x);
}

void Check_overloading_test_2(struct Check* self, int x, int y) {
	printf("%d, %d\n", x, y);
}

void Check_input_test(struct Check* self) {
	scanf("%d", &self -> z);
	printf("%d\n", self->z);
}

void Check_double_if_test(struct Check* self, int x) {
	if (x > 5) {
		if (x < 15) {
			printf("%d\n", x);
		} else {
			printf("%d\n", 0);
		}
	} else {
		printf("%d\n", 0);
	}
}

void Check_while_if_test(struct Check* self, int x) {
	while (x > 5) {
		if (x < 10) {
			x = x+ 1;
			printf("%d\n", x);
		} else {
			x = 0;
		}
	}
}

int main(){
	struct Check* c;
	int in;
	printf("%d\n", 1111);
	c = Check_init(NULL);
	Check_input_test(c);
	printf("%d\n", 1111);
	Check_not_test(c, 6);
	printf("%d\n", 1111);
	Check_and_test(c, 6, 4);
	Check_and_test(c, 6, 7);
	printf("%d\n", 1111);
	Check_or_test(c, 6, 4);
	Check_or_test(c, 3, 4);
	printf("%d\n", 1111);
	Check_overloading_test(c, 6);
	Check_overloading_test_2(c, 6, 7);
	printf("%d\n", 1111);
	Check_double_if_test(c, 7);
	Check_double_if_test(c, 3);
	printf("%d\n", 1111);
	Check_while_if_test(c, 6);
	
	return 0;
}