# ROS_practice

### Hello World of ROS


The node which sends out or publishes the information is called a Publisher Node and the one recieving it is called a Subscriber node. The Nodes communicate through a channel which is known as 'topic' and it has a certain type of 'message'. In this project the Publisher Node is task0_pub, Subscriber Node is task0_sub, and topic is /chatter.


Publisher and Subscriber scripts are implemented in Python for this project. These can be launched using publisher_subscriber.launch

### RRBot

RRBot or ''Revolute-Revolute Manipulator Robot'' is a robot used in ROS testing. Here, the joint positions of robot are manipulated with the help of a slightly modified publisher script making its joint at right angle with the fixed link.  
