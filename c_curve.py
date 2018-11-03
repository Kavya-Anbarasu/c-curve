from turtle import *
bob = Turtle()

def cCurve(level , steps):
	if level == 1:
		bob.forward(steps)
	
	elif level > 1:
		cCurve(level - 1 , steps)
		bob.right(90)
		cCurve(level - 1 , steps)
		bob.left(90)
		
def main():
	bob.speed(0)
	bob.penup()
	bob.goto(0 , -100)
	bob.pendown()
	cCurve(6 , 30)
	exitonclick()
	
main()