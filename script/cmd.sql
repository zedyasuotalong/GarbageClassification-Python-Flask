create table user(
	id int NOT NULL AUTO_INCREMENT,
	name varchar(64)  null,
	password varchar(64) null,
    	sex tinyint default 0 check(sex in (0,1)),
    	age tinyint default 20 check(age >= 0),
    	phone varchar(16) unique not null,
    	email varchar(32),
    	job varchar(64),
    	level tinyint default 0,
    	head_img varchar(128) NULL,
	reg_time varchar(32) NULL,
    	primary key(id)
);
create table manager(
	username char(16) NOT NULL,
	password varchar(64) NOT NULL,
	primary key(username)
);
create table category(
	id int NOT NULL check(id in (0,1,2,3)),
	name varchar(64) NOT NULL,
	info varchar(512) NOT NULL,
	primary key(id)
);
create table garbage(
	id int NOT NULL AUTO_INCREMENT,
	name varchar(64) NOT NULL,
	category_id int NOT NULL,
	info varchar(512) NOT NULL,
	count int default 0,
	primary key(id),
	foreign key(category_id) references category(id)
);
create table question(
	id int NOT NULL AUTO_INCREMENT,
	picture varchar(128) NOT NULL,
	answer tinyint NOT NULL check(answer in (0,1,2,3)),
	explains varchar(512) NULL,
	status tinyint default 0 check(status in (0,1)),
	primary key(id)
);
create table test(
	id int NOT NULL AUTO_INCREMENT,
	question_id int NOT NULL,
	user_id int NOT NULL,
	my_answer tinyint NOT NULL,
	time varchar(32) NOT NULL,
	score tinyint NOT NULL,
	primary key(id, question_id),
	foreign key(question_id) references question(id),
	foreign key(user_id) references user(id)
);
