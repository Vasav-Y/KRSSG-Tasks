This folder contains the task3 which
It has two folders 
  ->Images contains images of path and turtle moving on that path
  ->catkin_ws is the catkin workspace on which I have worked
  
 Important! ->Change the path of the image in the imread function accordingly
                It lies on line 435 in rrt_star_connect.py
                           line 12 in gotogoal.py
                           line 12 in without_pid.py
                           

How to run the file:

    ->create catkin_ws workspace
    ->catkin_make
    ->catkin_create package task3
    ->catkin_make
    ->source devel/setup.bash
    ->cd src/task3
    ->mkdir scripts
    ->cd scripts
    ->copy Images folder(catkin_ws/src/turtlesim_cleaner/src/) 
    ->copy gotogoal.py and rrt_star_connect.py
    ->cd ../..
    ->cd(now we are in catkin_ws) so run catkin_make
    ->source devel/setup.bash
    ->in a new terminal run roscore
    ->in a new terminal run turtlesim turtlesim_node
    ->in a new terminal cd into catkin_ws
    ->rosrun task3 rrt_star_connect.py
    ->in a new terminal rosrun task3 gotogoal.py
    ->This will open the image with the path and simulatneouly turtle will start running on that path
    ->Colour coding - 
                      Pink colour line final path
                      cyan blue circle are nodes of source tree
                      yellow circles are nodes of destination tree
                      
                      
     or
     ->copy src folder (catkin_ws)/src in existing workspace
     ->catkin_make
     ->source devel/setup.bash
     ->open new termial run roscore
     ->in a new terminal rosrun turtlesim turtlesim_node
     ->rosrun task3 rrt_star_connect.py
     ->in a new terminal rosrun task3 gotogoal.py
     ->This will open the image with the path and simulatneouly turtle will start running on that path
     
     
    
    
