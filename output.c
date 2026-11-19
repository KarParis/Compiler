
//------------------------ Code in C ------------------------//

#include <stdio.h>
#include <stdlib.h>

typedef struct Shape{
	int x, y;
	int color;
} Shape;

Shape* Shape_init(struct Shape* self, int x, int y) {
	if (self == NULL) {
		self = (struct Shape*) malloc(sizeof(struct Shape));
	}
	
	self->x = x;
	self->y = y;
	return self;
}

Shape* Shape_init_2(struct Shape* self, int x, int y, int color) {
	if (self == NULL) {
		self = (struct Shape*) malloc(sizeof(struct Shape));
	}
	
	self->x = x;
	self->y = y;
	self->color = color;
	return self;
}

void Shape_move(struct Shape* self, int dx, int dy) {
	self->x = self->x+ dx;
	self->y = self->y+ dy;
	if (self->x>=1) {
		self->y = self->y+ 1;
	} else {
		self->y = self->y- 1;
	}
	while (dx>2) {
		self->y = 0;
	}
}

void Shape_move_2(struct Shape* self, int dx) {
	self->x = self->x+ dx;
}

void Shape_inputs(struct Shape* self, int x, int y) {
	scanf("%d", &x);
	scanf("%d", &self -> x);
	scanf("%d", &y);
	scanf("%d", &self -> y);
}

void Shape_set_x(struct Shape* self, int x) {
	self->x = x;
}

int Shape_get_x(struct Shape* self) {
	return self->x;
}

typedef struct Circle{
	int x;
	int y;
	int color;
	int radius;
} Circle;

Circle* Circle_init(struct Circle* self, int radius) {
	if (self == NULL) {
		self = (struct Circle*) malloc(sizeof(struct Circle));
	}
	
	self->radius = radius;
	return self;
}

Circle* Circle_init_2(struct Circle* self, int x, int y, int color, int radius) {
	if (self == NULL) {
		self = (struct Circle*) malloc(sizeof(struct Circle));
	}
	
	self->x = x;
	self->y = y;
	self->color = color;
	self->radius = radius;
	return self;
}

int Circle_get_radius(struct Circle* self) {
	return self->radius;
}

int Circle_area(struct Circle* self) {
	int int_pi;
	int_pi = 3;
	return int_pi* self->radius* self->radius;
}

typedef struct Square{
	int x;
	int y;
	int color;
	int side;
} Square;

Square* Square_init(struct Square* self, int side) {
	if (self == NULL) {
		self = (struct Square*) malloc(sizeof(struct Square));
	}
	
	self->side = side;
	return self;
}

int Square_get_side(struct Square* self) {
	return self->side;
}

int Square_area(struct Square* self) {
	return self->side* self->side;
}

typedef struct SquareWithCirclesOnCorners{
	int x;
	int y;
	int color;
	int side;
	int radius;
} SquareWithCirclesOnCorners;

SquareWithCirclesOnCorners* SquareWithCirclesOnCorners_init(struct SquareWithCirclesOnCorners* self, int side, int radius) {
	if (self == NULL) {
		self = (struct SquareWithCirclesOnCorners*) malloc(sizeof(struct SquareWithCirclesOnCorners));
	}
	
	self->side = side;
	self->radius = radius;
	return self;
}

int SquareWithCirclesOnCorners_area(struct SquareWithCirclesOnCorners* self) {
	int int_pi;
	int_pi = 3;
	return Square_get_side((struct Square*)self)* Square_get_side((struct Square*)self)+ 3* int_pi* Circle_get_radius((struct Circle*)self)* Circle_get_radius((struct Circle*)self);
}

typedef struct SquareWithCirclesOnCorners2{
	struct Square* s;
	struct Circle* c;
} SquareWithCirclesOnCorners2;

SquareWithCirclesOnCorners2* SquareWithCirclesOnCorners2_init(struct SquareWithCirclesOnCorners2* self, int side, int radius) {
	if (self == NULL) {
		self = (struct SquareWithCirclesOnCorners2*) malloc(sizeof(struct SquareWithCirclesOnCorners2));
	}
	
	self->s = Square_init(NULL, side);
	self->c = Circle_init(NULL, radius);
	return self;
}

int SquareWithCirclesOnCorners2_area(struct SquareWithCirclesOnCorners2* self) {
	int int_pi_part;
	int_pi_part = 3;
	return Square_get_side(self->s)* Square_get_side(self->s)+ 3* int_pi_part* Circle_get_radius(self->c)* Circle_get_radius(self->c);
}

int main(){
	struct Circle* c;
	struct Square* s;
	struct SquareWithCirclesOnCorners* s1;
	struct SquareWithCirclesOnCorners2* s2;
	c = Circle_init(NULL, 4);
	printf("%d\n", Circle_area(c));
	s = Square_init(NULL, 4);
	printf("%d\n", Square_area(s));
	s1 = SquareWithCirclesOnCorners_init(NULL, 3, 5);
	s2 = SquareWithCirclesOnCorners2_init(NULL, 3, 5);
	printf("%d\n", SquareWithCirclesOnCorners_area(s1));
	printf("%d\n", SquareWithCirclesOnCorners2_area(s2));
	
	return 0;
}