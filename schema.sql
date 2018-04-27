-- This file contains the definitions of the tables used in the application.

--
Create Table Users(uid serial primary key, ufirst_name varchar(20), ulast_name varchar(20), phone varchar(10), udescription varchar(100));
--
Create Table Credentials(cid serial primary key, cpassword varchar(20), cusername varchar(20), cemail varchar(20), uid integer references Users(uid));
--
Create Table Groups(gid serial primary key, gname varchar(20), gdescription varchar(100), gdcreation timestamp, uid integer references User(uid));
--
Create Table Participates(uid integer references Users(uid), gid integer references Groups(gid), primary key(uid,gid));
--
Create Table Administrate(uid integer references Users(uid), gid integer references Groups(gid), primary key(uid,gid));
--
Create Table Message(mid serial primary key, mdate timestamp, minfo varchar(500), uid integer references Users(uid));
--
Create Table Reply(mid integer references Message(mid), rid integer references Message(mid), primary key(mid,rid));
--
Create Table Receive(mid integer references Message(mid), uid integer references Users(uid), primary key(uid,mid));
--
Create Table Reaction(mid integer references Message(mid), uid integer references Users(uid), Rating varchar(20),primary key(uid,mid));
--
Create Table IsPart(mid integer references Message(mid), gid integer references Groups(gid), primary key(gid,mid));
--
Create Table Media(meid serial primary key, mename varchar(20), meaddress varchar(100), mid integer references Message(mid));
--
Create Table Type(meid integer references Media(meid), type varchar(10), primary key(meid,type));
