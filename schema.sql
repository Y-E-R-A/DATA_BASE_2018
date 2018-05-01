--Main Tables:
Create Table Credentials(cid serial primary key, cpassword varchar(20), cusername varchar(20), cemail varchar(50));

Create Table Users(uid serial unique, cid integer references Credentials(cid), ufirst_name varchar(20), ulast_name varchar(20), phone varchar(20), udescription varchar(100), primary key(uid,cid));

Create Table Groups(gid serial primary key, gname varchar(50), gdescription varchar(100), gdcreation timestamp, uid integer references Users(uid));

Create Table Messages(mid serial primary key, mdate timestamp, minfo varchar(500), uid integer references Users(uid));

Create Table Media(meid serial unique, mid integer references Messages(mid) , mename varchar(20), meaddress varchar(100), metype varchar(10),primary key(meid,mid));

--Relational Tables:
Create Table Participates(uid integer references Users(uid), gid integer references Groups(gid), primary key(uid,gid));

Create Table Administrate(uid integer references Users(uid), gid integer references Groups(gid), primary key(uid,gid));

Create Table Reply(mid integer references Messages(mid), rid integer references Messages(mid), primary key(mid,rid));

Create Table Receive(mid integer references Messages(mid), uid integer references Users(uid), primary key(uid,mid));

Create Table Reaction(mid integer references Messages(mid), uid integer references Users(uid), Rating varchar(20),primary key(uid,mid));

Create Table IsPart(mid integer references Messages(mid), gid integer references Groups(gid), primary key(gid,mid));

Create Table Contacts(uid integer references Users(uid), cid integer references Users(uid), primary key (cid, uid));