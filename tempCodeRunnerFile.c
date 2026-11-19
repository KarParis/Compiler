c = Circle_init(NULL, 4);
	printf("%d", Circle_area(c));
	s = Square_init(NULL, 4);
	printf("%d", Square_area(s));
	s1 = SquareWithCirclesOnCorners_init(NULL, 3, 5);
	s2 = SquareWithCirclesOnCorners2_init(NULL, 3, 5);
	printf("%d", SquareWithCirclesOnCorners_area(s1));
	printf("%d", SquareWithCirclesOnCorners2_area(s2));
	