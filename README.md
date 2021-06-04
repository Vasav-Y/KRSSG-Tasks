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



