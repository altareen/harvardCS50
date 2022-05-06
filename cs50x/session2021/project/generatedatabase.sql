CREATE TABLE IF NOT EXISTS instructors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS departments (
    id SERIAL PRIMARY KEY,
    department VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS courses (
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    instructor_id INTEGER REFERENCES instructors (id),
    enrollment INTEGER NOT NULL,
    capacity INTEGER NOT NULL,
    section INTEGER NOT NULL,
    department_id INTEGER REFERENCES departments (id),
    description VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL,
    hash VARCHAR NOT NULL,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    grade_level INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS students_courses (
    student_id INTEGER REFERENCES students (id),
    course_id INTEGER REFERENCES courses (id)
);

CREATE UNIQUE INDEX username ON students (username);

INSERT INTO instructors (first_name, last_name) VALUES ('Albus', 'Dumbledore');
INSERT INTO instructors (first_name, last_name) VALUES ('Rubeus', 'Hagrid');
INSERT INTO instructors (first_name, last_name) VALUES ('Gilderoy', 'Lockhart');
INSERT INTO instructors (first_name, last_name) VALUES ('Remus', 'Lupin');
INSERT INTO instructors (first_name, last_name) VALUES ('Quirinus', 'Quirrell');
INSERT INTO instructors (first_name, last_name) VALUES ('Severus', 'Snape');

INSERT INTO departments (department) VALUES ('Mathematics');
INSERT INTO departments (department) VALUES ('Science');
INSERT INTO departments (department) VALUES ('Humanities');
INSERT INTO departments (department) VALUES ('Languages');
INSERT INTO departments (department) VALUES ('English');
INSERT INTO departments (department) VALUES ('Art');

INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('Concocting Magic Potions',6,0,25,3,2,'Potions is described as the art of creating mixtures with magical effects. It requires the correct mixing and stirring of ingredients at the right times and temperatures.');
INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('Incantations and Charms',1,0,25,5,5,'Charms are the types of spells concerned with giving an object new and unexpected properties, and hence this class mainly consists on learning those sorts of spells. Charms classes are described as notoriously noisy and chaotic, as the lessons are largely practical.');
INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('Transfiguration',2,0,15,1,1,'Transfiguration is the art of changing the form or appearance of an object, and hence this is what this class teaches. Transfiguration is a theory-based subject, including topics such as Switching Spells, which involves altering only a part of some object, such as giving a human rabbit''s ears.');
INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('Defence Against the Dark Arts',3,0,20,4,6,'This class teaches students defensive techniques to defend against the Dark Arts, and to be protected from dark creatures. Skills learned in this class will be instrumental in defeating a malicious adversary.');
INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('History of Magic',4,0,18,2,3,'History of Magic is the study of magical history. These lessons are depicted as some of the most boring at Hogwarts. They are only lectures, given without pause, about significant events in wizarding history.');
INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('Arithmancy',5,0,23,6,1,'Arithmancy is a branch of magic concerned with the magical properties of numbers. Arithmancy is reportedly quite difficult, as it requires memorising or working with many charts.');
INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('Herbology',3,0,15,5,6,'Herbology is the study of magical plants and how to take care of, utilise and combat them. Hogwarts has at least three greenhouses, holding a variety of magical plants of varying degrees of lethality.');
INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('Care of Magical Creatures',6,0,12,3,4,'Care of Magical Creatures is the class which instructs students on how to care for magical beasts. Classes are held outside the castle, and students can expect to interact with dragons, werewolves and elk.');
INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('Divination',1,0,25,6,5,'Divination is the art of predicting the future. Various methods are described, including tea leaves, fire-omens, crystal balls, palmistry, cartomancy(including the reading of conventional playing cards and the tarot), astrology, and dream interpretations.');
INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('Muggle Studies',5,0,10,1,4,'This class involves the study of the Muggle(non-magical) culture from a wizarding point of view. It also includes Muggle Art and Muggle Music. The only need for witches and wizards to learn about Muggle ways and means is to ensure that they can blend in with Muggles when the need arises.');
INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('Alchemy',2,0,18,4,2,'Alchemy is a sort of composite subject between Transfiguration, Potions and Muggle Chemistry, focused roughly on the transmutation of chemical substances into other forms, such as turning lead into gold.');
INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('Astronomy and Celestial Bodies',4,0,23,2,3,'Lessons involve observations of the night skies with telescopes. Known student homework activities include learning the names of stars, constellations and planets, and their location, movements, and environments.');
INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('Study of Ancient Runes',4,0,15,5,4,'This is a general theoretical subject that studies ancient runic scripts.');
INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('Ancient Studies',2,0,25,4,2,'This subject focuses on ancient magic as practiced by various historical cultures, such as the ancient Egyptians'' spells.');
INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('Broomstick Aeronautics',6,0,17,2,3,'This course is largely aimed towards providing students with a basic understanding of the most elementary principles behind the study of broomology. In general, students learn how to handle a broom and progressively work on various techniques and aeronautics performed while in flight, as well as receiving proper instructions on the subject of proper broom care and maintenance.');
INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('Magical Theory',1,0,23,6,1,'The objectives of this course include demystifying the practice of magic for new students by providing them with a basic understanding of what magic was, covering topics such as what made spells work, how did energy transfer during spellcasting work and the wand''s role in channelling it, why some spells seemed to be a matter of will, whereas others seemed to be a question of intent, how and why magic manifested itself in unexpected and sometimes dangerous ways when wizards failed to understand and manage their own feelings, how it was that they were able to keep it in check through emotional stability and exercised force of mind, and introducing them to the Fundamental Laws of Magic.');
INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('Muggle Art',3,0,11,1,6,'Muggle Art is a class where students paint, draw, and otherwise depict artistic things.');
INSERT INTO courses (title, instructor_id, enrollment, capacity, section, department_id, description) VALUES ('Xylomancy',5,0,18,3,5,'Xylomancy is a class in which students learn about the often overlooked way of divination, which often has something to do with twigs.');

-- password: magicwand
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('hpotter','sha256$rCK1qtP1$16f217c9d34f55b87d022fc79cb9a4c1f57aa8d24950aece4fb83a7f57df6cc0','Harry','Potter',12);
-- password: dragonsbane
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('hgranger','sha256$wEJ0gdKS$17a346f452fa7ce618ddf495a40fef97dad6d53e7d7a602773a353cbdd33f23d','Hermione','Granger',12);
-- password: broomstick
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('rweasley','sha256$cOVcFFWv$d59d19cff310abead627b586516c9cc300cd139d31a0b04edc0918d4d653a2cb','Ron','Weasley',12);
-- password: blackcauldron
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('dmalfoy','sha256$hhEdBhIf$7ff13d6863c90e552415627ac2114f9d8cc4de6ebaec28d8fce2ff8c70a3bd68','Draco','Malfoy',12);
-- password: charmedpotion
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('gweasley','sha256$Us8IlHkU$ab9a084dd356953d2743559ecbe4e8d2f64115eb14cd680ceb282a462a34d413','Ginny','Weasley',12);
-- password: castedspells
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('ccreevy','sha256$OVxD6Y3i$da72a71a59f926b1f36abe66ba7b393a185c37384beacd43472c7e1daea663c2','Colin','Creevy',12);
-- password: hiddenstreets
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('sfinnigan','sha256$BT5wwlvX$d5351b65e7ac7f1cbfecd3f4327b57abe8bacff225897a6b16f0c7a531445777','Seamus','Finnigan',12);
-- password: ancientpubs
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('habbott','sha256$2iime3LQ$364999e28a2f5f10643a6d8931c96e3b63b4773be96deb9e580c76700c1dea08','Hannah','Abbott',12);
-- password: countrymanors
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('pparkingson','sha256$qh9UlI0G$b2c2b8dc582798f793214edcd8d08d740aa863b3aac94eae79367fab1a053894','Pansy','Parkingson',11);
-- password: secludedcastles
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('zsmith','sha256$a4Rek5en$3da7756041425043f1e3ad048196b20b11b4846feb466d6670ca08f32d1ce07f','Zacharias','Smith',11);
-- password: ordinarymuggles
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('bzabini','sha256$gyhoYcDu$7cb11c518760917f902f4f42a0a1723d5511bc484352755959a2a8df31211438','Blaise','Zabini',11);
-- password: hogwartsacademy
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('dthomas','sha256$skxvxIZi$e85d8c468c1383e8a691c2889f2e1d8b0245fedfa22212338f2c4c902b2b110b','Dean','Thomas',11);
-- password: wizardryschool
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('mbulstrode','sha256$hkklKRnz$9b6b46268c152ceda8aa7f2b7be280987515ef0cf06aa964da9449574f398d85','Millicent','Bulstrode',11);
-- password: wildcentaurs
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('tboot','sha256$xIGfyd8E$d415141964875a57b165085cfe3a3c7fa4c1d740dc935bf04718f8bb5380c585','Terry','Boot',11);
-- password: invisiblecloak
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('emacmillan','sha256$0I4BRmvq$c92c42070fe6f0112e6e574b00532de0e34dc45ed951f8e547deca479c5c7c7f','Ernie','Macmillan',10);
-- password: potionsmaster
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('vcrabbe','sha256$ijTbV3Sp$37c2509ff8be5ced72a4a35ea2b5d8a2da917484f858a88094c240696a0084b6','Vincent','Crabbe',10);
-- password: fantasticbeasts
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('ggoyle','sha256$rVxv3xfU$43f588c47a99b7a0ed31d18a0728a96140d7bbade01cdf7e55ce3d3c6af391c2','Gregory','Goyle',10);
-- password: sortinghat
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('lbrown','sha256$QxoyT2aJ$b54dbbe65e4975b50e2e41bebfce535ad22c0e1dd8a29a15e3da56c5251d00a4','Lavender','Brown',10);
-- password: shrewdmystery
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('kbell','sha256$x5Tlvzyz$84380e94dc0adc9c2bcab0d9ca15b106797f0930574801648fbfbb153da0f347','Katie','Bell',10);
-- password: urbanfantasy
INSERT INTO students (username, hash, first_name, last_name, grade_level) VALUES ('ppatil','sha256$vjhVUs6G$f299e755202f567f21c3db1253583591f120b6ccea0be63654d5278ce2cf4d05','Parvati','Patil',10);
