# KRSSG-Tasks
This repo contains the tasks for the selection of AI Team of KRSSG

KRSSG Task Round

Task_1->It contains two folders
           ->Bonus folder for the Bonus task
		   ->WithoutBonus for normal task

	�	Bonus-
			This contains the files for the bonus round
			First run casino.py file
			Then run client.py file and enter the name Client
			Then enter the number of players and the number of rounds
			After entering client.py will automatically close
			Then open the number of terminals as the number of players
			Now run player.py in 1st terminal , enter the name of the first player then 
			move to the second terminal and continue the same steps for all
			
			When name of all the players would have been entered they will receive 3 cards ,scale
			them down to scale of 1-13 and return max value to the casino server and on 
			this basis casino server will calculate the score for each  round and announce the winner at the end of the last round

	�	WithoutBonus-
			This contains all the files without bonus
			First open a terminal and run casino.py
			Then open three terminals run player.py in them
			Rest steps are almost same as that in the bonus round


Task_2 -> It contains two folders
           ->Bonus folder for the Bonus task
		   ->WithoutBonus for normal task

	�	Bonus-
			This contains the file for the bonus round.
			First run traffic.py in a terminal 
			Then run client.py in a terminal enter the name of the lane which it will represent and send data for
			Do the same step total 4 times to have a client which for each lane 
			Then move to the client which is for the lane A and enter the number of straight
			and right going cars do the same step for th client representing lane B,C and D
			
			After this traffic.py will run for 1 time step and clear the traffic
			If more car has to entered, enter them the same way as before
			If no more cars has to be entered then enter �-1� in both the inputs where client asks the number of straight and right going cars
			Then traffic.py will run until all the traffic is resolved

	�	WithoutBonus-
			First enter the input of cars in the file input.txt and then run traffic.py
			It will ask the number of time steps for which input will be given enter the number of lines in input.txt
			Then traffic.py will run until all the traffic is resolved
			**If running this in Vscode then keep input.txt and traffic.py in the same
			folder and open only that folder in vscode and run traffic.py because otherwise you�ll
			have to change the path of input.txt in reading it from traffic.py accordingly


Task_3-> 
	This contains the two images on which we had to draw path in the images folder and two python files
	The python file rrt_star_connect.py contains the code for the path generation between the source and destination points of the image
	To generate the path first we will need to enter the x and y coordinates of source as well as destination which can be found 
		using the check_coordinates.py file 
	First run the check_coordinates.py file to find the coordinates of the source and destination 
	Then run the rrt_star_connect.py file and enter the coordinates of source and destination and the image having the path will be 
	shown usign opencv
	In the image the blue line joining the source and destination gives us a short path between them
	Cyan blue circles tell us that they are part of source tree
	Yellow circles tell us that they are part of destination tree
	
	In the check_coordinates.py file to change the image which you want to read modify the 
	line 3 accordingly by specifying address of that image
	
	In the rrt_star_connect.py file to change the image which you want to read modify the line 411 accordingly



